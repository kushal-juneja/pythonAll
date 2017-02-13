'''
Objective
1. Create file
2. Write to it
3. Read from it
'''

#Open the file in read/write mode
file_obj= open('tstFile',mode='a+')
#a+ --> Append  and read; w+ --> overwrite and read

#Make an object
a={'FirstName':'Kushal',
   'LastName':'Juneja',
   'Age':'5M Years'
   }

#Write the file
for i in range (1000):
    file_obj.write(str(a)+'\n')


#Close the connection
file_obj.close()


#Read the file
file_open = open('tstFile',mode='r')
i=0;
for lin in file_open:
    i+=1
    print('this is %d line of the file'%i)
    print(lin)





