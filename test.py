from midread import midiObj

midiFile = midiObj('test3.mid')

print(midiFile.DataLength())
#print(midiFile.PrintRawHeaders())
loops = 1
midi_items = midiFile.DataLength()
while loops < 2:
	counter = 0
	while counter < midi_items:
		print(midiFile.ReadData(counter))
		counter += 1
	loops += 1
