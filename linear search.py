Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst=[]#creating empty list
p=int(input("enter the no of values"))#taking nof valus from user

for i in range(p):#creating lst
    vals = int(input("enter the next value"))

    lst.append(vals)
print(lst)
n=int(input("enter the value for search"))

pos=-1
def search(lst,n):#creating search function

    for i in range(n):
        if lst[i]==n:
            globals()["pos"]=i
            return True

    else:
        return False



if search(lst,n):
    print("found at",pos,'place')
else:
    print("not found")