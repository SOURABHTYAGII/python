a={55,56,78,87,67,56,78,'hello'}
b={67,9,45,8,56,78}
c=a.union(b) # add to list without common data
print(c)
d=a.symmetric_difference(b) # remove common data
print(d)
e={78,56}
print(a.issuperset(e))
e.discard(78)
print(e)
print(55 in a) # to check value is exists in given list or not
#print(a[1:3:6])
#print(a[2])