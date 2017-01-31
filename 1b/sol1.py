import sys


def getMax(cases):

	#print(cases)
	lstore = {}
	rstore = {}
	count = 0
	cc = 0 
	for line in cases:
		l,r = line.split()
		if(l not in lstore):
			lstore[l] = 1
		else:
			lstore[l] += 1
		if(r not in rstore):
			rstore[r] = 1
		else:
			rstore[r] +=1 

	for i in range(len(cases)):
		#print(cases[i])
		l,r = cases[i].split()
		a = lstore[l] -1
		b = rstore[r] -1
		if(min(a,b) > 0 ):
			count += 1
			lstore[l] -= 1
			rstore[r] -= 1
		#print("x"+str(count))
	return count


# read input file 
input_file = "input.txt"; # update
#output_file = "output.txt";
fi = open(input_file,'r');
#fo = open(output_file, 'w');

case_count = int(fi.readline());
#print("case_count="+str(case_count));
#cases = fi.read();
curr_line = 1;
sub_case = 0
cases = []
ans = [] 
for line in fi:
	sub_case = int(line.strip())
	cases = []
	for i in range(sub_case):
		cases.append(fi.readline().strip())	
	ans.append(getMax(cases));
#print(ans);
for a in ans:
	print("Case #"+str(curr_line)+": " +str(a));
	curr_line += 1;