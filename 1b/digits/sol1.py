import sys


def getPhone(line):
	out = []
	store = dict()
	for w in line:
		#read each letter in a line
		#print(w) 
		if w in store:
			store[w] += 1
		else:
			store[w] = 1

	while ( check(store)):
		#print(out)
		#check for zero till dict count == 0
		if( 'Z' in store): # 0
			for i in range(store['Z']):
				out.append('0')
				store['E'] -= 1
				store['R'] -= 1
				store['O'] -= 1
			store['Z'] = 0
		if( 'W' in store): # 2
			for i in range(store['W']):
				out.append('2')
				store['T'] -= 1
				store['O'] -= 1
			store['W'] = 0
		if( 'U' in store):  # 4 
			for i in range(store['U']):
				out.append('4')
				store['F'] -= 1
				store['O'] -= 1
				store['R'] -= 1
			store['U'] = 0
		if( 'X' in store):  # 6 
			for i in range(store['X']):
				out.append('6')
				store['S'] -= 1
				store['I'] -= 1
			store['X'] = 0	
		if( 'G' in store):  #8
			for i in range(store['G']):
				out.append('8')
				store['E'] -= 1
				store['I'] -= 1
				store['H'] -= 1
				store['T'] -= 1
			store['G'] = 0
		# rest by elimintaion
		if( 'O' in store):  #1
			for i in range(store['O']):
				out.append('1')
				store['E'] -= 1
				store['N'] -= 1
			store['O'] = 0
		if( 'T' in store):  #3
			for i in range(store['T']):
				out.append('3')
				store['E'] -= 2
				store['H'] -= 1
				store['R'] -= 1
			store['T'] = 0
		if( 'S' in store):  #7
			for i in range(store['S']):
				out.append('7')
				store['E'] -= 2
				store['N'] -= 1
				store['V'] -= 1
			store['S'] = 0
		if( 'V' in store):  #5
			for i in range(store['V']):
				out.append('5')
				store['E'] -= 1
				store['F'] -= 1
				store['I'] -= 1
			store['V'] = 0
		if( 'I' in store):  #9
			for i in range(store['I']):
				out.append('9')
				store['E'] -= 1
				store['N'] -= 2
			store['I'] = 0
	return out

def check(store):
	for k in store:
		#print("k = " + k)
		if store[k] > 0:
			#print("k = " + k)
			#print(store[k])
			return True
	return False


# read input file 
input_file = "large.txt"; # update
#output_file = "output.txt";
fi = open(input_file,'r');
#fo = open(output_file, 'w');

case_count = int(fi.readline());
#print("case_count="+str(case_count));
#cases = fi.read();
curr_line = 1;
for line in fi:
	ans = getPhone(line.strip());
	ans = sorted(ans, key=int) 
	if(ans and curr_line <= case_count):
		print("Case #"+str(curr_line)+": " +''.join(ans));

	curr_line += 1;