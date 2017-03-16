"""
  Context Manager:
  1. open a file;
  2. class calling the __enter__()
"""

# open a file
print "Not use context manager"
f = open("new.txt","w")
print f.closed
f.write("hello world!")
f.close()
print f.closed

print "\nUse context manager"
with open("new.txt","w") as ff:
    print ff.closed
    ff.write("Hello World!")
print ff.closed


# when define a object, it will call its __init__().
# when using context manager, it will call its __enter__(), 
# after using, it will call __exit__(), too.
class vow(object):
  def __init__(self, text):
    print "$$$calling __init__()"
    self.text = text
  def __enter__(self):
    print "$$$calling __enter__()"
    self.text = 'I say, ' + self.text
    return self
  def __exit__(self, exc_type, exc_value, traceback):
    print "$$$calling __exit__()"
    self.text = self.text + ' !!'

print "\nNot use context manager"
myvow1 = vow("I'm fine")
print myvow1.text

print "\nUse context manager"
with vow("I'm fine, 2") as myvow2:
  print myvow2.text
print myvow2.text
