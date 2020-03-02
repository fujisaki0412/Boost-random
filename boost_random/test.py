import rd
import random
import time
#boost_random
b = [i for i in range(3000)]
s = time.time()
for i in b:
    rd.choice(b)
e = time.time() - s
print("boost_random>>>" + str(e))

#random
s = time.time()
for i in b:
    random.choice(b)
e = time.time() - s
print("random>>>"+ str(e))

