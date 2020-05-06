from flask import Flask,render_template,request
app = Flask(__name__)                                 #InitiateFlask
app.config['TEMPLATES_AUTO_RELOAD'] = True
twok=0
fiveh=0
h=0
atm=0
p1=101
p2=102
p3=103
p4=104
p5=105
pin101=1000
pin102=1111
pin102=2222
pin103=3333
pin104=4444
pin105=5555
bal101=100000
bal102=200000
bal103=150000
bal103=175000
bal104=75000
bal105=125000
rem=0
x=0
y=0
z=0
amt1=0
amt2=0
amt3=0
ch=0
acc=0
f=open('templates/101.html','w')
message="<center>TYPE----AMOUNT----DEBIT/CREDIT----BALANCE</center><br>"
f.write(message)
f.close()
f=open('templates/102.html','w')
message="<center>TYPE----AMOUNT----DEBIT/CREDIT----BALANCE</center><br>"
f.write(message)
f.close()
f=open('templates/103.html','w')
message="<center>TYPE----AMOUNT----DEBIT/CREDIT----BALANCE</center><br>"
f.write(message)
f.close()
f=open('templates/104.html','w')
message="<center>TYPE----AMOUNT----DEBIT/CREDIT----BALANCE</center><br>"
f.write(message)
f.close()
f=open('templates/105.html','w')
message="<center>TYPE----AMOUNT----DEBIT/CREDIT----BALANCE</center><br>"
f.write(message)
f.close()
@app.route('/')                                       #WelcomeScreen
def Welcome():        
    return render_template('Welcome.html')
@app.route('/Admin')                                   #AdminPage
def Admin():          
    return render_template('Admin.html')
@app.route('/Admin/LoadMoney')
def load():
    return render_template('LoadMoney.html')
@app.route('/Load')
def Load():
    if 'den' in request.args:
        den=request.args['den']
    if 'qty' in request.args:
        qty=request.args['qty']
    LoadMoney(den,qty)
    return "Successfully Loaded to ATM"
def LoadMoney(den,qty):                                #AddStockFunction
    global twok,fiveh,h
    if den=='2000':
        twok+=int(qty)
    elif den=='500':
        fiveh+=int(qty)
    elif den=='100':
        h+=int(qty)
@app.route('/Admin/ViewMoney')
def view():
    global atm
    atm=(2000*twok)+(500*fiveh)+(100*h)
    load = open('templates/ViewMoney.html','w')
    txt= "<html><body><center><h1>Welcome</h1><br><h2>View Money Left</h2><br>2000      : "+str(twok)+"<br> 500 : "+str(fiveh)+"<br> 100  : "+str(h)+"<br> Net Amount : Rs."+str(atm)+"</center></body></html>"
    load.write(txt)
    load.close()
    return render_template('ViewMoney.html')
@app.route('/Admin/Details')
def details():
    detail = open('templates/Details.html','w')
    txt="<html><body><center><h1>Welcome</h1><br><h2>View Customer Details</h2><br>AccNum----AccHolder----PIN----AccBalance<br>"+str(p1)+"---p1---"+str(pin101)+"---Rs."+str(bal101)+"<br>"+str(p2)+"---p2---"+str(pin102)+"---Rs."+str(bal102)+"<br>"+str(p3)+"---p3---"+str(pin103)+"---Rs."+str(bal103)+"<br>"+str(p4)+"---p4---"+str(pin104)+"---Rs."+str(bal104)+"<br>"+str(p5)+"---p5---"+str(pin105)+"---Rs."+str(bal105)+"<br></center></body></html>"
    detail.write(txt)
    detail.close()
    return render_template('Details.html')
@app.route('/User')
def User():
    return render_template('User.html')
@app.route('/User/CheckBalance')
def CheckBalance():
    return render_template('CheckBalance.html')
