def parlor_search(m, n, a):
    table = {}
    for i in range(n):
        if a[i] < m:
            if a[i] in table:
                print "%d %d" % (table[a[i]] + 1, i + 1)
            else:
                table[m - a[i]] = i
        
t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    parlor_search(m, n ,a)
