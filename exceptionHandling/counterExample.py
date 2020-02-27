#counterExample.py
from collections import Counter
with open('Basics') as f:
	s=f.read()
	print("Number of words",Counter(s.split()))
	