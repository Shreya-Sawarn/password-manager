import string
import random

if __name__=='__main__':
    s1=string.ascii_lowercase
    #print(s1)
    s2=string.ascii_uppercase
    #print(s2)
    s3=string.digits
    #print(s3)
    s4=string.punctuation
    #print(s4)
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print (s)
    random.shuffle(s)
    #print(s)
    
    try:
        plen = int(input("Enter the password length: "))
        print("".join(random.sample(s, plen)))
    except ValueError:
        print("Please enter a valid number.")
