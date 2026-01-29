# Program for accepting List of Values and separate them with +ve and -ve values by using pass keyword

nov = int(input("How many values you want to Enter: "))

if nov <= 0:
    print("{} Invalid input".format(nov))
else:
    print("="*50)
    lst = []
    for i in range(1,nov+1):
        value = int(input("Enter Value no.{}: ".format(i)))
        lst.append(value)
    else:
        print("="*50)
        print("List of Values = {}".format(lst))
        print("-"*50)
        
        plst = []
        for i in lst:
            if i <= 0:
                pass
            else:
                plst.append(i)
        else:
            print("+VE values = {}".format(plst))
            print("No. of +VE values = {}".format(len(plst)))
            print("-"*50)

            nlst = []
            for i in lst:
                if i >= 0:
                    pass
                else:
                    nlst.append(i)
            else:
                print("-VE values = {}".format(nlst))
                print("No. of -VE values = {}".format(len(nlst)))
                print("-"*50)
