#pip install pyserial
#pip install tk
#pip install Pillow

#Debug mode without connected sensor
debug = False

import usb_connection as usb
import window as wd
from threading import Timer

def ReadValues():
    if app.calibrate:
        sensor.Calibrate()
        app.calibrate = False
    sensor.GetData()
    data = sensor.ReadBuffer()
    if data != []:
        data = sensor.ToPercent(data)
        app.UpdateValues(data)
    Timer(0.1,ReadValues).start()

app = wd.SetupWindow() 
sensor = usb.USBConnection(debug)
sensor.Calibrate()
ReadValues()
app.window.mainloop()


