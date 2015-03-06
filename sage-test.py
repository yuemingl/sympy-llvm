import time

x = var('x')
y = var('y')

#f=2.0*x**5 + 3.0*x**4 + 5.0*x**3 + 4.5*x**2 + 5.6*x + x*y + 2.0*y**5 + 3.0*y**4 + 5.0*y**3 + 4.5*y**2 + 5.6*y + x*y
#f=1.0 * x**9.1 + 2.0 * x**8.1 + 3.0 * x**7.1 + 4.0 * x**6.1 + 5.0 * x**5.1 + 6.0 * x**4.1 + 7.0 * x**3.1 + 8.0 * x**2.1 + 9.0 * x**1.1 + 3.0 * x * y
f=1.0 * x**9 + 2.0 * x**8 + 3.0 * x**7 + 4.0 * x**6 + 5.0 * x**5 + 6.0 * x**4 + 7.0 * x**3 + 8.0 * x**2 + 9.0 * x**1 + 3.0 * x * y
#f=f.diff(x)
print f
print f(x=2,y=3)
ts = time.time()
g = fast_float(f, x,y)
te = time.time()
print "compile: ",(te-ts)

print g.op_list()
print g(2,3)

N=10000000
ts = time.time()
for i in range(N):
	g(2, 3)
te = time.time()
print (te-ts)
