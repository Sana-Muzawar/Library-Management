
import mysql.connector as db
import pyttsx3
engine=pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty('voice',sound[1].id)
                   
def tableissue():
    con=db.connect(host='localhost',user='root',passwd='shifa3')
    cur=con.cursor()
    cur.execute('use project')
    cur.execute('create table if not exists Issue(Bid char(5), Bname varchar(30), Uid char(5), qty int(4))')

def issue():
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    tableissue()
    qty="select Uid,sum(qty) from Issue group by Uid"
    cursor.execute(qty)
    r=cursor.fetchall()
    engine.say('Enter User ID')
    engine.runAndWait()
    Uid=input('Enter user ID:')
    rec=(Uid,)
    for i in r:
        if i[0]==rec[0]:
            if i[1]>1:
                engine.say('First return the book')
                engine.runAndWait()
                print("First return the book")
    else:
        engine.say('Reissue the book')
        engine.runAndWait()
        print("Reissue the book")
        print("*"*50)
        engine.say('Enter Book ID')
        engine.runAndWait()
        bid=input('Enter Book ID:')
        engine.say('Enter Book Name')
        engine.runAndWait()
        bname=input('Enter Book Name:')
        engine.say('Enter user ID')
        engine.runAndWait()
        Uid=input('Enter user ID:')
        engine.say('Enter quantity of the book issued:')
        engine.runAndWait()
        qty=int(input('Enter quantity of the book issued:'))
        print("~"*60)
        e="insert into Issue values('{}','{}','{}',{})".format(bid,bname,Uid,qty)
        cursor.execute(e)
        mydb.commit()
        print("**********  INFORMATION ADDED  **********")
        engine.say('Information added')
        engine.runAndWait()


def search():
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    engine.say('Enter user ID')
    engine.runAndWait()
    Uid=input('Enter user ID:')
    a="select * from Issue where Uid='{}'".format(Uid)
    cursor.execute(a)
    b=cursor.fetchone()
    if b!=None:
        print(b)
        print("\n")
    else:
        engine.say('Sorry! No such User ID exists.')
        engine.runAndWait()
        print('Sorry! No such User ID exists.')


def returnbook():
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    engine.say('Enter Book ID')
    engine.runAndWait()
    bid=input('Enter book ID:')
    engine.say('Enter user ID')
    engine.runAndWait()
    Uid=input('Enter user ID:')
    engine.say('Enter the quantity of book')
    engine.runAndWait()
    qty=int(input('Enter the quantity of book:'))
    rec=(bid,Uid,qty)
    cursor.execute("select * from Issue")
    r=cursor.fetchall()
    for i in r:
        if i[0]==rec[0] and i[2]==rec[1]:
            q="update Issue set qty={} where Bid='{}' and Uid='{}'".format(i[3]-qty,i[0],i[2])
            cursor.execute(q)
            mydb.commit()
            print("Updated issue details")
            break
    else:
        engine.say('ID not found')
        engine.runAndWait()
        print("ID Not found!")
        


def updatebook():
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    
    def updateissue():
        engine.say('Enter Book ID')
        engine.runAndWait()
        bid=input('Enter book ID:')
        engine.say('Enter the quantity of book')
        engine.runAndWait()
        qty=int(input('Enter the quantity of book:'))
        rec=(bid,qty,)
        cursor.execute("select * from Library")
        r=cursor.fetchall()
        for i in r:
            if i[0]==rec[0]:
                q="update Library set qty={} where bid='{}'".format(i[3]-qty,i[0])
                cursor.execute(q)
                mydb.commit()
                engine.say('Updated details')
                engine.runAndWait()
                print("Updated details")
                break


    def updatereturn():
        engine.say('Enter Book ID')
        engine.runAndWait()
        bid=input('Enter book ID:')
        engine.say('Enter the quantity of book')
        engine.runAndWait()
        qty=int(input('Enter the quantity of book:'))
        rec=(bid,qty,)
        cursor.execute("select * from Library")
        r=cursor.fetchall()
        for i in r:
            if i[0]==rec[0]:
                q="update Library set qty={} where bid='{}'".format(i[3]+qty,i[0])
                cursor.execute(q)
                mydb.commit()
                engine.say('Updated details')
                engine.runAndWait()
                print("Updated details")
                break


        
    while True:
        print("1.Update Book while issue book")
        print("2.Update Book while return book")
        print("3.EXIT")
        engine.say('Enter your choice')
        engine.runAndWait()
        ch=int(input("****** Enter your choice ******:"))
        if ch==1:
            updateissue()
        elif ch==2:
            updatereturn()
        elif ch==3:
            break
        else:
            engine.say('Wrong choice entered')
            engine.runAndWait()
            print('Wrong choice entered!')

            










    
                
    
