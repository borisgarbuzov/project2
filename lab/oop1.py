class Person:
    instance_count_field = 0
    
    def __init__ (self):
        Person.instance_count_field += 1
    
    
    def say_hi_with_self(self):
        print('With self. Hello, how are you?')

    @staticmethod        
    def say_hi_no_self():
        print('No self. Hello, how are you?')

    @staticmethod        
    def get_instance_count():
        return Person.instance_count_field
        
        
p = Person()
p.say_hi_with_self()

Person.say_hi_no_self()

max_instance_count = 10
for instance_index in range(max_instance_count):
    Person()
    print(Person.get_instance_count())

#----------------------------- 

class Person2:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person2('Swaroop')
p.say_hi()

#---------------------------------------------------- 


class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 9

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:o} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:o} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()




print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()


my_object = Robot("C-3PO")
del my_object
print("before")
# print(my_object)
print("after")

class MyClass:
    
    
    def my_method(self):
        print("my_method is called")
        # my_field = 5

my_class_instance = MyClass()
my_class_instance.my_field = 6
my_class_instance.my_field2 = 7
print("before")
print(my_class_instance)
print(my_class_instance.my_field)
print(my_class_instance.my_field2)
print("after")
