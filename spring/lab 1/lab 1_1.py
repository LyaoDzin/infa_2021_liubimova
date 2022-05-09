l = list()
numbers = input()

while numbers!='':
    l.append(int(numbers))
    numbers = input()

l.sort()
print(l)

if len(l) % 2 == 0:
    print(float(l[len(numbers)//2]))

elif len(l) % 2 == 1:
    print(float(((l[len(l)//2-1]) + (l[len(l)//2+1]))/2))

