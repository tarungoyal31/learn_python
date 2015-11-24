name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))

# Check occurence in a collection
Names = {"tarun", "goyal"}
if "tarun" in Names:
  print "tarun is present in names"

if "Tarun" in Names:
  print "Tarun is present in names"
else:
  print "Tarun is not in names"

para = """This is a Paragraph..
This continues over the lines..
"""
print para

ary = [1, "one", (i for i in range(1,10))]
print "ary is: %r, ary[2] is: %r" %(ary,ary[2])
print ary[0:2]
  
for x in ary:
  print x
for x in ary[2]:
  print x
for x in ary[2]: #generator already called do not print anything.
  print x

elements = []
for i in range(0,6):
  elements.append(i)
print elements

i = 0
while i<6:
  print i
  i += 1

x = "print 2*4"
print "Using exec",
exec x

cub = lambda x : x*x*x
print cub(3)

def empty(): # this block is empty
  pass

dictionary = {"one" : 1, "two" : 2}
print dictionary["one"]
del dictionary["one"] # delete entry from dictionary
print dictionary

class Person(object):
  def __init__(self, name):
    self.name = name
    self.lastName = None
    
class Employee(Person):
  def __init__(self, name, salary):
    super(Employee, self).__init__(name)
    self.salary = salary
    
tarun = Person("tarun")
goyal = Employee("goyal", 900)

print "Name of tarun is:", tarun.name
print "Name and salary of goyal is: ",goyal.name, goyal.salary
# // this type of comments do not work
