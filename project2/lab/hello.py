from src.compute_and_save_cov_and_cov_hats import compute_and_save_cov_and_cov_hats
import numpy as np

print ("hello world")

try:
    compute_and_save_cov_and_cov_hats(
        sample_size = None,
        t_par_count = None,
        gamma_count = None,
        mean = None,
        sigma = None,
        lag = None,
        noise_type = None,
        diag_or_horiz = None,
    )
except:
    print("I caught ")

# https://docs.python.org/3/tutorial/
a = 5
a
print(a)
print(round(a, 2))
'spam eggs'

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print ("abc"[1])
print ("123"[0:2])
print ("123"[0:3])
print ("123"[0:42])
squares = [1, 4, 9, 16, 25]
print (squares)
print (np.array(squares)**3)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
[['a', 'b', 'c'], [1, 2, 3]]
x[0]
['a', 'b', 'c']
x[0][1]

a, b = 0, 1
# while a < 10:
#    print(a)

print ("no brackets")   
while a < 10:
    print(a)
    a, b = b, a+b
print ("what happened?") 
print ("brackets 1")
print ("brackets 2 is eaten up if no line break for some reason \n") 
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

x = 5
if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))    

"""
users = {1, 2, 3}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
"""        
for i in range(5):
    print(i)  
print(range(7))        
print(list(range(7)))    
print(np.array(range(7)))    

# arguments
myList = [1, 2, 2, 'a', 'a', 'b']
first, second, *third = myList
print("first = ", first)
print("second = ", second)
print("third = ", third)

print("\n star on first ")
myList = [1, 2, 2, 'a', 'a', 'b']
*first, second, third = myList
print("first = ", first)
print("second = ", second)
print("third = ", third)
 
print("\n packing ")
def summator(*terms):
    return sum(term for term in terms)
    
print("summator('1, 2') = ", summator(1, 2))    
"""
>>> date_info = {'year': "2020", 'month': "01", 'day': "01"}
>>> track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
>>> filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
...     **date_info,
...     **track_info,
... )
>>> filename
'2020-01-01-Beethoven-Symphony No 5.txt'
"""
stringDictionary = {'a': "aa", 'b': "bb", 'c': "cc"}
numberDictionary = {1: 11, 2: 22}
myString = "{a}, {b}, {c}".format(**stringDictionary)
print(myString)
print(stringDictionary['a'])

a = [11, 2, 1, 1]
print ("x = ", x)
a[len(a):] = [x]
print ("a = ", a)
a.insert(1, 10)
print ("a = ", a)
a.remove(1)
print ("a = ", a)
# returned = a.pop([1])
# print(returned)

squares = list(map(lambda x: x**2, range(10)))
print ("squares = ", squares)

myMap = map(lambda x: x**2, range(10))
print ("myMap = ", myMap)
squares = [x**2 for x in range(10)]
print ("squares = ", squares)
print ([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print ([(x, y) for x in [1,2,3] for y in [3,1,4] if x == y])

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
print(len(matrix))
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)
print(len(transposed))

for row in matrix:
    print("row =", row)
    
sameMatrix = [row for row in matrix]
print("sameMatrix =", sameMatrix)
print("sameMatrix is matrix =", sameMatrix is matrix)

print("suppose there is an external cycle with i = ...")
i = 0
col0 = [row[i] for row in matrix]
i = 1
col1 = [row[i] for row in matrix]
i = 2
col2 = [row[i] for row in matrix]
i = 3
col3 = [row[i] for row in matrix]
transposed = [col0, col1, col2, col3]
print("transposed =", transposed)

a, b = 1, 2
myList = [a, b] = 1, 2
print("myList = ", myList)
print("type(myList) = ", type(myList))
# myList[1] = "a"
myProperList = [1, 2]
myProperList[0] = 10
print("myProperList = ", myProperList)

list(zip(*matrix))
print("matrix = \n", matrix)
print("*matrix = \n", *matrix)
# row1, row2, row3 = *matrix
print("zip(*matrix) = \n", zip(*matrix))
print("list(zip(*matrix)) = \n", list(zip(*matrix)))

print ("zip([1, 2]) = ", zip([1, 2]))






