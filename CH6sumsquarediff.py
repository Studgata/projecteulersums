import math

def sumofs():
    sumofnum = 0
    
    for x in range(0,101):
        sumofnum = sumofnum + x
        
    d = sumofnum**2
    return(d)
    
def squareofs():
    squaresum = 0
    for x in range(0,101):
        d = x**2
        squaresum = squaresum + d
    return(squaresum) 
           
        
def main():
    
    sumofsquare = squareofs()
    squareofsum = sumofs()
    difference =  squareofsum - sumofsquare
    print(difference)
    
if __name__ =="__main__":
    main()
