from libc.stdlib cimport rand
cpdef choice(list a):
    return a[rand() % len(a)]
cpdef sample(list a, int count):
    cdef list result = [None] * count
    cdef int n = len(a)
    sele = set()
    sele_add = sele.add
    for i in range(count):
        j = rand() % n
        while j in sele:
            j = rand() % n
        sele_add(j)
        result[i] = a[j]
    return result
