Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=6
for i in  range(n):
  for j in range(n):
    print(i,end=" ")
  print()

n=6
for i in  range(n):
  for j in range(n):
    print(i,end=" ")
  #print()
... 
... n=6
... for i in  range(n):
...   for j in range(n):
...     print(i,end=" ")
...   print('\n')
... 
... n=6
... for i in  range(n):
...   for j in range(n):
...     print(j,end=" ")
...   print()
... 
... n=6
... for i in  range(n):
...   for j in range(n):
...     print(max(i,j),end=" ")
...   print()
... 
... 
... n=6
... for i in  range(n):
...   for j in range(n):
...     print(n-i,end=" ")
...   print()
... 
... 
... n=6
... for i in  range(n):
...   for j in range(n):
...     print(n-j,end=" ")
...   print()
... 
... n=6
... for i in  range(n):
...   for j in range(n):
...     print(max(n-i,n-j),end=" ")
...   print()
... 
... 
... n=6
... for i in  range(n):
...   for j in range(n):
...     print(i+1,end=" ")
...   print()
... 
... 
n=6
for i in  range(n):
  for j in range(n):
    print(j+1,end=" ")
  print()

n=6
for i in  range(n):
  for j in range(n):
    print(n-i-1,end=" ")
  print()

n=6
for i in  range(n):
  for j in range(n):
    print(n-j-1,end=" ")
  print()

n=6
for i in  range(n):
  for j in range(n):
    print(max(n-i-1,n-j-1),end=" ")
  print()


#1st method
n=6
for i in  range(n):
  for j in range(n):
    print(max(i+1,j+1,n-i,n-j),end=" ")
  print()

#2nd method
n=6
for i in  range(n):
  for j in range(n):
    print(max(max(i+1,j+1),max(n-i-1+1,n-j-1+1)),end=" ")
  print()

#write the question for these solution

n=7
for i in  range(n):
  for j in range(n):
    print(max(i+1,j+1,n-i,n-j),end=" ")
  print()

n=7
for i in  range(n):
  for j in range(n):
    print((i,j),end=" ")
  print()


