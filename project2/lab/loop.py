knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)
knights.values()	;

pairList = [(1,1), (2,2)]
for k in pairList:
    print("k =", k)
    
for k1, k2 in pairList:
    print("k1 =", k1, ", k2 =", k2)

myEnumeration = enumerate(['tic', 'tac', 'toe'])
print (list(myEnumeration))
for i, v in myEnumeration:
    print(i, v)

questions = ['name', 'quest', 'favorite color', 'bbb']
answers = ['lancelot', 'the holy grail', 'blue', 'aaa']
for q, a in zip(questions, answers):
	print('What is your {0}?  It is {1}.'.format(q, a))
	
print (questions, answers)	
myTuple = (questions, answers)
print (myTuple)
myZip = zip(questions, answers)
print (myZip)
print (list(myZip))



	


