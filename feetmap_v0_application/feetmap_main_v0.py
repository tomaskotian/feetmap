#pip install pyserial
#pip install tk
#pip install Pillow

#Debug mode without connected sensor
debug = False

import usb_connection as usb
import window as wd
from threading import Timer

measure_interval = 0.1
time_cnt = 0 

def ReadValues():
    global time_cnt 
    if app.calibrate:
        sensor.Calibrate()
        app.calibrate = False
    sensor.GetData()
    data = sensor.ReadBuffer()
    if data != []:
        if time_cnt >= app.slider.get():
            cnt = int(app.slider.get()/measure_interval)
            data = sensor.ToAvg(data,cnt)
            data = sensor.ToPercent(data)
            app.UpdateValues(data)
            time_cnt = 0
        else:
            sensor.BufferData(data)
    Timer(measure_interval,ReadValues).start()
    time_cnt += measure_interval

app = wd.SetupWindow() 
sensor = usb.USBConnection(debug)
sensor.Calibrate()
ReadValues()
app.window.mainloop()


