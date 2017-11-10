def remove_repeat(str):
    if len(str) < 2:
        return str
    count = 0
    for i in range(0, len(str)):
        a = str[count]
        if a in str[count+1:]:
            str = str[:count]+str[count+1:]
        else:
            count = count+1
     return str

def is_anagrams(str1, str2):
    if sorted(list(str1)) == sorted(list(str2)):
        return True
    return False

def strCompress(stra):
 countspace = 0
 for i in stra:
     if i == ' ':
         countspace +=1
 oldlen = len(stra)
 newlen = len(stra) + countspace * 2
 stra = stra + '0'*(newlen-len(stra))
 print(stra)
 for i in range(oldlen-1,-1,-1):
    if stra[i] == ' ':
        print('Yes, find space')
        stra = stra[:newlen-3]+'%20'+stra[newlen:]
        newlen = newlen-3
        print('step ' + str(oldlen - i) + ' : ' + stra)
    else:
        stra= stra[:newlen-1]+ stra[i] + stra[newlen:]
        newlen = newlen - 1
        print('step ' + str(oldlen - i) + ' : ' + stra)

    return stra






str = '12232'
str_new = remove_repeat(str)