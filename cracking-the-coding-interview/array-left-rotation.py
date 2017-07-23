def array_left_rotation(a, n, k):
    k = k % n
    reverse(a, 0, n - 1)
    reverse(a, 0, n - 1 - k)
    reverse(a, n - k, n - 1)
    return a

def reverse(l, s, e):
    while s < e:
        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
