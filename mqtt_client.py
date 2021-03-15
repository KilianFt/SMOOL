import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self):
        ip_address = "10.240.1.25"
        port = 1883
        
        self.state_topic = "/shutter/state"
        self.cmd_topic = "/shutter/cmd"
        
        self.client = mqtt.Client()
        self.client.username_pw_set(username="fasw",password="fasw")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(ip_address, port, 60)

        self.client.loop_forever()
        
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(self.cmd_topic)
        
    def on_message(self, client, userdata, msg):
        cmd = msg.payload.decode()
        #print(cmd)
        state = self.shutter_contol(cmd)

        
    def shutter_contol(self, wanted_state):
        #print("changing shutter state\n")
        if wanted_state == "OPEN":
            print("opening...")
            self.client.publish("/shutter/state", "OFFEN")
            # do GPIO here
        elif wanted_state == "CLOSE":
            print("closing...")
            self.client.publish("/shutter/state", "ZU")
            # do GPIO here
        elif wanted_state == "STOP":
            self.client.publish("/shutter/state", "ERROR")
            # well, problem
            print("stopping...")
        else:
            print("Unknown command")
            return 0
        
        return 1
        
    
if __name__ == "__main__":
    MQTTClient()


