# Import Libraries
import os
import time
import RPi.GPIO as GPIO

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up variables for the LED, Buzzer and switch pins
LEDRed = 18
LEDYellow = 23
LEDGreen = 24
PinBuzzer = 22
ButtonPin = 25
BuzzerCount = 5
PedRed = 17
PedGreen = 27 # Even though it's a blue LED

# Set up each of the input (swich) and output (LEDs, Buzzer) pins
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDYellow, GPIO.OUT)
GPIO.setup(LEDGreen, GPIO.OUT)
GPIO.setup(PinBuzzer, GPIO.OUT)
GPIO.setup(ButtonPin, GPIO.IN)
GPIO.setup(PedRed, GPIO.OUT)
GPIO.setup(PedGreen, GPIO.OUT)

# Define a function for the initial state (green LED on, rest off)
# (If you have the 'second pedestrian' LEDs, turn the red on & green
# off)
def StartGreen():
	# Remember all code in the function is indented
	GPIO.output(LEDGreen, GPIO.HIGH)
	GPIO.output(PedRed, GPIO.HIGH)
	GPIO.output(PedGreen, GPIO.LOW)


# Turn the green off and the amber on for 3 seconds
# (Pedestrian red LED stays lit)
def SteadyAmber():
	# Remember all code in the function is indented
	GPIO.output(LEDGreen, GPIO.LOW)
	GPIO.output(LEDYellow, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(LEDYellow, GPIO.LOW)

# Turn the abber off, and then the red on for 1 second
def SteadyRed():
	# Remember all code in the function is indented
	GPIO.output(LEDRed, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(LEDRed, GPIO.LOW)

# Sound the buzzer for 4 seconds
# (If you have the 'pedestrian' LEDs, turn the red off and green on)
def StartWalking():
	GPIO.output(PedRed, GPIO.LOW)
	GPIO.output(PedGreen, GPIO.HIGH)
	while (count > 0):
		GPIO.output(PINBuzzer,GPIO.HIGH)
		time.sleep(.5)
		GPIO.output(PINBuzzer,GPIO.LOW)
		time.sleep(.5)
		count = count - 1

#Try and make the buzzer buzz on and off, half a second of
#sound followed by half a second of silence

# Turn the buzzer off and wait for 2 seconds
# (If you have a second green 'pedestrian' LED, make it flash on and
# off for the two seconds)
def DontWalk():
	# Remember all code in the function is indented

# Flash the amber on and off for 6 seconds
# (And the green 'pedestrian' LED too)
def FlashingAmberGreen():
	# Remember all code in the function is indented

# Flash the amber for one more second
# (Turn the green 'pedestrian' LED off and the red on)
def FlashingAmber():
	# Remember all code in the function is indented

# Go through the traffic light sequence by calling each function
# one after the other.
def TrafficLightSequence():
	# Remember all code in the function is indented

os.system('clear') #Clears the screen
print "Traffic Lights"
# Initialise the traffic lights
StartGreen()

# Here is the loop that waits at lease 20 seconds before
# stopping the cars if the button has been pressedS
while True: #Loop around forever
	ButtonNotPressed = True # Button has not been pressed
	start = time.clock() # Records the current time
	while ButtonNotPressed: # While the button as not been pressed
		time.sleep(0.1) # Wait for 0.1s
		if GPIO.input(ButtonPin) == False: # If the button is pressed
			ButtonNotPressed = False # Button has been pressed
			if time.clock()-start<=20: # If under 20 seconds
				time.sleep (20-start) # Wait until 20s is up
			TrafficLightSequence() # Runthe traffic light sequence
GPIO.cleanup() 
