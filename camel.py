
name = input("What is your name: ")
ans = " "
for i in name:
    if(i.isupper()):
        ans+= "_" + i.lower()
    else:
        ans+= i
print(ans[1:])