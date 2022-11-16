#creating a list its same as arry but yemsa list bhancha
a=[1,2,34,23,34]
print(a)
  
print(a[0])
# in this index starts with 0

#to modify
a[0]=22
print(a)
#list was modified 


# we can create index using diff types of items as well
b=[1,2,"hello",6.5,True]#all types of value
print(b)
print(b[3])

#we can concat the array
print(a+b)

#we can slice list also
print(b[0:3])
#its same as string

#to calculate length
c=len(a)
print(c)

#sort list data
d=[2,4,5,9,6,8]
d.sort()
print(d)



#to reverse
d.reverse()
print(d)

# to add at last we use append
d.append(3)
print(d)


#to imsert from anywhere
d.insert(2,9) #now two index ma 9 add huncha as you can see
print(d)



#to take out data from list
d.pop(2)
print(d)


#ani index use na gari remove garna chai we have
d.remove(6)
print(d)
#now 6 is removed


# !!! if we want more function of the list then go to python.doc
