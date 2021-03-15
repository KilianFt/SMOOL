import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    #client.subscribe("$SYS/#")
    client.subscribe("/shutter/cmd")
    #client.publish("")
    
def on_message(client, userdata, msg):
    cmd = int(msg.payload)
    #print(cmd)
    if not shutter_contol(cmd):
        print("Failed to close shutter")
        client.publish("/shutter/state", 0)

    
def shutter_contol(wanted_state):
    print("changing shutter state\n")
    # do gpio here
    _success = 0
    
    #print("MOVING...")
    _success = 1
    
    # check if shutter closed
    if _success == 1:
        return True
    else:
        return False

    
client = mqtt.Client()
client.username_pw_set(username="fasw",password="fasw")
client.on_connect = on_connect
client.on_message = on_message

ip_address = "10.240.1.25"
client.connect(ip_address, 1883, 60)

client.loop_forever()