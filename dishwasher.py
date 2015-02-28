#
# sudo pip install -U git+https://github.com/relayr/python-sdk
#
import relayr 
import time
from relayr import Client
from relayr.dataconnection import MqttStream

DO_DBG_RAPI=True
WG_TOKEN='Pm8az.iBVc6DBdHI7iKI9KDFu-VdKW4_'
stop_daemon=False

INFRARED='ac8f56f3-9ccc-4896-b2e0-a5a9fc7e603b'
DISHWASHER='f4ab513e-590d-494f-8586-2e06af2d186d'
GYROSCOPE='a2e4d803-82d2-4504-add2-8e99111d9178'
MICROPHONE='89287aad-db10-4303-ad01-5547c67eca96' 
THERMOMETER='a7ec5e46-4f6e-4193-a21a-5b5c7cb34485' 
LIGHT='103156b3-1a78-42c2-a4af-1512721ded3d'
BRIDGE='ada09702-5898-42fb-9c42-7ef0c1a1dd45' 

def dbg_rapi(msg):
    if DO_DBG_RAPI:
        print(msg)

def rapi_callback(topic, payload):
    print('topic:%s payload: >>%s<<<' % (topic, payload))


c = relayr.Client(token=WG_TOKEN)
usr = c.get_user()

dev = c.get_device(id=DISHWASHER)
app = c.get_app()
dbg_rapi(app)

stream = MqttStream(rapi_callback, [dev])

stream.start()
while not stop_daemon:
    time.sleep(100)
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





