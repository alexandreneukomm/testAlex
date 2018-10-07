coco = 10000

print(coco)


coco=( "%.2e"% coco)

print(coco)
#
# cocomax=max(coco)
# print(cocomax)


a = 1896.75694

ch = "%e" % a
print (ch)

i = ch.find('.')
j = ch.find('e')

a1 = ch[:i]
a2 = ch[i + 1:j]
a3 = ch[j + 1:]
print (a1, a2, a3)

print ("diminuer l'exposant de 1:")

b1 = a1 + a2[0]
b2 = a2[1:]
b3 = "%+02d" % (int(a3) - 1)
print (b1, b2, b3)

x = b1 + '.' + b2 + 'e' + b3
print(x)