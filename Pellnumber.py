def pellNumber(i):
    
    if i <= 1:
        return i
    
    p0, p1 = 0, 1

    for j in range(2, i + 1):
        current = 2 * p1 + p0
        p0, p1 = p1, current 

    return p1

if __name__ == '__main__':
   i = int(input()) 
   print("Pell number {} is {}.\n".format(i ,pellNumber( i )))

