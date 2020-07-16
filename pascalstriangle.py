
'''
                               1
                            1    1
                        1    2    1
                    1    3    3    1
                1    4    6    4    1
            1    5    10  10   5    1

'''

num= int(input("Enter the number of rows: "))

val1= 2*num

list1=[1]
list2=[]

for j in range(num):

    for i in range(val1):

        print(" ", end="")

    list2=[1]

    for jose in range(len(list1)-1):
        list2.append((list1[jose]+list1[jose+1]))

    list2.append(1)

    for k in list1:

        print(k, end="  ")

    print("\r")
    val1= val1-2
    list1= list2





