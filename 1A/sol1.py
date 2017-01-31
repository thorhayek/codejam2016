import sys


def lastWord(line):
	out = "";
	for w in line:
		if(len(out) == 0):
			out = w
		else:
			out = out+w if out[0] > w else w+out
	return out
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
	ans = lastWord(line);
	if(ans and curr_line <= case_count):
		print("Case #"+str(curr_line)+": " +ans);

	curr_line += 1;