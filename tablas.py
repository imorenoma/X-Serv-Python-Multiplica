#!/usr/bin/python3

"""Program to calculate product table"""

def multiply():

    for i in range(1, 11):
        print("\n" + "tabla del " + str(i))
        print("------------------")
        for j in range(1, 11):
            prod = i * j
            print(str(i) + " por " + str(j) + " es " + str(prod))

multiply()
