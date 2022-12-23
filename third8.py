list1=[8,9,10,45,"moolya","india","delhi"]
list2=["goa",67,98,45,"alibaba"]
c=zip(list1,list2) # mapping the lists(pair the two lists).as the form of tuples
print(list(c))
print(c)

list3=(1,2,3,4,5,6)
list4=("banglore","sourabh","tyagi","india")
d=zip(list3,list4)
#print(tuple(d))

for x,y in zip(list3,list4):
    print(x,y)
for x,y in d:
    print(x,y)
product=("pen","apple","orange","bike","car")
coastprice=(80,90,100,120,150)
sellingprice=(85,90,95,140,180)
e=zip(product,coastprice,sellingprice)
