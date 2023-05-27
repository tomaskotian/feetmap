import serial.tools.list_ports
import sys

def ConnectUSB():
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()

    portList = []
    for port in ports:
        portList.append(str(port))
        if 29987 == port.pid:
            print(f"Connecting...{str(port)}")
            portVar = port.device
            break
        else:
            print("Device is not connected!!!")
            sys.exit()
            
    if len(portList) == 0:
        print("Device is not connected!!!")
        sys.exit()


    serialInst.baudrate = 115200
    serialInst.port = portVar
    serialInst.open()
    serialInst.reset_input_buffer()
    return serialInst

def Read(serialInst):
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            print(packet.decode('utf'),end="")