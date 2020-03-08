import rd
import random
import time
#boost_random
b = [i for i in range(30000)]
s = time.time()
rd.shuffle(b)
e = time.time() - s
print("boost_random>>>" + str(e))

#random
s = time.time()
random.shuffle(b)
e = time.time() - s
print("random>>>"+ str(e))

