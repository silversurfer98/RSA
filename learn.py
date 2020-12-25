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
    r = b-1;
    u=0;
    while(r%2==0):
        r=r/2;
        u=u+1;
    r=int(r);
    if(mrtest(b,s,u,r)):
        return True
    return False

x=int(input("enter the num :   "))
s=int(input("enter the acc :   "))
if(loop(s,x)):
    print("\n\nmama")
else:
    print("\n\noma")