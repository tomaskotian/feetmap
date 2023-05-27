#pip install pyserial
import usb_connection as usb

sensor = usb.ConnectUSB()
usb.Read(sensor)
