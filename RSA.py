import random as ran
def mo(base,exp,mod):
    # it retuens x^m mod p    
    ans = 1
    base = base % mod

    while(exp > 0):
        if((exp % 2) == 1):
            ans = (ans * base) % mod
        exp = exp / 2
        exp = int(exp)
        base = (base * base) % mod;

    return ans;


def mrtest(p,s,u,r):
    for i in range(s):
        a = ran.randint(2, p-2);

        x = mo(a,r,p);
        if(x==1 or x==(p-1)):
            return True
        else:
            for j in range (u-1):
                x=mo(x,2,p);
                if(x==1):
                    return False
                if (x == (p-1)):
                    return True
    return False


def loop(s,b):
    loop.p = ran.randint(4, b);
    
    r = loop.p-1;
    u=0;
    while(r%2==0):
        r=r/2;
        u=u+1;
    r=int(r);
    if(mrtest(loop.p,s,u,r)):
        return True
    return False


def genprime(a,b):
    while(not loop(a,b)):
        print("generating p")
    p=loop.p
    while(not loop(a,b)):
        print("generating q")
    q=loop.p
    n = p * q
    phi = (p - 1) * (q - 1)
    return p,q,n,phi;


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def modinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b




def parameters():
    a=input("\n\nenter accuracy for prime generation : ")
    a=int(a)
    b=input("\nenter the maximum value for primes : ")
    b=int(b)
    p,q,n,phi = genprime(a,b)
    if(p==q):
        p,q,n,phi = genprime(a,b)
    #print("our parameters\n\n p : ",p,"\n\nq : ",q,"\n\nn : ",n,"\n\nphi : ",phi,"\n\n")
    ekey = input("\n\nenter private key between 1 and phi : ")
    ekey = int(ekey)
    GCD=gcd(ekey,phi)
    while(GCD != 1):
        ekey = input("\nenter private key again : ")
        ekey = int(ekey)
        GCD=gcd(ekey,phi)
    print("\n\n******** success ************\n\n")

    phi = int(phi)
    dkey = modinv(ekey,phi)

    pk = open("Private Key.txt","w")
    puk = open("Public key.txt","w")
    pn = open("N.txt","w")

    pk.write(str(dkey))
    puk.write(str(ekey))
    pn.write(str(n))


    print("\n**************************************************************************\n")
    print("our parameters\n\np : ",p,"\n\nq : ",q,"\n\nn : ",n,"\n\nphi : ",phi,"\n\n")
    print("\n************************************************\n")
    print("\n\npublic keys : \n\n",ekey,"\n\n",n)
    print("\n\nprivate keys : \n\n",dkey,"\n\n")
    print("\n************************************************\n")


def encrypt(e,m,n):
    mm = mo(m,e,n)
    return mm

def decrypt(d,c,n):
    mm = mo(c,d,n)
    return mm


def encrypt(e,m,n):
    mm = mo(m,e,n)
    return mm

def decrypt(d,c,n):
    mm = mo(c,d,n)
    return mm



def ende(prvk,pubk,n):

    x=int(input("\n\npress 1 to encrypt and 2 to decrypt message from message.txt  : "))
    if(x==1):
        mes = open("message.txt","r")
        ct = open("cipher text.txt","w")
        m=mes.read()
        x=len(m)
        i=0
        print("\n\n the encrypted message is stored in cipher text ")
        while(x>0):
            x=x-1
            y=int(ord(m[i]))
            i=i+1
            print("\n",y)
            g=str(encrypt(pubk,y,n))
            print("\n",g)
            ct.write(g)
            ct.write("\n")

    elif(x==2):
        mes = open("message.txt","w")
        ct = open("cipher text.txt","r")
        print("\n\nopening text from cipher text : ")
        arr = []
        arr = ct.readlines()
        al = arr.__len__()
        al = int(al)
        i=0
        for i in range(al):
            g=int(arr[i])
            f=chr(decrypt(prvk,g,n))
            mes.write(f)





print("\n\n*************************************** RSA ************************************\n\n")
ch=int(input("\n\nPress 1 to generate parameters or Press 2 to encrypt and decrypy    :    "))
if(ch==1):
    parameters()
elif(ch==2):
    pk = open("Private Key.txt","r")
    puk = open("Public key.txt","r")
    pn = open("N.txt","r")

    prvk = int(pk.read())
    pubk = int(puk.read())
    n = int(pn.read())
    ende(prvk,pubk,n)

else:
    print("\n\n fuck off u idiot\n\n")

























