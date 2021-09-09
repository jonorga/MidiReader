import struct

f = open('test.mid', 'rb')
read_data = f.read()
print('Raw data Ableton:\n', read_data)



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
header_id1 = read_data[0:4]
header_leng1 = read_data[5:8]
header_format = read_data[9:10]
header_n = read_data[11:12]
header_div = read_data[13:14]


# Chunk 2 read
header_id2 = read_data[14:18]
header_leng2 = read_data[19:22]



# Chunk 1 decode
header_id1 = header_id1.decode('ascii')
header_leng1_dc = int.from_bytes(header_leng1, byteorder='big')
header_format_dc = int.from_bytes(header_format, byteorder='big')
header_n_dc = int.from_bytes(header_n, byteorder='big')
header_div_dc = int.from_bytes(header_div, byteorder='big')


# Chunk 2 decode
header_id2 = header_id2.decode('ascii')
header_leng2_dc = int.from_bytes(header_leng2, byteorder='big')



# Chunk 1 Print
print('Header 1 ID: ', header_id1)
print('Header 1 Length: ', header_leng1_dc)
print('Header 1 format: ', header_format_dc)
print('Chunks to follow: ', header_n_dc)
print('Division: ', header_div_dc)


# Chunk 2 Print
print('Header 2 ID: ', header_id2)
print('Header 2 Length: ', header_leng2_dc, '\n')


def ValueToNote(note_num):
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

i = 0
pt = ""
while i < len(read_data):
	pt = read_data[i]

	if pt == 128:
		print('Note ', ValueToNote(read_data[i+1]),' off, velocity ', read_data[i+2], ', ', read_data[i-1], ' ticks from last event')
	if pt == 144:
		print('Note ', ValueToNote(read_data[i+1]),' on, velocity ', read_data[i+2], ', ', read_data[i-1], ' ticks from last event')

	i += 1
