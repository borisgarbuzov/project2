for n in range(2, 10):
    print (n)    
else:
    print("finished")

def f(n)    :
    return n**2
    
print (f(3)    )
print (f    )

a = []
a.append(1)
b = a.append("1")
print(b)
print(a)

a = 5
a += 1
print(a)

i = 5

def f1(arg=i):
    print(arg)
f1()
i = 6
f1()
f1(arg = 10)
f1(11)

def f2(a, L=[]):
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))
print(f2(a = 4, L=[5, 6, 7]))
print(f2(L=[5, 6, 7], a = 4))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

# stopped at dictionary arguments with stars
# https://docs.python.org/3/tutorial/controlflow.html
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
"""           
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
    
standard_arg(2)
standard_arg(arg=2)
pos_only_arg(1)
kwd_only_arg(3)
kwd_only_arg(arg=3)
combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3)
    
"""
def foo(name, **kwds):
    return 'name' in kwds

returned = foo(name = "name1")
print(returned)

returned = foo(name = "name")
print(returned)

returned = foo(name = "name", kwds = 'a')
print(returned)

returned = foo(name = "name", kwds = ['a'])
print(returned)

print("should be true?")
returned = foo(name = "noname", kwds = 'name')
print(returned)

print("Damn. Now it should be true for sure")
returned = foo(name = "anything", kwds = ['name'])
print(returned)

print("Without a function")
trueOrFalse = "name" in ['name']
print(trueOrFalse)

"""
def foo(name, /, **kwds):
    return 'name' in kwds
print(foo(1, **{'name': 2}))    
"""    

def concat(*args, sep="/"):
	return sep.join(args)
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

print(list(range(3, 6)))            # normal call with separate arguments
args = [3, 6]
print (list(range(*args)))

def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)    
print (f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)





















