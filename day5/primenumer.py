#Print Prime numbers between 1 to 100
print(1)
for i in range(2,101):
         prime=True
         for j in range(2,i):
                  num=i%j
                  if num==0:
                          prime=False
                          break
         if prime:
                  print(i)          