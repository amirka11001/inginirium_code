import numpy

'''massiv = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])

massivX2 = numpy.repeat(massiv, 5).reshape(massiv.shape[0], massiv.shape[1], -1)
massivstack = numpy.stack((massiv, massiv))

print(massiv)
print(massivX2)
print(massivstack)

a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = numpy.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

c = a + b
d = a - b
e = a / b
f = a * b

print(c, '+', '\n', '\n', d, '-', '\n', '\n', e, '/', '\n', '\n', f, '*')'''

a = numpy.array([[ 2, -1, 3 ],
                 [ 4,  2, 0 ],
                 [-1,  1, 1 ]])
b = numpy.array([[ 1 ],
                 [ 2 ],
                [ -1 ]])

print(a[0,0] * b[0,0] + a[0,1] * b[1,0] + a[0,2] * b[2,0], '\n', a[1,0] * b[0,0] + a[1,1] * b[1,0] + a[1,2] * b[2,0], '\n', a[2,0] * b[0,0] + a[2,1] * b[1,0] + a[2,2] * b[2,0])
