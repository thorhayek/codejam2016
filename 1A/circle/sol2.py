import sys


def circle(kids, bff_lst):
	bff = {}
	rev_bff = {}
	out = []
	for i in range(1,kids+1):
		val = bff_lst[i-1]
		bff[i] = val
		if val in rev_bff:
			rev_bff[val].append(i)
		else:
			rev_bff[val] = [i]

	curr = 1
	out.append(curr)
	while True:
		val = bff[curr]
		if val not in out:
			out.append(val)
		else:
			new_val = rev_bff[val]
			for x in new_val:
				if x not in out:
					out.append(x)
					return len(out)
					
		curr = val
		if(curr in out):
			return len(out)

# read input file 
input_file = "input.txt"; # update
#output_file = "output.txt";

fi = open(input_file,'r');
#fo = open(output_file, 'w');

case_count = int(fi.readline())

#print("case_count="+str(case_count));
#cases = fi.read();
curr_line = 1;
grid_size = 2

for line in fi:
	
	ans = []
	inp_lst = [];
	#line = fi.readline()
	kids = int(line.strip())
	line2 = fi.readline()
	lst = line2.strip().split()
	ans = circle(kids, lst)
	if(ans and curr_line <= case_count):
		print("Case #"+str(curr_line)+": "+str(ans))
		#print();
	curr_line += 1

	