import string
from operator import itemgetter


def getComb(j, p, s, k):
	#print("#####")
	d = {} 
	lol = []
	for ij in range(1,j+1):
		for ip in range(1,p+1):
			for iss in range(1,s+1):
				tmp = [] 
				a = str(ij)
				b = str(ip)
				c = str(iss)
				tmp.append(a)
				tmp.append(b)
				tmp.append(c)
				#print("#####")
				#print(tmp)
				# check if this is a valid list 
				if(("1",a,b) in d):
					#print("k="+str(k)+"da,b="+str(d[(a,b)]))
					if(k <= d[("1",a,b)]):
						#print(tmp)
						continue
				else:
					d[("1",a,b)] = 0
				if(("2",a,c) in d):
					if(k <= d[("2",a,c)]):
						#print(tmp)
						continue
				else:
					d[("2",a,c)] = 0
				if(("3",b,c) in d):
					if(k <= d[("3",b,c)]):
						#print(tmp)
						continue
				else:
					d[("3",b,c)] = 0
				d[("1",a,b)] += 1
				d[("2",a,c)] += 1
				d[("3",b,c)] += 1
				lol.append(tmp)
	return len(lol),lol
	
# read input file 
input_file = "small.txt"; # update
#output_file = "output.txt";
fi = open(input_file,'r');
#fo = open(output_file, 'w');

case_count = int(fi.readline());
#print("case_count="+str(case_count));
#cases = fi.read();s
curr_line = 1;
#cmn_lst = list(string.ascii_uppercase)
for line in fi:
	line = line.strip();
	j,p,s,k = line.split();
	num,ans = getComb(int(j), int(p), int(s), int(k))
	if(curr_line <= case_count):
		print("Case #"+str(curr_line)+": " + str(num));
		for l in ans:
			print(' '.join(l));

	curr_line += 1;