__author__ = 'Alien'
'''
1. Dynamically typed variables and printing in python
'''
a = 10000
b = 3.4
c = "Hello world!"
d = True
e = 1000
f = 100
g = 10
h = 16368.27521
print a, b, c, d, e, f, g, h
print format(a, "4d")
print format(e, "4d")
print format(f, "4d")
print format(g, "4d")
print format(h, "0.3f")
print "%3d %0.2f" % (f, h)
print format(f,"3d"),format(h,"0.2f")
print a + h

'''
2. Conditionals
'''
print "First conditional example"
if a < h:
    print "Result: a < h"
else:
    print "Result: a>=h"

print "Second conditional example"
if a < h:
    pass
else:
    print "Result: a>=h"

str = "Summer sun"
if "sun" in str:
    print "Yes!"

if (a == 10000) and (f == 100):
    print "a =", a, "f =", f

if (a == 9999) or (f == 100):
    print "a =", a, "f =", f

#To handle multiple-test cases, use the elif statement, like this:
month = "January"
days = 0
if month == ("April" or "June" or "September" or "November"):
     days = 30
elif month == "February":
     days = 28
else:
     days = 31
print days

'''
3. File Input and Output
'''
f = open("readme.txt")           # Returns a file object
line = f.readline()              # Invokes readline() method on file
while line:
      print line,                # trailing ',' omits newline character
      line = f.readline()
f.close()
print "\n*********************************************************************************************************"
#Python provides a dedicated statement, for , that is used to iterate over items.
for line in open("readme.txt"):
    print line,

#To make the output of a program go to a file, you can supply a file to the  print statement using >>
f = open("out.txt","w")     # Open file for writing
i = 0
while i <= 100:
      print >>f,"%3d %0.2f" % (i, i*1.4532)
      i += 1
f.close()

print "\n*********************************************************************************************************"
print "\n***Working with command line***"
import sys
sys.stdout.write("Enter your name:")
name = sys.stdin.readline()
print "Your name is: ", name

'''
4. Strings
'''
a = "Hello World"
b = 'Python is groovy'
c = """Computer says 'No'"""
print a
print b
print c

print '''Content-type: text/html
<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.
'''

a = "This is a string."
b = a[6]
print a[0], a[2], b
c = a[:5]
d = a[6:]
e = a[8:14]
print c
print d
print e

#Strings are concatenated with the plus (+) operator:
a = "This"
b = "is"
с = "a"
d = "string"