import serial.tools.list_ports
import sys, time

class USBConnection():
    def __init__(self,debug):
        self.debug = debug
        self.constants = [32398597, 32291861, 32600000 , 32487481, 32437759, 32259989, 33140000, 32338967, 1190777, 904007]
        self.values = [0,0,0,0,0,0,0,0,0,0]
        
        if not(self.debug):
            self.Startup()

    def Startup(self):
        ports = serial.tools.list_ports.comports()
        self.serialInst = serial.Serial()
        portList = []
        portVar = ""
        for port in ports:
            portList.append(str(port))
            if 29987 == port.pid:
                print(f"Connecting...{str(port)}")
                portVar = port.device
                break
        if portVar == "" or len(portList) == 0:
            print("Device is not connected!!!")
            sys.exit()

        self.serialInst.baudrate = 115200
        self.serialInst.port = portVar
        self.serialInst.timeout = 0.1
        self.serialInst.open()
        self.serialInst.reset_input_buffer()
        time.sleep(2) 
        print(f"Connected to {str(port)}")

    def Read(self):
        """
        test function for answer 10 sensors
        """
        for x in range(10): 
            packet = self.serialInst.readline()
            print(packet.decode('utf'),end="")

    def ReadBuffer(self):
        if not(self.debug):
            tmp = []
            for x in range(10):
                tmp.append(self.serialInst.readline().decode('utf'))
            print(tmp)
            if self.ControlData(tmp):
                return  self.ToKg(tmp)
            else:
                print("ERROR")
                return []
        else:
            return [1, 2, 1 , 2, 3000000, 3000000, 3238967, 3238967, 190777, 90407]
        
    def Buffer(self):
        tmp = []
        if not(self.debug):
            for x in range(10):
                tmp.append(self.serialInst.readline().decode('utf'))
            if self.ControlData(tmp):
                return  self.Parse(tmp)
            else:
                print("ERROR")
                return []
        else:
            return [32398597, 32291861, 32600000 , 32487481, 32437759, 32259989, 33140000, 32338967, 1190777, 904007]

    def Parse(self,data):
        tmp = []
        for b in data:
            tmp.append(int(b.split()[0].split('-')[-1]))
        return tmp


    def SendChar(self,char):
        self.serialInst.write(char)

    def GetData(self):
        """
        function witch send S via usb to get values from all sensors
        """
        if not(self.debug):
            self.SendChar(b'S')

    def Calibrate(self):
        self.GetData()
        self.constants = self.Buffer()

    def ToKg(self,data):
        tmp = []
        weight = []
        constants  = self.constants
        if data[0] == '':
            return [0,0,0,0,0,0,0,0,0,0]
        for b in data:
            tmp.append(int(b.split()[0].split('-')[-1]))
        for i in range(len(tmp)):
            if i == 9:
                if tmp[i] >= constants[i]:
                    val = int((33554432-tmp[i])/25000) + 35
                else:
                    val = int((constants[i]-tmp[i])/25000)
            elif i == 8:
                if tmp[i] >= constants[i]:
                    val = int((33554432-tmp[i])/25000) + 47
                else:
                    val = int((constants[i]-tmp[i])/25000)
            else:
                val = int((constants[i]-tmp[i])/25000)
            if val < 0:
                weight.append(0)
            else:
                weight.append(val)
        return weight

    def ControlData(self,data):
        template = ["L1","L2","L3","L4","L5","R1","R2","R3","R4","R5"]

        if len(template) == len(data):
            i = 0
            for t in template:
                if t in data[i]:
                    i += 1
                else:
                    print(f"template {template}")
                    print(f"template {data}")
                    return False
            return True
        else:
            print(f"Missing data from sensor {data}")
            return False

    def BufferData(self,data):
        for i in range(len(data)):
            self.values[i] += data[i]

    def ToAvg(self,data,cnt):
        values = []
        if cnt == 0:
            return data
        else:
            for i in range(len(data)):
                values.append(int(self.values[i]/cnt))
            return values


    def ToPercent(self,data):
        l_total = data[0] + data[1] + data[2] + data[3] + data[4] 
        r_total = data[5] + data[6] + data[7] + data[8] + data[9] 

        if (data[8] + data[9]) ==  r_total:
            data = data[:5] + [0,0,0,0,0]
            r_total = 0

        min_weight = 10
        if r_total <= min_weight:
            data = data[:5] + [0,0,0,0,0] 
            r_total = 0
        if l_total <= min_weight:
            data = [0,0,0,0,0] + data[5:]
            l_total = 0
        total = l_total + r_total
        tmp = [0,0,0,0,0,0,0,0,0,0,0,0]
        
        if total != 0:
            tmp[10] = int((l_total/total)*100)
            tmp[11] = int((r_total/total)*100)
        
        if l_total != 0:
            for i in range(5):
                tmp[i] = int((data[i]/l_total)*100)

        if r_total != 0:
            for i in range(5,10):
                tmp[i] = int((data[i]/r_total)*100)

        return tmp
