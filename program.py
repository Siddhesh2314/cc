x=[] 
n=int(input("Enter how many no you want for Selection Sorting ")) 
for i in range(n): 
  print("Enter the Element",i,": ") 
  a=int(input("")) 
  x.append(a) 
 
print("unsorted element are", x) 
for i in range(0,len(x)-1): 
  for j in range(i+1,len(x)): 
    if x[i]>x[j]: 
      c=x[i] 
      x[i]=x[j] 
      x[j]=c

