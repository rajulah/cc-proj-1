import sys
def abcd():
    # var = input("Please enter something: ")
    # print("You entered: " + var)
    try:
        # print(sys.argv[1])
        # argu = json.loads(sys.argv[1])
        argu = sys.argv[1]
        # print(argu)
        return argu
    except:
        print("lolol")
        raise Exception("error while loading argument")

print(abcd())