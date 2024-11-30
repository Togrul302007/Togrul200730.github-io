text = input()
text = text.split()
test = {}
for i in text:
    s = len(i)
    test[i] = s
    if s < 4:
       print(i[::-1])
    elif s > 6:
        print(i[:3])

       
    
   
  