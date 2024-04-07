#importing modules
from cryptography.fernet import Fernet
import math

#--------------------------------------------------------------------------------------------------------
#title

print ("       -------------------------------------------------------------    ")
print ("            * DATALOCK!- The Encryption And Decryption Program! *    ")
print ("       -------------------------------------------------------------    ")

print ("\nHello! I will help you encrypt and decrypt your message...")

#------------------------------------------------------------------------------------------------------
#Symmentric and assymetric encryption/decryption choice
option = input("\nEnter 1 for symmetric and 2 for asymmetric encryption/decryption : ")

#symmetric encryption/decryption using Fernet       
if option == "1":
    print ("\n****************************************************************************")
    print ("\n             You have chosen symmetric encryption/decryption!               ")
    print ("\n****************************************************************************")
    key = Fernet.generate_key()
    file = open('key.key','wb')
    file.write(key)
    file.close()
    
    file = open('key.key','rb')
    key = file.read()
    file.close()
    message = "x"
    while message != ("exit"):
        message = input("\nenter your message here('exit' to quit): ")
        select = input("\nType 'E' for encryption and 'D' for decrytion: ")
        if(select=='E'):
            encoded = message.encode()
            f = Fernet(key)
            encrypted = f.encrypt(encoded)
            print("\nENCRIPTED MESSAGE IS:\n\n",encrypted)

            file = open('key.key', 'rb')
            key2 = file.read()
            file.close()
        elif(select == 'D'):
            f2 = Fernet(key)
            decrypted = f2.decrypt(encrypted)
            original_message = decrypted.decode()
            print ("\nTHE DECRYPTED MESSAGE IS:\n", original_message)
        else:
            print("\nyou have entered the wrong option")
        
#----------------------------------------------------------------------------------------------------------
#Asymmetric encryption decryption using RSA

elif option == "2":
    print ("\n****************************************************************************")
    print ("\n           You have chosen asymmetric encryption/decryption!           ")

    p = 283
    q = 563

    def prime_check(a):
        if(a==2):
            return True
        elif((a<2) or ((a%2)==0)):
            return False
        elif(a>2):
            for i in range(2,a):
                if not(a%i):
                    return false
        return True
 
    check_p = prime_check(p)
    check_q = prime_check(q)
    while(((check_p==False)or(check_q==False))):
        check_p = prime_check(p)
        check_q = prime_check(q)
 
    #RSA Modulus
    n = p * q
 
    #Eulers Toitent
    r= (p-1)*(q-1)
 
    #GCD
    def egcd(e,r):
        while(r!=0):
            e,r=r,e%r
        return e
 
    #Euclid's Algorithm
    def eugcd(e,r):
        for i in range(1,r):
            while(e!=0):
                a,b=r//e,r%e
                if(b!=0):
                    temp = 5
                r=e
                e=b
 
    #Extended Euclidean Algorithm
    def eea(a,b):
        if(a%b==0):
            return(b,0,1)
        else:
            gcd,s,t = eea(b,a%b)
            s = s-((a//b) * t)
            return(gcd,t,s)
 
    #Multiplicative Inverse
    def mult_inv(e,r):
        gcd,s,_=eea(e,r)
        if(gcd!=1):
            return None
        else:
            if(s<0):
                temp = 5
            elif(s>0):
                temp = 5
            return s%r
 
    #e Value Calculation
    '''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
    for i in range(1,1000):
        if(egcd(i,r)==1):
            e=i
 
    #d, Private and Public Keys
    '''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
    eugcd(e,r)


    d = mult_inv(e,r)

    public = (e,n)
    private = (d,n)

    #Encryption
    '''ENCRYPTION ALGORITHM.'''
    def encrypt(pub_key,n_text):
        e,n=pub_key
        x=[]
        m=0
        for i in n_text:
            if(i.isupper()):
                m = ord(i)-65
                c=(m**e)%n
                x.append(c)
            elif(i.islower()):               
                m= ord(i)-65
                c=(m**e)%n
                x.append(c)
            elif(i.isspace()):
                spc=400
                x.append(400)
        return x
     
 
    #Decryption
    '''DECRYPTION ALGORITHM'''
    def decrypt(priv_key,c_text):
        d,n=priv_key
        txt=c_text.split('X')
        x=''
        m=0
        for i in txt:
            if(i=='400') or i =='X400':
                x+=' '
            else:
                m=(int(i)**d)%n
                m+=65
                c=chr(m)
                x+=c
        return x

    def myconvert(x):
        mystr = ""
        for i in x:
            mystr = mystr + str(i) + "X"
        
        mystr= mystr[:-1]
        return mystr
 
    #Message
    print ("\n****************************************************************************")
    message = 'x'
    while message != "exit":
        message = input("\nEnter the message you want encrypted or decrypted('exit'to quit): ")
        print("\nYour message is: ",message)
        #Choose Encrypt or Decrypt and Print
        choose = input("\nType 'E' for encryption and 'D' for decrytion: ")
        if(choose=='E'):
            enc_msg=encrypt(public,message)
            enc_msg=myconvert(enc_msg)
            print("\nYour encrypted message is:",enc_msg)
        elif(choose=='D'):
            dec_msg=decrypt(private,message)
            print("\nYour decrypted message is:",dec_msg)
        elif(choose!='E' or choose!='D'):
            print("\nYou entered the wrong option.")
        elif(choose=="exit"):
            break
        


    
