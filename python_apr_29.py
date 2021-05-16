##my_file=open('Ganesh.txt',"w")
##my_file.write('\n')
##my_file.write('csk won against srh')
##my_file.close()

#context manger
##
##with open('ganesh.txt','a') as my_file:
##    my_file.write("\n")
##    my_file.write("welcome")


##with open('ganesh.txt','r') as my_file:
##    output=my_file.read(4)
##    output1=my_file.read()
##    print(output)
##    print("________________")
##    print(output1)

##with open('ganesh.txt','r') as my_file:
##    output=my_file.readline()
##    print(output)
##    output1=my_file.readline()
##    print(output1)

##with open('ganesh.txt','r') as my_file:
##    output=my_file.readlines(5)
##    print(output)

with open('ganesh.txt','a+') as my_file:
   my_file.write("IPL")
   my_file.seek(0)
   output=my_file.read()
   print(output)

 
    
    
