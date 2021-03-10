import random
def x():
    str=input()
    print("%s"%str[::1]) 
    
def x1():
    lst1=[num for num in input().split()]
    lst2=[num for num in input().split()]
    s1=set(lst1)
    s2=set(lst2)
    print(len(s1&s2))

def x2():
    lst=[[0]*7]*5
    for i in range(5):
        lst[i]=input().split()

    for i in range(7):
        for j in range(5):
            print(lst[j][i],end="\t")
        print()
    print()

def x3():
    n=input()
    for i in range(len(n)):
        print(n[i],end=" ")
    print()

def x4():
    n=int(input())
    lst=[]
    for i in range(n):
        lst.append(input())
    for i in range(len(lst)):
        for j in range(len(lst)):
            if int(lst[i]) < int(lst[j]):
                tmp=lst[i]
                lst[i]=lst[j]
                lst[j]=tmp
    for i in lst:
        print(i)