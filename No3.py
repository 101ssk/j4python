import random
import linecache

a = random.randint(1,1500)
line = linecache.getline('toeic1500.dat',a)
print(line)
linecache.clearcache()
