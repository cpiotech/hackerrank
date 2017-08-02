def number_needed(a, b):
    arr = [0] * 26
    for c in a:
        index = ord(c) - ord('a')
        arr[index] += 1
    for c in b:
        index = ord(c) - ord('a')
        arr[index] -= 1
    res = 0
    for i in arr:
        res += abs(i)
    return res

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
