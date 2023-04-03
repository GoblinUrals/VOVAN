def erase(txt: str):
    while '#' in txt:
        idx = txt.index('#')
        if idx == 0:
            txt = txt[1:]
        else:
            txt = txt[:idx-1] + txt[idx+1:]
    return txt

for i in ['he##l#hel#llo','major#spar##ks','si###tboy']:
    print(erase(i), end=' ')

# hello majospks tboy

