def main():
    a=input("Enter string: ")
    words = a.split()
    a_rev = ' '.join(reversed(words))
    print (a_rev)

main()
