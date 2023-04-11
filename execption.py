while True:
    try:
        x=int(input("enter the value of x "))
        print(f"x is {x}")
    except ValueError:
        print("X is not an Interger")
else:
    break

print(f"x is{x}")

