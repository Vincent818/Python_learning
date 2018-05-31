# -*- coding: utf-8 -*-

names = ['Michael','Bob','Tracy']
score = [95,75,86]

d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])

d['Adam']=67
print(d['Adam'])

print(d)

if 'Thomas'in d:
    print('Yes')
else:
    print('No')

d.get('Thomas',-1)

d.pop('Bob')
print(d)

i = [1,2,3,2,7,1,2]
f = set(i)
print(f)

f.add(3)
print(f)

f.add(8)
print(f)

f.remove(1)
print(f)