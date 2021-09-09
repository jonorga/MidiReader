import struct


class midiObj:
	def __init__(self, mid_file):
		# Read file
		f = open(mid_file, 'rb')
		self.raw_midi_data = f.read()
		debuggin = True

		# Uncomment below line to read all raw data
		# print('Raw data:\n', raw_midi_data)


		# Chunk 1 variables
		header_id1 = chr(4)
		header_leng1 = bytes(4)
		header_format = bytes(2)
		header_n = bytes(2)
		header_div = bytes(2)


		# Chunk 2 variables
		header_id2 = chr(4)
		header_leng2 = bytes(4)



		# Chunk 1 read
		header_id1 = self.raw_midi_data[0:4]
		header_leng1 = self.raw_midi_data[5:8]
		header_format = self.raw_midi_data[9:10]
		header_n = self.raw_midi_data[11:12]
		header_div = self.raw_midi_data[13:14]


		# Chunk 2 read
		header_id2 = self.raw_midi_data[14:18]
		header_leng2 = self.raw_midi_data[19:22]



		# Chunk 1 decode
		self.header_id1 = header_id1.decode('ascii')
		self.header_leng1_dc = int.from_bytes(header_leng1, byteorder='big')
		self.header_format_dc = int.from_bytes(header_format, byteorder='big')
		self.header_n_dc = int.from_bytes(header_n, byteorder='big')
		self.header_div_dc = int.from_bytes(header_div, byteorder='big')


		# Chunk 2 decode
		self.header_id2 = header_id2.decode('ascii')
		self.header_leng2_dc = int.from_bytes(header_leng2, byteorder='big')


		# Read all data into arrays
		self.played_notes = []
		self.played_notes_bin = []


		self.notes = []

		i = 0
		prev = ""
		pt = ""
		first_note = True
		while i < len(self.raw_midi_data):
			prev = pt
			pt = self.raw_midi_data[i]
			print(pt)
			if pt == 128:
				if self.raw_midi_data[i-4] == 128 or self.raw_midi_data[i-4] == 144:
					prev = self.raw_midi_data[i-1]
				else:
					if first_note:
						prev = self.raw_midi_data[i-1]
					else:
						prev = ((self.raw_midi_data[i-2] - 128) * 128) + self.raw_midi_data[i-1]
				print("Off ===================")
				first_note = False
				self.notes.append([0, self.raw_midi_data[i+1], prev])
				if debuggin:
					print('Note ', self.ValueToNote(self.raw_midi_data[i+1]),' off, velocity ', self.raw_midi_data[i+2], ', ', prev, ' ticks from last event')
			if pt == 144:
				if self.raw_midi_data[i-4] == 128 or self.raw_midi_data[i-4] == 144:
					prev = self.raw_midi_data[i-1]
				else:
					if first_note:
						prev = self.raw_midi_data[i-1]
					else:
						prev = ((self.raw_midi_data[i-2] - 128) * 128) + self.raw_midi_data[i-1]
				print("On ===================")
				first_note = False
				self.notes.append([1, self.raw_midi_data[i+1], prev])
				self.played_notes.append(self.ValueToNote(self.raw_midi_data[i+1]))
				self.played_notes_bin.append(self.raw_midi_data[i+1])
				if debuggin:
					print('Note ', self.ValueToNote(self.raw_midi_data[i+1]),' on, velocity ', self.raw_midi_data[i+2], ', ', prev, ' ticks from last event')
			i += 1

		self.total_notes = len(self.played_notes)


	def PrintRawHeaders(self):
		# Chunk 1 Print
		print('Header 1 ID: ', self.header_id1)
		print('Header 1 Length: ', self.header_leng1_dc)
		print('Header 1 format: ', self.header_format_dc)
		print('Chunks to follow: ', self.header_n_dc)
		print('Division: ', self.header_div_dc)


		# Chunk 2 Print
		print('Header 2 ID: ', self.header_id2)
		print('Header 2 Length: ', self.header_leng2_dc, '\n')

	def ValueToNote(self, note_num):
		mod = note_num % 12
		if mod == 0:
			mod = 'C'
		if mod == 1:
			mod = 'C#'
		if mod == 2:
			mod = 'D'
		if mod == 3:
			mod = 'D#'
		if mod == 4:
			mod = 'E'
		if mod == 5:
			mod = 'F'
		if mod == 6:
			mod = 'F#'
		if mod == 7:
			mod = 'G'
		if mod == 8:
			mod = 'G#'
		if mod == 9:
			mod = 'A'
		if mod == 10:
			mod = 'A#'
		if mod == 11:
			mod = 'B'
		octi = int(note_num / 12)
		return str(mod) + str(octi)

	def GetNote(self, note_index, noteformat="notename"):
		if note_index >= self.total_notes:
			return "Invalid index"

		if noteformat == "notename":
			return self.played_notes[note_index]
		if noteformat == "bin":
			return self.played_notes_bin[note_index]


	def ReadData(self, index):
		return self.notes[index]

	def DataLength(self):
		return len(self.notes)
	
		
