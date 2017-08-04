def ransom_note(magazine, ransom):
    table = {}
    for w in magazine:
        if w not in table:
            table[w] = 1
        else:
            table[w] += 1
    for w in ransom:
        if w in table:
            table[w] -= 1
            if table[w] < 0:
                return False
        else:
            return False

    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
