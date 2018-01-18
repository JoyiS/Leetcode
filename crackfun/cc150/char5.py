
def floatToBinary(num):
    intpart = int(num[:num.index('.')])
    decpart = float(num[num.index('.'):]) # need to be very careful
    int_string = ''
    while intpart>0:
        r = intpart%2
        print(str(intpart))
        intpart>>=1
        print('after right shift : ' + str(intpart))
        int_string = str(r)+int_string
    dec_string = ''
    while decpart>0:
        if decpart == 1:
            dec_string = dec_string + '1'
            break
        r = decpart*2
        if r>=1:
            dec_string = dec_string + '1'
            decpart = r - 1
        else:
            dec_string = dec_string + '0'
            decpart=r
    print(int_string + '.' + dec_string)

def diff(a,b):
    c = a^b
    count =0
    while c>0:
        if c ==1:
            count +=1
            break
        count = count+c%2
        c= c>>1
    return count
