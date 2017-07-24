def is_matched(expression):
    openers = "{[("
    closers = "}])"
    match = {"{":"}", "[":"]", "(":")"}
    stack = []
    for c in expression:
        if c in openers:
            stack.append(c)
        elif c in closers:
            if len(stack) == 0:
                return False
            else:
                o = stack.pop()
                if match[o] != c:
                    return False
    # the stack must be empty if it's a balanced bracket
    return len(stack) == 0

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"