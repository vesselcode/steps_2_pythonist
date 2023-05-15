
# input variable
a = int (input("input value for a: "))
b = int (input("input value for b: "))

#  operator penjumlahan
c = a + b
print ("result %d + %d = %d" % (a,b,c))

# Operator Pengurangan
c = a - b
print ("result %d - %d = %d" % (a,b,c))

# Operator Perkalian
c = a * b
print ("result %d * %d = %d" % (a,b,c))

# Operator Pembagian
c = a / b
print ("result %d / %d = %d" % (a,b,c))

# Operator Sisa Bagi
c = a % b
print ("result %d %% %d = %d" % (a,b,c))

# Operator Pangkat
c = a ** b
print ("result %d ** %d = %d" % (a,b,c))

print('----------assingment------------')


print('a = %d' %a)

# try add a with assingment
a += 5

# after a add by 5, look the result
print ("Value a after adding a += 5")
print ("a = %d" % a)
print('a -= 3    # add by 2\n'
      'a *= 10   # multiply by 3\n'
      'a /= 4    # divide by 4\n'
      'a **= 3   # exponent 3')
print('alternative operator aritmatic')
# add by 2
a += 2
print ("a = %d" % a)
# reduce by 3
a -= 3
print ("a = %d" % a)

# multiply by 3
a *= 3
print ("a = %d" % a)
# divide by 4
a /= 4
print ("a = %d" % a)
# exponent 3
a **= 3
print ("a = %d" % a)

# how value a now?

print ("after multi operation, now value a is %d" % a)

print()
print('--------compare------')
#a = int(input("input value for a: "))
#b = int(input("input value for b: "))

#  a same b?
c = a == b
print ("is %d == %d: %r" % (a,b,c))

#   a < b?
c = a < b
print ("is %d < %d: %r" % (a,b,c))

#   a > b?
c = a > b
print ("is %d > %d: %r" % (a,b,c))

#   a <= b?
c = a <= b
print ("is %d <= %d: %r" % (a,b,c))

#   a >= b?
c = a >= b
print ("is %d >= %d: %r" % (a,b,c))

#   a != b?
c = a != b
print ("is %d != %d: %r" % (a,b,c))

print()
print('----------logical----------')
a = True
b = False

#  AND
c = a and b
print ("%r and %r = %r" % (a,b,c))

#  OR
c = a or b
print ("%r or %r = %r" % (a,b,c))

#  Not
c = not a
print ("not %r  = %r" % (a,c))