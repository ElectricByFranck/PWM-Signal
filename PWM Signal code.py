import machine
from machine import UART, Pin, PWM, ADC
import time

#Initialisation the UART serial communication protocols
#DAK:uart = UART(1, baurate=9600, tx=Pin(8), rx=(9))
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))   # Fixed the typo in the Pin argument

# Note that you can test this on a single pico by connecting Tx pin 8 on the 'UART' header to Rx pin 9 ... for a serial loopback connection
# You will need a wire for this, too, of course! :-)

uart.init(bits=8, parity=None, stop=1)

#Initialisation of the PWM Pin
#DAK:pwm_pin=Pin(15)
pwm_pin=Pin(17) # I used pin 17 so that I could see the green LED get brighter or dimmer, based on the PWM duty cycle value (trick for testing!) 
pwm=PWM(pwm_pin)

#Set up the frequence at 1000Hz
pwm.freq(1000) 

#Initialisation of the ADC Pin
#DAK:adc_pin=Pin(25)
adc_pin=Pin(26)    # Not all pins can be Analog inputs, I believe
adc=ADC(adc_pin)

while True:
    #Sending DATA
    for duty in range(0,65536,1000): #Defining the range of the duty cycle
        #DAK:PWM.duty_u16(duty) #Defining the duty cycle in the range 0 to 65536 with 1000 as frequency
        pwm.duty_u16(duty) # Defining the duty cycle in the range 0 to 65536 with 1000 as frequency ... need to use the instantiated object from the library

        uart.write(f'{duty}\n') #Sending the duty cycle value through my serial communication link
        print(f'Value sent:{duty}')
        time.sleep(4) #After sending the message wait for 4 second for any reply

        #Receiving DATA
        if uart.any(): #Checking if any data is available 
            data=uart.read() #Store the data in a variabale called data
            #DAK:print('Here is the value received:, {data}')
            print(f'Here is the value received:, {data}')   # Fixed the error in the format string (missing 'f')
            time.sleep(4) #After receiving the message wait for 4 second for the new signal
        else:
            print('I didn\'t received any value yet!!')
    
    #Reading DATA
    if uart.any(): #Checking if any data is available 
        data=uart.read() #Store the data in a variabale called data
        print('Received:', data)
        adc_value = adc.read_u16()
        uart.write(f'{adc_value}\n') #Read the value of the PWM signal
        print(f'Sent ADC value:{adc_value}')
        time_sleep(4) #Wait for 4 seconds before sending another PWM signal
    else:
        print('No value yet!!')




