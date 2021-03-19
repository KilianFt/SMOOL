import RPi.GPIO as GPIO
from time import sleep

class ManualControl:
    def __init__(self):

        self.gpio_pins = [17,27,23,24]#[14,15,16,17]
        self.button_pins = [20,21]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pins, GPIO.OUT, initial = 0)
        GPIO.setup(self.button_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.add_event_detect(self.button_pins[0], GPIO.FALLING, callback= (self.open_all), bouncetime=300)
        GPIO.add_event_detect(self.button_pins[1], GPIO.FALLING, callback= (self.close_all), bouncetime=300)
        self.loop()

    def open_all(self, channel):
        print('opening all')
        GPIO.output([self.gpio_pins[0], self.gpio_pins[2]], True)
        while GPIO.input(self.button_pins[0]) == GPIO.LOW:
            pass
        GPIO.output([self.gpio_pins[0], self.gpio_pins[2]], False)
        #sleep(1)

    def close_all(self, channel):
        print('closing all')
        GPIO.output([self.gpio_pins[1], self.gpio_pins[3]], True)
        while GPIO.input(self.button_pins[1]) == GPIO.LOW:
            pass
        GPIO.output([self.gpio_pins[1], self.gpio_pins[3]], False)
            
    def loop(self):
        while True:
            sleep(0.5)
            pass
        
        GPIO.cleanup()

if __name__ == "__main__":
    ManualControl()



