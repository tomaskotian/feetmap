#pip install pyserial

import serial.tools.list_ports

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

serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()

serialInst.reset_input_buffer()
while True:
    
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'),end="")
