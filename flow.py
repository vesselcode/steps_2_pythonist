#flow consider condition
x = int(input("How time is it now ..?"))
#Please enter an integer: 42
if 2<x < 5:
    print('time to bath')
elif x == 7:
    print('time to go to school')
elif x == 6:
    print('time to breakfast')
elif x > 7 and x<13 :
    print('you should study at school')
elif 24<x :
    print('you loss a day..')

else:
    print('you are free time')

# for---range [start, end,step]

print()
print('------loop for and range-----')
for i in range(2,15,3) :
    print(i)
print('-----------')
k=1
for k in range(0,15,6) :
    print(k)
print()

print('-------sorting data user active-------------')
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', 'Bejo': 'active'}
print('all users : ',users)
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print('methode 1 : ',users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print('methode 2 : ',active_users)

print('-----------------')
for n in range(2, 15):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
print()
#break loop
print('--------break loop---------')
sum = 0
for i in range(12):
    if sum > 8:
        break
    sum += i
    print(i,':',sum)

print()
print('----pass---')
#very usefull if you writing flow coding at first step use conditional statement

x=15
for i in range (x) :
    if <i<2 :
        pass
    elif i==5 :
        pass
    elif 12>i>5 :
        pass
    else :
        print(i,'some data pass')

