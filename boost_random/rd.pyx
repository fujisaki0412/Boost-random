from libc.stdlib cimport rand
def choice(list seq):
    return seq[rand() % len(seq)]
def sample(list a, int count):
    cdef list result = [None] * count
    cdef int n = len(a)
    sele = set()
    sele_add = sele.add
    cdef int i,j
    for i in range(count):
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
