#pip install pyserial
import usb_connection as usb

sensor = usb.USBConnection()
sensor.Read()
