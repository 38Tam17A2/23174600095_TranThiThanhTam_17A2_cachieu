for n in range(100,1001):
    if n > 1:
        for i in range(2,int(n/2)+1):
            if(n % i) == 0:
                break
        else:
            print(n)
             
        
    