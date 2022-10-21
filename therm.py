import time
from PublishTherm import PublishTherm

p=PublishTherm()

sensor="28-000008579306"
therm = None
with open("/sys/bus/w1/devices/"+sensor+"/temperature", "r") as f:
    therm = f.read()
    therm = float(therm)/1000

#power on reset je nestatna hodnota 85
if therm == 85:
    exit()
p.publish(therm)

