def main():
    x = [2,3,4,5,6,7,8,9,1]
    i=0
    print (x)
    while (i<3):
        x.remove(max(x))
        i= i+1
    print (max(x))

main()
        
        
