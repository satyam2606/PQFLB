year=int(input("Enter Year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("YES LEAP YEAR")
        else:
            print("NOT LEAP YEAR")
    else:
        print("YES LEAP YEAR")
else:
    print("NOT LEAP YEAR")
