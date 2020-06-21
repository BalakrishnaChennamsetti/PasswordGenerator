import random
def randomPassword():
       
        numbers=['1','2','3','4','5','6','7','8','9','0']

        lowers=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        uppers=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        spec_sym=['@','$','&','*','_','-','#','.']
    

        password=random.choice(numbers)+random.choice(lowers)+random.choice(uppers)+random.choice(spec_sym)+random.choice(numbers)+random.choice(lowers)+random.choice(uppers)+random.choice(spec_sym)
        return password

l2=[]
c=0
for i in range(100000):
    l=randomPassword()
    if(l in l2):
        print("PASWORD REPETED...................")
        print(l2.index(l))
        print(c)
        continue
    l2.append(l)
    c+=1

    print(l)    
