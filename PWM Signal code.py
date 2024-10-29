from machine import UART, Pin
import time

#Initialisattion the UART serial communication protocols
uart =UART(1, baurate=9600, tx=Pin(8), rx=(9))
uart.init(bits=8, parity=None stop=1)


while True:
    #Sending DATA
    uart.write('Hello world!')
    print('Message sent')
    time.sleep(4) #After sending the message wait for 4 second for any reply


    #Receiving DATA
    if uart.any():
        data=uart.read()
        print('Here is the data I received:, {data}')
        time.sleep(4) #After receiving the message wait for 4 second and then reply 
    
    else:
        print('I didn\'t received any data yet!!')
