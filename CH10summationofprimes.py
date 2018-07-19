import itertools
def primebelow(x):
    sumd = 0 
    for d in range(0,x):
        tf = checkprime(d)
        if tf == True :
            sumd = sumd + d    
    print (sumd)


def checkprime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def main():
    val = primebelow(2000000)            
    #val = checkprime(167)
    print(val)  
    
if __name__=="__main__":
    main()
