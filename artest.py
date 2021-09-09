#import serial
#import time
#arduino = serial.Serial(port='/dev/cu.usbmodem145201', baudrate=115200, timeout=.1) #/dev/cu.usbmodem144101


import pyfirmata
import time
from midread import midiObj

board = pyfirmata.Arduino('/dev/cu.usbmodem144201')

midiFile = midiObj('test3.mid')
num = 0.6

midi_items = midiFile.DataLength()
while True:
    counter = 0
    print("Start")
    while counter < midi_items:
        current_note_val = midiFile.ReadData(counter)
        if current_note_val[2] > 0:
            sleep_time = current_note_val[2]/96
            time.sleep(sleep_time)
        if current_note_val[0] == 1:
            board.digital[5].write(1)
        else:
            board.digital[5].write(0)
        counter += 1
    
