'''
1 We use the copy module of Python for shallow and deep copy operations.
'''
import copy

n = ['A','B','C']
l = [1,2,n,3]
l2 = copy.copy(l)
l3 = copy.deepcopy(l)
n.append('D')
l.append(4)

print(' \n L id is  :', id(l))
print(' \n L2 id is :', id(l2))
print(' \n L3 id is :', id(l3))

print(' \n L value is  :', l)
print(' \n L2 value is :', l2)
print(' \n L3 value is :', l3)






