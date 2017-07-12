# -*- coding: UTF-8 -*-

"""
try:
    ...
except exception1:
    ...
except exception2:
    ...
except:
    ...
else:
    ...
finally:
    ...
"""
#try -> EXCEPTION       -> except   -> finally
#try -> Non-EXCEPTION   -> else     -> finally


print "\n#####Sub-function will hand over the exception to main program"
def test_func():
    try:
        m = 1/0
    except NameError:
        print "catch nameError in the sub-function"
try:
    test_func()
except ZeroDivisionError:
    print "catch error in the main program"

print "\n#####Example of Raise error"
try:
    raise StopIteration
except NameError:
    print "NameError"
except StopIteration:
    print "StopIteration Error"