@app.route('/Check')
def Check():
    if 'accnum' in request.args:
        accnum=request.args['accnum']
    if 'pin' in request.args:
        pin=request.args['pin']
    
    if accnum=='101':
        if pin=='1000':
            return "Your Account Balance is "+str(bal101)
        else:
            return "Incorrect PIN"
    if accnum=='102':
        if pin=='1111':
            return "Your Account Balance is "+str(bal102)
        else:
            return "Incorrect PIN"
    if accnum=='103':
        if pin=='2222':
            return "Your Account Balance is "+str(bal103)
        else:
            return "Incorrect PIN"
    if accnum=='104':
        if pin=='3333':
            return "Your Account Balance is "+str(bal104)
        else:
            return "Incorrect PIN"
    if accnum=='105':
        if pin=='4444':
            return "Your Account Balance is "+str(bal105)
        else:
            return "Incorrect PIN"
    
@app.route('/User/WithdrawMoney')
def WithdrawMoney():
    return render_template('WithdrawMoney.html')
@app.route('/Withdraw')
def Withdraw():
    if 'accnum' in request.args:
        accnum=request.args['accnum']
    if 'pin' in request.args:
        pin=request.args['pin']
    global acc
    if accnum=='101':
        if pin=='1000':
            acc=101
            return render_template('EnterAmount.html')
        else:
            return "Incorrect PIN"
    if accnum=='102':
        if pin=='1111':
            acc=102
            return render_template('EnterAmount.html')
        else:
            return "Incorrect PIN"
    if accnum=='103':
        if pin=='2222':
            acc=103
            return render_template('EnterAmount.html')
        else:
            return "Incorrect PIN"
    if accnum=='104':
        if pin=='3333':
            acc=104
            return render_template('EnterAmount.html')
        else:
            return "Incorrect PIN"
    if accnum=='105':
        if pin=='4444':
            acc=105
            return render_template('EnterAmount.html')
        else:
            return "Incorrect PIN"
@app.route('/WithdrawConfirm')
def confirm():
    if 'withdraw' in request.args:
        withdraw=request.args['withdraw']
    ch=(int(withdraw)%100)
    int(ch)
    global twok,fiveh,h,acc,bal101,bal102,bal103,bal104,bal105
    if ch==0:
        rem=int(withdraw)
        x=int(int(rem)/2000)
        if int(x)<int(twok):
            amt1=x*2000
            rem=rem-int(amt1)
        else:
            x=0
        y=int(int(rem)/500)
        if int(y)<int(fiveh):
            amt2=y*500
            rem=rem-int(amt2)
        else:
            y=0
        z=int(int(rem)/100)
        if int(z)<int(h):
            amt3=z*100
            rem=rem-int(amt3)
        else:
            z=0
        
        if rem==0:
            if acc==101:
                if int(withdraw)<=int(bal101):
                    twok=int(twok)-int(x)
                    fiveh=int(fiveh)-int(y)
                    h=int(h)-int(z)
                    bal101=int(bal101)-int(withdraw)
                    f=open('templates/101.html','a')
                    message="<center>Withdraw---Rs."+str(withdraw)+"---Debit---Rs."+str(bal101)+"</center><br>"
                    f.write(message)
                    f.close()
                    return "Transaction Done! Your Account Balance is Rs."+str(bal101)
                else:
                    return "No enough Money in Account"
            elif acc==102:
                if int(withdraw)<=int(bal102):
                    twok=int(twok)-int(x)
                    fiveh=int(fiveh)-int(y)
                    h=int(h)-int(z)
                    bal102=int(bal102)-int(withdraw)
                    f=open('templates/102.html','a')
                    message="<center>Withdraw---Rs."+str(withdraw)+"---Debit---Rs."+str(bal102)+"</center><br>"
                    f.write(message)
                    f.close()
                    return "Transaction Done! Your Account Balance is Rs."+str(bal102)
                else:
                    return "No enough Money in Account"
            elif acc==103:
                if int(withdraw)<=int(bal103):
                    twok=int(twok)-int(x)
                    fiveh=int(fiveh)-int(y)
                    h=int(h)-int(z)
                    bal103=int(bal103)-int(withdraw)
                    f=open('templates/103.html','a')
                    message="<center>Withdraw---Rs."+str(withdraw)+"---Debit---Rs."+str(bal103)+"</center><br>"
                    f.write(message)
                    f.close()
                    return "Transaction Done! Your Account Balance is Rs."+str(bal103)
                else:
                    return "No enough Money in Account"
            elif acc==104:
                if int(withdraw)<=int(bal104):
                    twok=int(twok)-int(x)
                    fiveh=int(fiveh)-int(y)
                    h=int(h)-int(z)
                    bal104=int(bal104)-int(withdraw)
                    f=open('templates/104.html','a')
                    message="<center>Withdraw---Rs."+str(withdraw)+"---Debit---Rs."+str(bal104)+"</center><br>"
                    f.write(message)
                    f.close()
                    return "Transaction Done! Your Account Balance is Rs."+str(bal104)
                else:
                    return "No enough Money in Account"
            elif acc==105:
                if int(withdraw)<=int(bal105):
                    twok=int(twok)-int(x)
                    fiveh=int(fiveh)-int(y)
                    h=int(h)-int(z)
                    bal105=int(bal105)-int(withdraw)
                    f=open('templates/105.html','a')
                    message="<center>Withdraw---Rs."+str(withdraw)+"---Debit---Rs."+str(bal105)+"</center><br>"
                    f.write(message)
                    f.close()
                    return "Transaction Done! Your Account Balance is Rs."+str(bal105)
                else:
                    return "No enough Money in Account"
        else:
            return "No enough Money in ATM. Try entering less Amount. Sorry for the Inconvenience."
    else:
        return "Enter in Multiple of 100"
