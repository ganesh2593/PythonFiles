##d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
##def is_key_present(x):
##  if x in d:
##      print('Key is present in the dictionary')
##  else:
##      print('Key is not present in the dictionary')
##is_key_present(5)
##is_key_present(9)

##d1 = {'a': 100, 'b': 200}
##d2 = {'x': 300, 'y': 200}
##d = d1.copy()
##d.update(d2)
##print(d)

##var={1:"dhoni",False:"kohli",2:"ashwin",("a","b"):"rahul"}
##print(var["team"])
####output=var.get("team")
####print(output)
##print("welcome to python")

###to add a key
##var={}
##var['country']="india"
##print(var)

# 3 diff scenerio for running for looping

var={"name":"dhoni","age":33,"team":"csk"}
for x in var.items():
    print(x)

for y in var.values():
    print(y)

for z in var:
    print(z)
    

