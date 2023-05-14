A = 8
B = 4
D = A+B
print('D = ',D)

print()
A = "I like programming"
B = "with Python"
print(D)
D = A+ " "+B
print(D)
print("sum characters : ",len(D))

n = sum(range(2,4))
while n:
    print(n, end = ' ')
    n = n - 1
    break
else:
    print('End', end = ' ')
print()
print('I can\'t come today')    #\'    for single quotes
print("please don't call me")   # for double quotes
print()
line= '1.First line.\n2.Second line.' # \n for make new line
print(line)

# print multi line
print("""------------
    option :
    r : read only       x  : delete
    w : write           x* : delete all
    p : print
    h : help

""")

#multiply string
A = "I"
B ='love-'
C = "you"
print(A, 3*B,C)
