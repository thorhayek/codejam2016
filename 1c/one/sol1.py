import string
from operator import itemgetter


def getOrder(nums, slist, alpha_list):
	m = []
	o = [] 
	t = 0 
	for i in range(len(slist)):
		c = int(slist[i])
		t += c
		m.append([c, alpha_list[i]])
	m.sort(key=itemgetter(0), reverse = True)
	while m[0][0] != 0:
		s = ""
		f = m[0][0]
		if(f == 1 and t%2 != 0):

			t -= 1
			m[0][0] -= 1
			s += m[0][1]


		elif(f > t/2 ):

			if(f > 1):
				m[0][0] -= 2
				t -= 2
				s += (m[0][1]+m[0][1])
			else:
				m[0][0] -= 1
				t -= 1
				s += (m[0][1])
		else:
			m[0][0] -= 1
			t -= 1
			s += m[0][1]
			if(len(m) > 1 and m[1][0] != 0):
				m[1][0] -= 1
				t -= 1
				s += m[1][1]
		o.append(s)
		m.sort(key=itemgetter(0), reverse = True)
	return o
# read input file 
input_file = "large.txt"; # update
#output_file = "output.txt";
fi = open(input_file,'r');
#fo = open(output_file, 'w');

case_count = int(fi.readline());
#print("case_count="+str(case_count));
#cases = fi.read();
curr_line = 1;
cmn_lst = list(string.ascii_uppercase)
for line in fi:
	num_sen = line.strip();
	count_lst = fi.readline().strip().split();
	ans = getOrder(num_sen, count_lst, cmn_lst)
	if(ans and curr_line <= case_count):
		print("Case #"+str(curr_line)+": " +' '.join(ans));

	curr_line += 1;