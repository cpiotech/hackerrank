import math
def is_prime(num):
    if num <= 1:
        return False
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    if is_prime(n) == True:
        print 'Prime'
    else:
        print 'Not prime'
