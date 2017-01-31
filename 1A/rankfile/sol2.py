import sys


def rankFile(nums, grid_size):
	pro_dict = {}
	for n in nums:
		if(n in pro_dict):
			pro_dict[n] += 1
		else:
			pro_dict[n] = 1
	out = odd_lst(pro_dict)
	out.sort()
	#print(out)
	#print(out)
	return out

def odd_lst(d):
	out = []
	for i in d.keys():
		if( d[i]%2 > 0 ):
			out.append(int(i));
	return out

# read input file 
input_file = "large.txt"; # update
#output_file = "output.txt";

fi = open(input_file,'r');
#fo = open(output_file, 'w');

case_count = int(fi.readline())

#print("case_count="+str(case_count));
#cases = fi.read();
curr_line = 1;
for line in fi:
	grid_size = int(line)
	ans = []
	inp_lst = [];
	for ln_num in range(2*grid_size-1):
		line = fi.readline()
		nums = line.split()
		inp_lst.extend(nums)
	ans = rankFile(inp_lst, grid_size)
	if(ans and curr_line <= case_count):
		print("Case #"+str(curr_line)+": "+" ".join(str(x) for x in ans))
		#print();
	curr_line += 1

	