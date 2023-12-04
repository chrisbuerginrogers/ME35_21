#-------------------------- Matricies
#first get an array of 1s and 0s
import numpy as np
from PIL import Image
a = np.zeros((7,7), dtype=np.uint8)
a[1:6, 2:5] = 1; a[1:3,3] = 0
a[3:5, 0:3] = [1,1,0]

#if you want to see your image
Image.fromarray(a*255)

#if you want just the 3rd row:
print(a[2])

#3rd, 4th, and 5th row
print(a[2:5])

# a specific point
print(a[2,3]) #or a[2][3]

#or the 3rd column
print(a[0:,2]) #or a[:,2]

#or the lower right part of a
print(a[2:,3:])

#or any subset
print(a[2:4,3:5])

#and a color image, you can define
#a subset and then b,g, or r (0,1 or 2)
cv2_image[100:105,90:95,0]
    
#-------------------- Lists
grandkids = ['Harper','Charlie','Nathan']
print(grandkids[0])
for kid in grandkids:
    print(kid)
for i,kid in enumerate(grandkids):
    print("%d: %s"%(i,kid))
print('I have %d grandkids'%(len(grandkids)))
grandkids.append('Fred')
print(grandkids)
grandkids.pop(grandkids.index('Fred'))
print(grandkids) 
grandkids.reverse()
print(grandkids) 
grandkids.insert(1,'Harper')
print(grandkids)
grandkids.sort()
print(grandkids)
print(grandkids.count('Harper'))
grandkids.pop(1)
random = [2,'hi',True] #note lists can be different data types

#--------------------- Tuples
kidTuple=('Harper','Charlie','Nathan')
print(len(kidTuple),kidTuple)
print(kidTuple[2])

#---------------------- Sets
cards={'A',2,3,4,5,6,7,8,9,10,'J','Q','K'}
print(4 in cards)
if 12 not in cards:
    cards.add(12)
for card in cards:
    print(card,end=', ')
print('') # need to finish the print
cards.remove(12) #use card.discard(12) to avoid an error in 12 is not in the set

#----------------------- dictionary
GPA = {'fred':3.5, 'sally': 3.7, 'hank': 3.0, 'Sunil':'A+'}
print(GPA['Sunil'])
GPA.pop('Sunil')
GPA.update({'kim':4.0})
for student in GPA.values(): #try replacing values with keys and items
    print(student)
for key,value in GPA.items():
    print(key,value)
Grads = {'ed':3.2, 'jill': 3.4, 'martha': 2.9}
students = {'ugrads':GPA, 'grads':Grads}
print('Sally got a %f'%students['ugrads']['sally'])
print('The max was %0.2f'%max(GPA.values()))
print(students)
