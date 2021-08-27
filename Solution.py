# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
a = input().strip()

for key,grp in groupby(a):
    print((len(list(grp)),int(key)), end = " ")
