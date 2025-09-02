def pan(a):
    if a%2 ==0:
        return 'evennum'
    else:
        return 'oddnum'

def ave(b):
    sum = 0
    for i in b:
        sum += int(i)
    ave = sum/len(b)
    return ave

def max(c):
    max = c[0]
    for i in c:
        if max<int(i):
            max = int(i)
    return max

def min(d):
    min = d[0]
    for i in d:
        if min>int(i):
            min = int(i)
    return min  









