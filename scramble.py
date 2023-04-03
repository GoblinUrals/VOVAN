def scramble(s1, s2):
    if s2!="" and s1!="":
        return True if len([x for x in s2 if x in s1])==len(s2) else False
    else:
        return False

s1 = "ovhvjvpteqpdpmuf"
s2 = "fequjdpvmjth"
# True should equal False


print(scramble(s1,s2))

def func(txt: str):
    while '#' in txt:
        inx = txt.index('#')
        if inx == 0:
            txt = txt[1:]
        else:
            txt = txt[:inx-1]+txt[inx+1:]
    return txt


for txt in ['major# spar##ks','he##l#hel#llo','si###tboy']:
    print(func(txt))

a = ['one','two','three','four']

first,*_,last = a
print(first)
print(_)
print(last)

# one
# ['two', 'three']
# four