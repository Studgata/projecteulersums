def iterate():
    
    lst = []
    for x in range (1,300000000):
        tf = divis(x)
        if tf == True :
            lst.append(x)

    return (lst)        
#the range can be expanded to another number using iteritems.

def divis(num):
    for d in range(1,21):
        if num % d == 0 :
            continue
        else :
            return False 
            break 
        
    return True
    
def main():
    x= iterate()
    print(x)
    
if __name__ =="__main__":
    main()
