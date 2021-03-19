import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep
import threading

# TODO
# add threading, so that multiple actions can take place on the same time

class MQTTClient:
    def __init__(self):
        ip_address = "10.240.1.19"
        port = 1883

        self.gpio_pins = [17,27,23,24]#[14,15,16,17]
        #self.button_pins = [20,21]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pins, GPIO.OUT, initial = 0)
        #GPIO.setup(button_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        #GPIO.add_event_detect(self.button_pins[0], GPIO.FALLING, callback= (self.open_all))
        #GPIO.add_event_detect(self.button_pins[1], GPIO.FALLING, callback= (self.close_all))
        
        #self.close_thread = threading.Thread(target=self.threaded_timer, args=(1,))
        #self.open_thread = threading.Thread(target=self.threaded_timer, args=(2,))
        #self.close_thread.start()
        #self.open_thread.start()
        
        self.state_topic_1 = "/makerspace/shutter1/state"
        self.cmd_topic_1 = "/makerspace/shutter1/cmd"

        self.state_topic_2 = "/makerspace/shutter2/state"
        self.cmd_topic_2 = "/makerspace/shutter2/cmd"
        
        self.client = mqtt.Client()
        self.client.username_pw_set(username="fasw",password="fasw")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(ip_address, port, 60)

        self.client.loop_forever()
        
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(self.cmd_topic_1)
        self.client.subscribe(self.cmd_topic_2)
        
    def on_message(self, client, userdata, msg):
        cmd = msg.payload.decode()
        #print(msg)
        state = self.shutter_contol(cmd, msg.topic)
    
    def threaded_timer(self, x):
        # not used yet
        sleep(5)
        print(x)
        GPIO.output(17, False)
        
    def activate(self, x):
        GPIO.output(x, True)
        #self.open_thread.join(x)
        sleep(5)
        GPIO.output(x, False)
        
    def shutter_contol(self, wanted_state, topic):
        #print(topic)
        #print(self.cmd_topic_1)
        if topic == self.cmd_topic_1:
            _up = 0
            _down = 1
            _state_topic = self.state_topic_1
        elif topic == self.cmd_topic_2:
            _up = 2
            _down = 3
            _state_topic = self.state_topic_2
        else:
            return -1
            
        if wanted_state == "OPEN":
            print("opening...")
            self.activate(self.gpio_pins[_up])
            self.client.publish(_state_topic, "OFFEN")

        elif wanted_state == "CLOSE":
            print("closing...")
            self.activate(self.gpio_pins[_down])            
            self.client.publish(_state_topic, "ZU")

        elif wanted_state == "STOP":
            print("stopping...")
            self.client.publish(_state_topic, "STOP")           
            GPIO.output(self.gpio_pins, False)

        else:
            print("Unknown command")
            return -1
        
        return 1
        
    
if __name__ == "__main__":
    MQTTClient()




