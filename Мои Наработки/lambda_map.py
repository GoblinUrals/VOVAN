# _____________________________________________________________
z = lambda x:x*0.5
print(z(4))
#2.0
print(list(map(lambda x: x.upper(),['cat','dog','cow'])))
#['CAT', 'DOG', 'COW']
# _____________________________________________________________
mag = ['1','2','5','10']
result = list(map(lambda x: int(x), mag))
print(result)
#[1,2,5,10]
# ______________________________________________________________
b = [5,3,0,-6,8,10,1]
result = filter(lambda x: x>0 and x%2==0, b)
print(result)   #<filter object at 0x01B3A0A0>
print(list(result)) #[8,10]
# ______________________________________________________________
from functools import reduce

print(reduce(lambda a,b: a*b, (50,57,89,12,100)))
#304380000
# _______________________________________________________________
a = [4,5,lambda: print('work'), 7,8]
print(a[2]())
#work
# _________________________________________________________________
num = [2,4,6,8]
lst1 = list(map(lambda x:x*2, num))
lst2 = [x*2 for x in num]
print(lst1, lst1.__sizeof__())
print(lst2, lst2.__sizeof__())
#[4, 8, 12, 16] 48
#[4, 8, 12, 16] 36
# __________________________________________________________________
from pipe import where

lst1 = [1,2,3,5,6,8,10]
lst2 = list(lst1
            |where (lambda x:x%2==0)
            |where (lambda x: x>6))
print(lst2)
# ____________________________________________________________________
def func():
    return [lambda x:x*i for i in range(5)]

print([m(2) for m in func()])

#[8,8,8,8]ju


