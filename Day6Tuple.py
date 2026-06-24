#TUPLE

tup = (2,1,3,1)
print(tup)
print(type(tup))

#TUPLE Method   
#1) INDEX
tup = (1,2,3,4,)
print(tup.index(2))

##QWAp to ask the user enter names of their 3 favorite movies & store them in a list
movies =[]
mov1 =input("enter 1st movie:")
mov2 =input("enter 2st movie:")
mov3 =input("enter 3st movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#Q WAP to check if a list contains a palindrome of element.
list1 =[1,2,3,2,1]
 
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("this is the palindrome")
else:
    print("this is not palindrome")  

print ("end code")


grade = ("c","d","a","a","b","b","a")
print(grade.count("a"))

grade = ["c","d","a","a","b","b","a"]
grade.sort()
print(grade)

