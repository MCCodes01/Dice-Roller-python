import random
x = int(input("How many sides?: "))
y= int(input("How many die?: "))

def Die_roller(string):
    return(random.randint(1,x))

for i in range(y):

    print (Die_roller("string"))


