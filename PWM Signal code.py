import machine
from machine import UART, Pin, PWM, ADC
import time

#Initialisattion the UART serial communication protocols
uart = UART(1, baurate=9600, tx=Pin(8), rx=(9))
uart.init(bits=8, parity=None, stop=1)

#Initialisation of the PWM Pin
pwm_pin=Pin(15)
pwm=PWM(pwm_pin)

#Set up the frequence at 1000Hz
pwm.freq(1000) 

#Initialisation of the ADC Pin
adc_pin=Pin(25)
adc=ADC(adc_pin)

while True:
    #Sending DATA
    for duty in range(0,65536,1000): #Defining the range of the duty cycle
        PWM.duty_u16(duty) #Defining the duty cycle in the range 0 to 65536 with 1000 as frequency
        uart.write(f'{duty}\n') #Sending the duty cycle value through my serial communication link
        print(f'Value sent:{duty}')
        time.sleep(4) #After sending the message wait for 4 second for any reply

        #Receiving DATA
        if uart.any(): #Checking if any data is available 
            data=uart.read() #Store the data in a variabale called data
            print('Here is the value received:, {data}')
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




