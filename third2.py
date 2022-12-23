#dictionary
a={"url1":"google.com","url2":"amazon.com"}
b={1:"sourabh",2:"moolya"}
print(b[1])
print(a["url1"])#url1(key)p
b[3]="tyagi"
print(b)
print(b[3])
print(b.get(2))# get method
b[4]=88
print(b)
print(b.get(4))
print(b.keys())# key comes only
print(b.items())# value come with key
print(b.values())# only values comes
print(b.pop(4))# remove the fourth key(selected key)
print(b.keys())
print(b.popitem())# dlt the last element
print(b.keys())
b.update({3:"demoqa.com"})# update the value of key
print(b)
b.update({4:"delhi",5:"dehradun"})
print(b)
b.setdefault(6,"goa")# also update the value of key
print(b)
b.clear()# clear the dictionary
print(b)