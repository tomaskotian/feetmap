import serial.tools.list_ports
import sys, time

class USBConnection():
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()

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

    serialInst.baudrate = 115200
    serialInst.port = portVar
    serialInst.open()
    serialInst.reset_input_buffer()
    time.sleep(2) 

    def Read(self):
        for x in range(10): 
            packet = self.serialInst.readline()
            print(packet.decode('utf'),end="")

    def ReadBuffer(self):
        tmp = []
        if self.serialInst.in_waiting:
            for i in range(5):
                text = self.serialInst.readline().decode('utf')
                if not(text.startswith("L") or text.startswith("R")):
                    text = self.serialInst.readline().decode('utf')
                tmp.append(self.serialInst.readline().decode('utf'))
            self.serialInst.reset_input_buffer()
            return tmp

    def SendChar(self,char):
        self.serialInst.write(char)

    def GetData(self):
        """
        function witch send S via usb to get values from all sensors
        """
        self.SendChar(b'S')