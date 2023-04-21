rhym = {"1": "David",
        "2": "Vlad",
        "3": "Lexa",
        "4": "Boda",
        "5": "Aleks"
    }
n = input("Enter a number: ")
if n in rhym:
    rhym = rhym[n]
    print(rhym)
else:
    print("not found")