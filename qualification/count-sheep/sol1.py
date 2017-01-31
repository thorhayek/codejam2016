import sys

def printDict(input_dict):
	input_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 };
	for key,val in input_dict.items():
		print(str(key)+":"+str(val), end=" ");

def sleepNumber(inp):

	if(type(inp) is not int):
		return None;
	digitTracker = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 };

	if(inp == 0):
		return "INSOMNIA";

	for i in range(1,100000):
		curr_num = i*inp;
		#print("current input"+str(curr_num));
		digit_list = get_digits(curr_num);
		if( (type(digit_list) is list) and len(digit_list) > 0):
			mark_digits(digit_list, digitTracker);
			#printDict(digitTracker);
			if(check_markers(digitTracker)):
				return curr_num;
	return "INSOMNIA";

def get_digits(curr_num):
	digit_lst = [];
	while(curr_num > 0):
		digit = curr_num % 10;
		digit_lst.append(digit);
		curr_num = curr_num // 10;
	return digit_lst;

def mark_digits(digit_list, digitTracker):
	for num in digit_list:
		if(digitTracker[num] == 0):
			digitTracker[num] = 1;

def check_markers(digitTracker):
	sumVal = 0 ;
	#printDict(digitTracker);
	for key,val in digitTracker.items():
		sumVal += val;
	if(sumVal == 10):
		return True;
	return False;

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
	#print("case="+line);
	ans = sleepNumber(int(line));
	if(ans and curr_line <= case_count):
		print("Case #"+str(curr_line)+": " +str(ans));

	curr_line += 1;