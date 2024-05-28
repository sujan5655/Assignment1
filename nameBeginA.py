#5. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name starts with ‘a’ or ‘A’
namelist=[]

for name in range(10):
    yourname=input("enter your name")
    namelist.append(yourname)
print("name of people begin with 'a' or 'A'")
for name in namelist:
    if(name.lower().startswith('a')):
        print(name)
    else:
        print()