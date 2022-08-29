import subprocess
import timeit

beg = timeit.default_timer()

for i in range(1000):
    try:
        id = subprocess.call('notepad', timeout = 0)
    except:
        pass

with open('g:/time.txt', 'w') as out:
    time = timeit.default_timer() - beg
    out.write(str(time))
	