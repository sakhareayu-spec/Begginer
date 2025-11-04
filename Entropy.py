import math
s=0
r=0
inputs=[]
b = int(input("Enter the number or probabilities = "))
for b1 in range (b):
  c = float(input(f"Enter the probability number {b1+1} = "))
  s+=c
  inputs.append(c)
  b1+=1
if s==1:
  p = c*math.log2(1/c)
  print("The entropy is = ",p)
  r+=p
else:
  print("The sum of probabilities should be equal to 1")

print("The total entropy is = ",r)
  
  
  
     
