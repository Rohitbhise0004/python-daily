# Strings 
# A string is a sequence of characters.
# Strings are immutable, which means that once a string is created, it cannot be changed.

str1 = "i am rohit "
str2 = "i am from ngp"
srt3 ='password'
print(str1) 

# String concatenation
str1 = "i am rohit "
str2 = "i am from ngp"
finalstr = str1 +str2
print(finalstr)



#string length
str1 = "rohit"
len1 = len(str1)
print(len1)
print(len(str1))

str2 ='ROHITBHISE'
len2 = len(str2)
print(len2)

#indexing

str ='rohit'
print (str[3]) 

#Slicing
str ='rohitbhise'
print(str[1:4])

str = 'i am a coder'
print(str.endswith('er'))  #endwith
print(str.capitalize())    #capitalize
print(str.replace('coder','rohit'))  #replace
print(str.count('am'))
print(str.find('o'))

#Q.WAP to give input from user and print the length of the string.
str = input("enter user name:")
print(len(str))

#q.WAP to give input from user and print the first and last character of the string.
str = input("enter name:")
print("first character:",str[0])
print("last character:",str[-1])

#q.WAP to give input from user and print the string in reverse order.
str =input('enter name:')
print(str[::-2])