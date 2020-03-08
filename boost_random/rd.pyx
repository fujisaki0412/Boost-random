from libc.stdlib cimport rand
from math import ceil as _ceil, log as _log
def choice(list seq):
    return seq[rand() % len(seq)]
def sample(list a, int k):
    cdef list result = [None] * k
    cdef:
        int n = len(a)
        int setsize = 21
    if k > 5:
        setsize += 4 ** _ceil(_log(k * 3, 4))
    if n <= setsize:
        pool = list(a)
        for i in range(k):
            j = rand() % n-1
            result[i] = pool[j]
            pool[j] = pool[n-i-1]
    else:
        sele = set()
        sele_add = sele.add
        for i in range(k):
            j = rand() % n
            while j in sele:
                j = rand() % n
            sele_add(j)
            result[i] = a[j]
    return result
def shuffle(list x, random=None):
    cdef int i
    for i in reversed(range(1, len(x))):
        j = rand() % i+1
        x[i], x[j] = x[j], x[i]
