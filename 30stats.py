# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

val = []

total = 0
for v in sys.argv[1:]:
	val.append(float(v))
	total += 1
print('Count:', total)

print('Minimum:', float(min(val)))

print('Maximum:', float(max(val)))

mean = sum(val) / len(val)
print('Mean:', f'{mean:.3f}')

sum = 0
for v in val:
	sum += (v - mean) ** 2
variance = sum / len(val)
stdev = variance ** 0.5
print('Std. dev:', f'{stdev:.3f}')

val.sort()
mid = len(val) // 2
if len(val) % 2 == 0:
	median = (val[mid] + val[mid - 1])
else:
	median = val[mid]
print('Median:', f'{median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
