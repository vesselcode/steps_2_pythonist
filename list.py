car = ['BMW', 'TOYOTA', 'SUZUKI', 'FORD', 'MAZDA']
print(car)
i = 0
for c in car:
    print('index list',i,c)
    i =1+i
print(car[2:5],'------->car[2:5]')
print()
car.append('FERARI')
car.append('TESLA')
print('NEW BRAND:', car)

car[4:]=['VOLVO','KIA'] #remove and replace list index 4 upwith new items
#car[2:5]=['VOLVO','KIA']
print(car,'------->remove and replace list index 4 upwith new items')
car.remove(car[0])
print(car,' ------->remove[0] ')

print()
MIX=[2,4,9, 'LEMON','MANGO']
print('Mix item list :',MIX)
print(MIX[2]-MIX[0], '                  ----------->operation integer')
print(2*MIX[4].split(), ' ------->this operation multiply string') #add separator with spacing

#list in list
print()
print('list in list ')
DMIX=[car,MIX]
print(DMIX)
print('DMIX[0] =',DMIX[0])