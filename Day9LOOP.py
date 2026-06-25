#LOOP
count = 1
while count <=5 :   #stopping condition
    print("rohit")
    count += 1
print(count)


i = 1
while i <= 5 :#stopping condition
    print("demo")  
    i +=1
    # print(i)

i = 5
while i >=1 : #stopping condition
    print(i)
    i -=1
print('end code')    

#Q print numbers from 1 to 100
i=1
while i <=100:  #stopping condition
    print(i)
    i+=1
print('end')  

#Q print numbers from 100 to 1

i=100
while i>=1: #stopping condition
    print(i)
    i-=1
print('end code')    

#Q print the multiplication table of a number n

i = 3
while i <= 30:  #stopping condition
    print(i)
    i +=3
print('table')    

n = int(input('enter number:'))
i = 1
while i <=10:
    print(n*i)
    i +=1
print('table')    

#Q print the element of the following list using  LOOP 

num=[1,4,9,16,25,36,49,64,81,100]

i =0
while i < len(num):
    print(num[i])
    i +=1

#Q 
num=(1,4,9,16,25,36,49,64,81,100)

x = 49
i = 0
while i < len(num):
    if (num[i]==x):
          print('found at idx',i)
    else:
         print('finding')
    i +=1


#BREAK
i = 0
while i <= 5:
    print(i)
    if(i == 3):
       break
    i +=1
print('end of loop')


#continue
i =0 
while i <=5:
    if(i ==3):
        i +=1
        continue #skip
    print(i)
    i +=1

#FOR loop 

list = [1,2,3,4,5,6]

for val in list:
    print(val)
 

num = (1,4,9,16,25,36,49,64,81,100,25)
x =25

idx =0
for el in num:
    if(el ==x):
        print("number found at idx",idx)
        break
    idx +=1


for i in range(10):
    print(i)

for i in range(2,20):
 print(i)

for i in range(2,100,2):  #even num
    print(i)


for i in range(1,100,2):  #odd num
    print(i)

#Q
n = int(input("enter num:"))

for i in range(1,11):
    print(n*i)


