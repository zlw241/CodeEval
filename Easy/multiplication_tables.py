

def mult_table(n):
    for i in range(1,n+1):
        line = ['%2s' % i]+['%4s' % (i*x) for x in range(2,n+1)]
        print(''.join(line))


mult_table(12)