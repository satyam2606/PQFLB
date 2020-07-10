while 1:
    try:
        x=int(input("Enter integer only"))
        break;
    except ValueError:
        print(" ERROR !!!!! Enter integers only")
        continue;
print("Entered number is ",x)
