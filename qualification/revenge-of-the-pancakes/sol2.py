import sys

def printDict(input_dict):
	input_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 };
	for key,val in input_dict.items():
		print(str(key)+":"+str(val), end=" ");

def flipCount(inp):

	if(type(inp) is not str):
		return None;
	inp_lst = list(inp);
	flip_count = 0 ;
	i = 0;

	while i < len(inp_lst):
		incr = False;
		if(inp_lst[i] == '-'):
			while i < len(inp_lst) and inp_lst[i] == '-':
				inp_lst[i] = "+";
				i += 1;
				incr = True;
			flip_count += 1;
		elif(i < len(inp_lst) and inp_lst[i] == '+'):
			flip_both = False;
			while i < len(inp_lst) and inp_lst[i] == '+':
				i += 1;
				incr = True;
			while i < len(inp_lst) and inp_lst[i] == '-' :
				inp_lst[i] = "+";
				i += 1;
				incr = True;
				if(not flip_both):
					flip_both = True;
			if(flip_both):
				flip_count += 2;
		if(not incr):
			i+=1;
	return flip_count;

# read input file 
input_file = "large2.txt"; # update
#output_file = "output.txt";

fi = open(input_file,'r');
#fo = open(output_file, 'w');

case_count = int(fi.readline());
#print("case_count="+str(case_count));
#cases = fi.read();
curr_line = 1;
for line in fi:
	#print("case="+line);
	ans = flipCount(line);
	if(ans != None and curr_line <= case_count):
		print("Case #"+str(curr_line)+": " +str(ans));

	curr_line += 1;