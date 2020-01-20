#!D:\Python27
def fib(n):
	"""return a list of Fibonacci series
	
	A list of Fibonacci series.
	"""
	a,b=0,1
	rs=[];
	while a<n:
		rs.append(a)
		a,b=b,a+b
	return rs

print fib(100);

def readbooks(**books):
	for bkName in sorted(books.keys()):
		print bkName,books[bkName]

readbooks(h="hadoop",b="bigdata")

args=[4,10]
print range(*args);

mybooks={"name":"bigdata","price":20,"publisher":"electric publisher"}
readbooks(**mybooks)

inc=lambda x:x*x
print inc(20)

l=[23,45,35]
l.append(55)
print l
print l.pop()
print l

from collections import deque
q=deque(["hadoop","bigdata","ddd","python"])
print q
q.append("sqlserver")
print q
print q.popleft()
print q

def func(x):
	"""numbers devidable by 7:	"""
	return x%7==0;
print func.__doc__
print filter(func,range(0,100))

def cube(x):
	"""get the cube of a number	"""
	return x**3
print cube.__doc__
print map(cube,range(0,50))

def add(x,y):
	"""add 2 numbers"""
	return x+y
print add.__doc__
print map(add,range(0,20),range(20,40))
print reduce(add,range(0,100))

def sum1(seq):
	"""get the sum of a seq"""
	return reduce(add,seq,0)
print sum1.__doc__
print sum1(range(100))
print sum1([])
print sum.__doc__
print sum(range(100))
print sum([])

print [x**2 for x in range(30)]

print [(x,y) for x in [2,5,8] for y in [1,5,7] if x!=y]

from math import pi
print [str(round(pi,x)) for x in range(10)]

matrix=[
[1,3,6],
[3,1,8],
[4,2,5]
]
print matrix
print [ [ row[c] for row in matrix] for c in range(3)]
print zip(*matrix)

t="windows","linux","mac os"
u=t,("aaa","bbb","ccc")
print t
print u

p="onlyone","another","one more"
print p
a,b,c=p
print a
print b
print c
print "hello,world"
print "Deal with issue 1"
print "Deal with issue 3"






