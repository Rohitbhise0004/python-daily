#list 

marks = [95.2, 45.2,65.3,87.3,98.4,41.2]
print(marks)
print(type(marks))

print(marks[2]) #indexing 
print(len(marks))# lenght

# list slicing 

marks = [63,14,25,63,52]
print(marks[1:3]) 
       
#list method 

#1) Append - add one element at the END
list = [2,1,3]
list.append(4)     
print(list)

#2) Sort - sort in ascending and descending order.
list = [2,1,3]
list.sort()  # sort in ascending order
print(list)

list = [2,1,3]
list.sort(reverse=True) #sort in descending oeder
print(list)

#3) Reverse -reverse list 
list =[2,1,3]
list.reverse() 
print(list)

#4) Insert
list = [2,1,3]
list.insert(2,5)
print(list)

#5)Remove
list = [2,1,3,1]
list.remove(1)
print (list)

#6) POP
list = [5,1,3,1]
list.pop(0)
print(list)


