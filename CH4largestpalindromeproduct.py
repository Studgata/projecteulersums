def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return True
    else:
        return False 

def multiplication():
    
    p_num = []
    
    for x in range (100,1000):
        for y in range (100,1000):
            z = x*y
            tf = palindrome(z)
            if tf == True:
                p_num.append(z)
            
            
            
    print(max(p_num))

def main():
    multiplication()
    
if __name__ == "__main__":
    main()
