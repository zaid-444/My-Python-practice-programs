# Write a python program which will read the records from employee file where employee record are present by using unpickling process

import pickle

with open("emp.data",'rb') as fp:
    while True:
        try:
            emp = pickle.load(fp)
            for val in emp:
                print(val,end="\t")
            print()
        except EOFError:
            break