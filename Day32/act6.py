# Variable Length Arguments

def callme(arg, *vartuple):
    print("India??")
    print(arg)
    for var in vartuple:
        print(var)

callme("Democracy", "or", "Gerontocracy")