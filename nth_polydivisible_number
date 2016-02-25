def is_polydivisible(s, b):
    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    s_lego = ''
    used = [1]
    for x in list(str(s)):
        s_lego += x
        for a in xrange(used[-1], b+b):
            used.append(int(CHARS[a])+1)
            print s_lego
            print 'lego'
            print len(s_lego)
            print 'len'
            if s_lego == b:
                print True
            elif to_base10(s_lego, b) % len(s_lego) != 0:
                return False
            else:
                break
    return True

def run_up(n, b):
    num = b
    count = b
    while count < n:
        if is_polydivisible((toStr(num, b)), b):
            print count
            print 'count'
            print toStr(num, b)
            print num
            print 'num'
            print '========'
            count += 1
            if count == n:
                break
            else:
                num += 1
        else:
            num += 1
    return toStr(num, b)

def toStr(n,base):
    convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

def to_base10(n,base):
    conStr = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    n = [x for x in n]
    total = 0
    for a in range(len(n)-1):
        power = len(n)- 1 - a
        total += ((conStr.index(n[a])) * (base**power))
    total += conStr.index(n[-1])
    return total
    
"""
run_up() has two input variables (x, y), where x is the nth polydivisible number, 
and y is the number base the answer should be returned in.
"""

print run_up(50, 5)
