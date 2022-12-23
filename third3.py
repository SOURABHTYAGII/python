#formating the string
str1="i love my india"
str2="how are you"
print("welcome",str1,str2)
print("welcome",str2,str1)
print("welcome {} {}".format(str1,str2))#formating
print("welcome {1} {0}".format(str1,str2))# reversing
print("welcome {about} {question}".format(about=str1,question=str2))# as variable