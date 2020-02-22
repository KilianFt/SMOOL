import RPi.GPIO as GPIO
from time import sleep

def activate(x):
	GPIO.output(x, True)
	sleep(5)
	GPIO.output(x, False)


def callbackB1(channel):
	print('opening 1')
	activate(myLED[0])


def callbackB2(channel):
	print('closing 1')
	activate(myLED[1])


def callbackB3(channel):
	print('opening 2')
	activate(myLED[2])


def callbackB4(channel):
	print('closing 2')
	activate(myLED[3])


def main():
	global myLED
	myLED = [14,15,16,17]
	myB = [9,10,11,12]

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(myLED, GPIO.OUT, initial = 0)
	GPIO.setup(myB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(myB[0], GPIO.FALLING, callback= (callbackB1))
	GPIO.add_event_detect(myB[1], GPIO.FALLING, callback= (callbackB2))
	GPIO.add_event_detect(myB[2], GPIO.FALLING, callback= (callbackB3))
	GPIO.add_event_detect(myB[3], GPIO.FALLING, callback= (callbackB4))

	while True:
		pass

if __name__ == '__main__':
	main()
