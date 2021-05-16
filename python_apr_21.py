#output ={0:0,1:1,2:4,3:9}


output={}
for x in range(5):
    output[x]=x*x
print(output)

##output={x:x*x for x in range(4)}
##print(output)

##var={"name":["india","ashwin","csk"]}
##var["name"][2]="rcb"
##print(var)

#how to merge two dictionary
##var={"name":"dhoni"}
##var1={"age":33}
####var.update(var1)
####print(var)
##output={**var,**var1}
##print(output)

##import json
##var ='{"name":"dhoni"}'
##output = json.loads(var)
##print(output)
##print(type(output))

val=[{"name":"ganesh"},{"name":"athi"}]
for x in val:
    for i in x.values():
        print(i)


