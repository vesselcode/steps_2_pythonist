#tuple is sequence data like list
color='red','blue','yellow','pink'
say=('i','have','some','pencils')
book=(451,'Biografi','100','World Heroes')

print(color)
d=color[3]
print(d)
mine=say+color
print(mine)
print(book)
print(book[1])
print()
#unpacking tuple
code,title,person,category=book
print(code)
code = '455'
print('book = ',book)


if  color[1]==('red') :
    pass
else :
    print("can't replace item tuple")