@app.route('/User/TransferMoney')
def TransferMoney():
    return render_template('TransferMoney.html')
@app.route('/Transfer')
def Transfer():
    if 'accnum' in request.args:
        accnum=request.args['accnum']
    if 'pin' in request.args:
        pin=request.args['pin']
    global acc
    if accnum=='101':
        if pin=='1000':
            acc=101
            return render_template('Transfer.html')
        else:
            return "Incorrect PIN"
    if accnum=='102':
        if pin=='1111':
            acc=102
            return render_template('Transfer.html')
        else:
            return "Incorrect PIN"
    if accnum=='103':
        if pin=='2222':
            acc=103
            return render_template('Transfer.html')
        else:
            return "Incorrect PIN"
    if accnum=='104':
        if pin=='3333':
            acc=104
            return render_template('Transfer.html')
        else:
            return "Incorrect PIN"
    if accnum=='105':
        if pin=='4444':
            acc=105
            return render_template('Transfer.html')
        else:
            return "Incorrect PIN"
@app.route('/TransferConfirm')
def TransferConfirm():
    global acc,bal101,bal102,bal103,bal104,bal105
    if 'accnum1' in request.args:
        acc1=request.args['accnum1']
    if 'money' in request.args:
        money=request.args['money']
    if int(acc)==int(acc1):
        return "Sorry! Cannot Transfer to Same Account."
    if acc==101:
        if int(money)<=int(bal101):
            if acc1=='102':
                bal101=int(bal101)-int(money)
                bal102=int(bal102)+int(money)
                f=open('templates/101.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal101)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/102.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal102)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal101)
            if acc1=='103':
                bal101=int(bal101)-int(money)
                bal103=int(bal103)+int(money)
                f=open('templates/101.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal101)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/103.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal103)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal101)
            if acc1=='104':
                bal101=int(bal101)-int(money)
                bal104=int(bal104)+int(money)
                f=open('templates/101.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal101)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/104.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal104)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal101)
            if acc1=='105':
                bal101=int(bal101)-int(money)
                bal105=int(bal105)+int(money)
                f=open('templates/101.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal101)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/105.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal105)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal101)
        else:
            return "Sorry! Your Account does not have Sufficient Balance to do the Transaction."
    if acc==102:
        if int(money)<=int(bal102):
            if acc1=='101':
                bal102=int(bal102)-int(money)
                bal101=int(bal101)+int(money)
                f=open('templates/102.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal102)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/101.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal101)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal102)
            if acc1=='103':
                bal102=int(bal102)-int(money)
                bal103=int(bal103)+int(money)
                f=open('templates/102.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal102)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/103.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal103)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal102)
            if acc1=='104':
                bal102=int(bal102)-int(money)
                bal104=int(bal104)+int(money)
                f=open('templates/102.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal102)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/104.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal104)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal102)
            if acc1=='105':
                bal102=int(bal102)-int(money)
                bal105=int(bal105)+int(money)
                f=open('templates/102.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal102)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/105.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal105)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal102)
        else:
            return "Sorry! Your Account does not have Sufficient Balance to do the Transaction."
    if acc==103:
        if int(money)<=int(bal103):
            if acc1=='101':
                bal103=int(bal103)-int(money)
                bal101=int(bal101)+int(money)
                f=open('templates/103.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal103)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/101.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal101)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal103)
            if acc1=='102':
                bal103=int(bal103)-int(money)
                bal102=int(bal102)+int(money)
                f=open('templates/103.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal103)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/102.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal102)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal103)
            if acc1=='104':
                bal103=int(bal103)-int(money)
                bal104=int(bal104)+int(money)
                f=open('templates/103.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal103)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/104.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal104)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal103)
            if acc1=='105':
                bal103=int(bal103)-int(money)
                bal105=int(bal105)+int(money)
                f=open('templates/103.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal103)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/105.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal105)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal103)
        else:
            return "Sorry! Your Account does not have Sufficient Balance to do the Transaction."
    if acc==104:
        if int(money)<=int(bal104):
            if acc1=='101':
                bal104=int(bal104)-int(money)
                bal101=int(bal101)+int(money)
                f=open('templates/104.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal104)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/101.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal101)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal104)
            if acc1=='102':
                bal104=int(bal104)-int(money)
                bal102=int(bal102)+int(money)
                f=open('templates/104.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal104)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/102.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal102)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal104)
            if acc1=='103':
                bal104=int(bal104)-int(money)
                bal103=int(bal103)+int(money)
                f=open('templates/104.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal104)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/103.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal103)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal104)
            if acc1=='105':
                bal104=int(bal104)-int(money)
                bal105=int(bal105)+int(money)
                f=open('templates/104.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal104)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/105.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal105)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal104)
        else:
            return "Sorry! Your Account does not have Sufficient Balance to do the Transaction."
    if acc==105:
        if int(money)<=int(bal105):
            if acc1=='101':
                bal105=int(bal105)-int(money)
                bal101=int(bal101)+int(money)
                f=open('templates/105.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal105)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/101.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal101)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal105)
            if acc1=='102':
                bal105=int(bal105)-int(money)
                bal102=int(bal102)+int(money)
                f=open('templates/105.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal105)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/102.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal102)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal105)
            if acc1=='103':
                bal105=int(bal105)-int(money)
                bal103=int(bal103)+int(money)
                f=open('templates/105.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal105)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/103.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal103)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal105)
            if acc1=='104':
                bal105=int(bal105)-int(money)
                bal104=int(bal104)+int(money)
                f=open('templates/105.html','a')
                message="<center>Transfer to "+str(acc1)+"---Rs."+str(money)+"---Debit---Rs."+str(bal105)+"</center><br>"
                f.write(message)
                f.close()
                f=open('templates/104.html','a')
                message="<center>Transfer from "+str(acc)+"---Rs."+str(money)+"---Credit---Rs."+str(bal104)+"</center><br>"
                f.write(message)
                f.close()
                return "Successfully transferred Money!! Your Current Account Balance is Rs."+str(bal105)
        else:
            return "Sorry! Your Account does not have Sufficient Balance to do the Transaction."
        
@app.route('/User/MiniStatement')
def MiniStatement():
    return render_template('MiniStatement.html')
@app.route('/MiniStatement')
def Statement():
    if 'accnum' in request.args:
        accnum=request.args['accnum']
    if 'pin' in request.args:
        pin=request.args['pin']
    global acc
    if accnum=='101':
        if pin=='1000':
            return render_template('101.html')
        else:
            return "Incorrect PIN"
    if accnum=='102':
        if pin=='1111':
            return render_template('102.html')
        else:
            return "Incorrect PIN"
    if accnum=='103':
        if pin=='2222':
            return render_template('103.html')
        else:
            return "Incorrect PIN"
    if accnum=='104':
        if pin=='3333':
            return render_template('104.html')
        else:
            return "Incorrect PIN"
    if accnum=='105':
        if pin=='4444':
            return render_template('105.html')
        else:
            return "Incorrect PIN"


if __name__ =="__main__":
            app.run(host='0.0.0.0',threaded=True)
            
