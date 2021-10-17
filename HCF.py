A=int(input("enter first number: "))
B=int(input("enter second number: "))
if A>B:
    HCF=B
else:
    HCF=A
for I in range(1,HCF+1):
    if((A%I==0) and (B%I==0)):
        HCF=I
print("HCF is: ",HCF)
