def bubble_sort(n, a):
    swap = 0
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
                
    print "Array is sorted in %d swaps." % (swap)
    print "First Element: %d" % (a[0])
    print "Last Element: %d" % (a[n - 1])
        
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

bubble_sort(n, a)
