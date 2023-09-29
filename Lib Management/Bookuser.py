
import pyttsx3
engine=pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty('voice',sound[1].id)

def tableuser():
    import mysql.connector as db
    con=db.connect(host='localhost',user='root',passwd='shifa3')
    cur=con.cursor()
    cur.execute('use project')
    q="create table if not exists User(Uid char(5), Name varchar(30), Pno varchar(15), city varchar(25), email_ID varchar(40))"
    cur.execute(q)

def adduser():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    tableuser()
    cursor.execute("select * from User")
    r=cursor.fetchall()
    engine.say('Enter User ID')
    engine.runAndWait()
    Uid=input("Enter User ID: ")
    rec=(Uid,)
    for i in r:
        if i[0]==rec[0]:
            engine.say('ID already exists')
            engine.runAndWait()
            print("ID already exists")
            break
    else:
        engine.say('Enter User name')
        engine.runAndWait()
        Name=input('Enter user name:')
        engine.say('Enter Phone number')
        engine.runAndWait()
        Pno=input('Enter phone no. :')
        engine.say('Enter city')
        engine.runAndWait()
        city=input('Enter city:')
        engine.say('Enter email ID')
        engine.runAndWait()
        email=input('Enter email ID:')
        A="insert into User values('{}','{}','{}','{}','{}')".format(Uid,Name,Pno,city,email)
        cursor.execute(A)
        mydb.commit()
        engine.say('User details added')
        engine.runAndWait()
        print("User details added!")


def display():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    cursor.execute("select * from User")
    d=cursor.fetchall()
    for i in d:
        print(i)


def search():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    engine.say('Enter User ID to be searched')
    engine.runAndWait()
    Uid=input('Enter User ID to be searched:')
    q="select * from User where Uid='{}'".format(Uid)
    cursor.execute(q)
    d=cursor.fetchone()
    if d!=None:
        print(d)
        print("\n")
    else:
        engine.say('Sorry! No such User ID exists.')
        engine.runAndWait()
        print('Sorry! No such User ID exists.')



def update():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    while True:
        print("*"*50)
        engine.say('User details')
        engine.runAndWait()
        print("\t\tUser Details")
        print("*"*50)
        print("1.Name")
        print("2.Phone number")
        print("3.City")
        print("4.Email ID")
        print("5.Exit")
        print("*"*50)
        engine.say('Enter the choice to be modified')
        engine.runAndWait()
        x=int(input("Enter the choice to be modified:"))
        print("*"*50)
        engine.say('Updation will be done only when you will provide user ID')
        engine.runAndWait()
        print("NOTE- Updation will be done only when you will provide user ID")
        if x==1:
            engine.say('Enter User ID')
            engine.runAndWait()
            u=input("Enter user ID:")
            engine.say('Enter name to be modified')
            engine.runAndWait()
            name=input("Enter name to be modified:")
            q="update User set Name='{}' where Uid='{}'".format(name,u)
            cursor.execute(q)
            mydb.commit()
            engine.say('Data modified')
            engine.runAndWait()
            print("Data modified!")
        if x==2:
            engine.say('Enter User ID')
            engine.runAndWait()
            u=input("Enter user ID:")
            engine.say('Enter phone number to be modified')
            engine.runAndWait()
            Pno=input("Enter phone no. to be modified:")
            q="update User set Pno='{}' where Uid='{}'".format(Pno,u)
            cursor.execute(q)
            mydb.commit()
            engine.say('Data modified')
            engine.runAndWait()
            print("Data modified!")
        if x==3:
            engine.say('Enter User ID')
            engine.runAndWait()
            u=input("Enter user ID:")
            engine.say('Enter city to be modified')
            engine.runAndWait()
            city=input("Enter city to be modified:")
            q="update User set city='{}' where Uid='{}'".format(city,u)
            cursor.execute(q)
            mydb.commit()
            engine.say('Data modified')
            engine.runAndWait()
            print("Data modified!")
        if x==4:
            engine.say('Enter User ID')
            engine.runAndWait()
            u=input("Enter user ID:")
            engine.say('Enter email ID to be modified')
            engine.runAndWait()
            email=input("Enter email ID to be modified:")
            q="update User set email_ID='{}' where Uid='{}'".format(email,u)
            cursor.execute(q)
            mydb.commit()
            engine.say('Data modified')
            engine.runAndWait()
            print("Data modified!")
        if x==5:
            break


def delete():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    engine.say('Enter User ID whose detail has to be deleted')
    engine.runAndWait()
    u=input('Enter User ID whose detail has to be deleted:')
    q="delete from User where Uid='{}'".format(u)
    cursor.execute(q)
    mydb.commit()
    engine.say('Data deleted')
    engine.runAndWait()
    print("Data deleted!")

    
    
    
    





    
