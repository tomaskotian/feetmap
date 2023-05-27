#pip install pyserial
#pip install tk

#import usb_connection as usb
import window as wd
import memory as me
import random

print()

memory = me.Memory()
for i in range(0,10):
    r = []
    l = []
    for x in range(5):
        r.append(random.randint(0,9))
        l.append(random.randint(0,9))
    memory.Add(r,l)


# app = wd.SetupWindow()
# app.window.mainloop()

# sensor = usb.USBConnection()
# sensor.Read()
