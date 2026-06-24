#Set

collection = {1,2,3,4,4,"rohit",9.8}
print(collection)
print(type(collection))
print(len(collection))  

collection = set()  #empty set ; syntax
print(type(collection))


###Set Method 
#1) set.add(el)
collection = {1,2,3,4,4,"rohit",9.8}
collection.add("bhise")
collection.add(5)
print(collection)

#2)sec.remove(el)
collection = {1,2,3,4,4,"rohit",9.8}
collection.remove('rohit')
print(collection)

#3)set.clear()
collection = {1,2,3,4,4,"rohit",9.8}
collection.clear()
print(len(collection))

#4)ser.pop()
collection = {"rohit","word","python",}
collection.pop()         #randomly value pop 
collection.pop()
print(collection)

#5) set.uninon(set2)
set1 ={1,2,3}

set2 ={2,3,4}
print(set1.union(set2)) 

#6)set.intersection(set2)
set1 ={1,2,3}
set2 ={2,3,4,5}
print(set1.intersection(set2))

#Q
dict = {
    "table": ["piece of paper", "list of facts & figures"],
    "cat" : "a small animal"
}
print(dict)

#Q

sub = {
    "python","java","c++","javascript","java",
    "python","java","c++","c"
}

print (len(sub))

#add marks subject 3
marks ={}

x = int(input("enter phy : "))
marks.update({"phy" : x })

x = int(input("enter math:"))
marks.update({"math":x})

x = int(input("enter bio:"))
marks.update({"bio":x})
print(marks)