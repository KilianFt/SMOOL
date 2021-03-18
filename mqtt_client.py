import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep

class MQTTClient:
    def __init__(self):
        ip_address = "10.240.1.25"
        port = 1883

        self.gpio_pins = [17,27,23,24]#[14,15,16,17]
        #self.button_pins = [20,21]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pins, GPIO.OUT, initial = 0)
        #GPIO.setup(button_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        #GPIO.add_event_detect(self.button_pins[0], GPIO.FALLING, callback= (self.open_all))
        #GPIO.add_event_detect(self.button_pins[1], GPIO.FALLING, callback= (self.close_all))
        
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

#    def open_all(self, channel):
#        print('opening all')
#        GPIO.output([self.gpio_pins[0], self.gpio_pins[2]], True)

#    def close_all(self, channel):
#        print('closing all')
#        GPIO.output([self.gpio_pins[1], self.gpio_pins[3]], True)
    
    def activate(self, x):
        GPIO.output(x, True)
        sleep(5)
        GPIO.output(x, False)

        
    def shutter_contol(self, wanted_state):
        #print("changing shutter state\n")
        if wanted_state == "OPEN":
            print("opening...")
            self.client.publish("/shutter/state", "OFFEN")
            # do GPIO here
            self.activate(self.gpio_pins[0])

        elif wanted_state == "CLOSE":
            print("closing...")
            self.client.publish("/shutter/state", "ZU")
            # do GPIO here
            self.activate(self.gpio_pins[2])

        elif wanted_state == "STOP":
            self.client.publish("/shutter/state", "ERROR")
            # well, problem
            print("stopping...")
            
            # setting all to 0           
            GPIO.output(self.gpio_pins, False)

        else:
            print("Unknown command")
            return -1
        
        return 1
        
    
if __name__ == "__main__":
    MQTTClient()


