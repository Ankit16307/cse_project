print()
print('                            ACCOUNT MANAGEMENT                 ')
print()
u=input('username         - ')
ac=0
while ac!=1:
    a=int(input('age              - '))
    if a>0:
        ac=1
    else :
        print('invalid input, try again')
gc=0
while gc!=1:
    g=input('gender (M/F)     - ')
    if g=='M' or g=='F':
        gc=1
    else:
        print('invalid input, try again')
        
p=input('password         - ')
c=input('confirm password - ')
l=[]
n=''
print()
if p==c:
    l=[[u,p,n,g,a]]
    print()
    print('account created successfully')
else:
    print('wrong password')
    
print()
print('Do you want to -')
print('1. Sign up another account')
print('2. Log in')
print('3. List of accounts ')
print('4. Delete account')
print('5. Exit')
print()
s=0

while s!='5':
    s=input('Type corresponding serial no. to proceed - ')
    print()
    
    if s=='1':
        u=input('username         - ')
        ac=0
        while ac!=1:
            a=int(input('age              - '))
            if a>0:
                ac=1
            else :
                print('invalid input, try again')
        gc=0
        while gc!=1:
            g=input('gender (M/F)     - ')
            if g=='M' or g=='F':
                gc=1
            else :
                print('invalid input, try again')
        p=input('password         - ')
        c=input('confirm password - ')
        n=''
        print()
        if p==c:
            l=l+[[u,p,n,g,a]]
            print('account created successfully')
        else:
            print('wrong password')
        print()
        print('Do you want to -')
        print('1. Sign up another account')
        print('2. Log in')
        print('3. List of accounts ')
        print('4. Delete account')
        print('5. Exit')
        print()
        
    elif s=='2':
        lu=input('username         - ')
        lp=input('password         - ')
        print()
        a=0
        for i in l:
            if i[0]==lu:
                if i[1]==lp:
                    print('successfully logged in')
                    print()
                    
                    print('Do you want to -')
                    print('1. Open notepad')
                    print('2. Change password')
                    print('3. Log out')
                    t=input('Type corresponding serial no. to proceed - ')
                    print()
                    if t=='1':
                        
                        print('NOTEPAD - ')
                        print()
                        print(i[2])
                        ni=input()
                        print()
                        i[2]=i[2]+'\n'+ni
                        print('successfully logged out')
                        print()
                    elif t=='2':
                        cp=input('enter new password - ')
                        ccp=input('confirm new password -')
                        i[1]=cp
                        print()
                        print('password changed successfully')
                        print('Logged out, you need to login again.')
                        print()
                    elif t=='3':
                        print('successfully logged out')
                        print()
                    a=1
                else:
                    print('wrong password')
                    print()
                    a=1
        if a==0:
            print('no account found')
            print()
        print('Do you want to -')
        print('1. Sign up another account')
        print('2. Log in')
        print('3. List of accounts ')
        print('4. Delete account')
        print('5. Exit')
        print()
        

    elif s=='3':
        print('List of accounts - ')
        print()
        for i in l:
            print('username:',i[0],' ','age:',i[4],' ','gender:',i[3])
        print()
        print('Do you want to -')
        print('1. Sign up another account')
        print('2. Log in')
        print('3. List of accounts ')
        print('4. Delete account')
        print('5. Exit')
        print()
        
    elif s=='4':
        lu=input('username         - ')
        lp=input('password         - ')
        print()
        a=0
        for i in l:
            if i[0]==lu:
                if i[1]==lp:
                    l.remove(i)
                    print('account deleted successfully')
                    print()
                    a=1
                else:
                    print('wrong password')
                    a=1
        if a==0:
            print('no account found')
            print()
        print('Do you want to -')
        print('1. Sign up another account')
        print('2. Log in')
        print('3. List of accounts ')
        print('4. Delete account')
        print('5. Exit')
        print()
        
    else:
        print('wrong input')
        print()
        
print()
print('                                    THANK YOU')
    

