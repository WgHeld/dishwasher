import relayr 
import time
from relayr import Client
from relayr.dataconnection import MqttStream


wg_token='Pm8az.iBVc6DBdHI7iKI9KDFu-VdKW4_'

dev_id="ac8f56f3-9ccc-4896-b2e0-a5a9fc7e603b"
infrared='ac8f56f3-9ccc-4896-b2e0-a5a9fc7e603b'
dishwasher='f4ab513e-590d-494f-8586-2e06af2d186d'
gyroscope='a2e4d803-82d2-4504-add2-8e99111d9178'
microphone='89287aad-db10-4303-ad01-5547c67eca96' 
thermometer='a7ec5e46-4f6e-4193-a21a-5b5c7cb34485' 
light='103156b3-1a78-42c2-a4af-1512721ded3d'
bridge='ada09702-5898-42fb-9c42-7ef0c1a1dd45' 

def mqtt_callback(topic, payload):
    print('%s %s' % (topic, payload))


c = relayr.Client(token=wg_token)
usr = c.get_user()
"""
devs = usr.get_devices()
for d in devs:
    info = d.get_info()
    print("dev '%s' (%s) " % (info.name, info.id))
    #d.switch_led_on(True)
    #print("on")

apps = usr.get_apps()
for a in apps:
    print(a)
"""

dev = c.get_device(id=dishwasher)
app = c.get_app()
print(app)

stream = MqttStream(mqtt_callback, [dev])
stream.start()
time.sleep(600)
stream.stop()
"""
m = dev.get_info()
print(m)
conn = usr.connect_device(app, m, mqtt_callback )
conn.start()

print("Monitoring '%s' (%s) for 600 seconds..." % (m.name, m.id))
try:
    time.sleep(600)
except KeyboardInterrupt:
    print('')
conn.stop()
print("Stopped")
"""

