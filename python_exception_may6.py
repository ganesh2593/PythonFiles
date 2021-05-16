##try:
##    var=10
##    print(var)
##except:
##    print("sorry")

##try:
##    var="a"+12
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex)
##except:
##    print("welcome")

try:
    var=2+","
    print(var)
except Exception as ex:
    print(ex)
else:
    print("no error")
finally:
    print("running")
