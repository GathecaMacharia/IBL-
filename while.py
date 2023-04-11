"""
while True:
    x=int(input("enter the value of X "))
    if x<0:
        continue
    else:
        break
"""

def main():
    number= get_number()
    helloworld(number)
def get_number():
    while True:
        x=int(input("enter the value of X "))
        if x > 0:
            break
    return x

def helloworld():
    for _ in range(x):
        print("hello world")


main()
      
