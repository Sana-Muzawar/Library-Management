
import pyttsx3
engine=pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty('voice',sound[1].id)


def createtable():
    import mysql.connector as db
    con=db.connect(host='localhost',user='root',passwd='shifa3')
    cur=con.cursor()
    cur.execute('use project')
    cur.execute('create table if not exists Library(bid char(5), name varchar(30), author varchar(25), qty int(4))')


def addbook():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    print("*"*50)
    createtable()
    engine.say('Enter Book ID')
    engine.runAndWait()
    bid=input('Enter book ID:')
    engine.say('Enter Book name')
    engine.runAndWait()
    name=input('Enter book name:')
    engine.say('Enter name of the author')
    engine.runAndWait()
    author=input('Enter name of the author:')
    engine.say('Enter the quantity of book')
    engine.runAndWait()
    qty=int(input('Enter the quantity of book:'))
    rec=(bid,name,author,qty)
    cursor.execute('select * from Library')
    r=cursor.fetchall()

    for i in r:
        if i[0]==rec[0] and i[1]==rec[1]:
            query="update Library set qty={} where bid='{}'".format(i[3]+qty,i[0])
            cursor.execute(query)
            mydb.commit()
            engine.say('Books added')
            engine.runAndWait()
            print('Books added!')
            break
        elif i[0]==rec[0] and i[1]!=rec[1]:
            print('Book ID already exists but you entered wrong Book name')
        elif i[0]!=rec[0] and i[1]==rec[1]:
            print('Wrong Book ID entered!')
            break
        
    else:
        if i[0]!=rec[0] and i[1]!=rec[1]:
            q="insert into Library values('{}','{}','{}',{})".format(bid,name,author,qty)
            cursor.execute(q)
            mydb.commit()
            engine.say('New book records added!')
            engine.runAndWait()
            print('New book records added!')
            print("*"*50)



def displaybook():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    cursor.execute('select * from Library')
    r=cursor.fetchall()
    for i in r:
        print(i)
    print('-'*100)


def deletebook():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    print("*"*60)
    print("1.Book name")
    print("2.Book ID")
    print("#"*50)
    ch=int(input("Enter your choice:"))
    if ch==1:
        engine.say('Enter book name that you want to delete')
        engine.runAndWait()
        x=input('Enter book name that you want to delete:')
        y='delete from Library where name="{}"'.format(x)
        cursor.execute(y)
        mydb.commit()
    elif ch==2:
        engine.say('Enter book ID that you want to delete')
        engine.runAndWait()
        x=input('Enter book ID that you want to delete:')
        y='delete from Library where bid="{}"'.format(x)
        cursor.execute(y)
        mydb.commit()
    else:
        engine.say('Wrong input')
        engine.runAndWait()
        print("Wrong input")
    engine.say('Deleted')
    engine.runAndWait()
    print('Deleted')
    print("*"*50)


def updatebook():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    print("-"*50)
    print('****** MENU for modification of book details ******')
    print("\n")
    print('1.Book ID')
    print('2.Book name')
    print('3.Author name')
    print('4.Book quantity')
    print("-"*60)
    ch1=input('Enter your choice which you want to modify from above menu:')
    ch2=input('Enter option to be modified on the basis of:')
    if ch1=='1':
        if ch2=='1':
            print("\n")
            x=input('Enter new Book ID to be added:')
            z=input('Enter Book ID to be removed:')
            y='update Library set bid="{}" where bid="{}"'.format(x,z)
        elif ch2=='2':
            print("\n")
            x=input('Enter new Book ID:')
            z=input('Enter Book Name whose ID has to be changed:')
            y='update Library set bid="{}" where name="{}"'.format(x,z)
        elif ch2=='3':
            print("\n")
            x=input('Enter new Book ID:')
            z=input('Enter Author Name whose ID has to be changed:')
            y='update Library set bid="{}" where author="{}"'.format(x,z)
        elif ch2=='4':
            print("\n")
            x=input('Enter new Book ID:')
            z=input('Enter Book Quantity whose ID has to be changed:')
            y='update Library set bid="{}" where qty={}'.format(x,z)
    elif ch1=='2':
        if ch2=='1':
            print("\n")
            x=input('Enter new Book Name:')
            z=input('Enter Book ID whose Name has to be changed:')
            y='update Library set name="{}" where bid="{}"'.format(x,z)
        elif ch2=='2':
            print("\n")
            x=input('Enter new Book Name:')
            z=input('Enter Book Name to be removed:')
            y='update Library set name="{}" where name="{}"'.format(x,z)
        elif ch2=='3':
            print("\n")
            x=input('Enter new Book Name:')
            z=input('Enter Author Name whose Book Name has to be changed:')
            y='update Library set name="{}" where author="{}"'.format(x,z)
        elif ch2=='4':
            print("\n")
            x=input('Enter new Book Name:')
            z=input('Enter Book Quantity whose Book Name has to be changed:')
            y='update Library set name="{}" where qty={}'.format(x,z)
    elif ch1=='3':
        if ch2=='1':
            print("\n")
            x=input('Enter new Author Name:')
            z=input('Enter Book ID whose Author Name has to be changed:')
            y='update Library set author="{}" where bid="{}"'.format(x,z)
        elif ch2=='2':
            print("\n")
            x=input('Enter new Author Name:')
            z=input('Enter Book Name whose Author Name has to be changed:')
            y='update Library set author="{}" where name="{}"'.format(x,z)
        elif ch2=='3':
            print("\n")
            x=input('Enter new Author Name:')
            z=input('Enter Author Name to be removed:')
            y='update Library set author="{}" where author="{}"'.format(x,z)
        elif ch2=='4':
            print("\n")
            x=input('Enter new Author Name:')
            z=input('Enter Book Quantity whose Author Name has to be changed:')
            y='update Library set author="{}" where qty={}'.format(x,z)
    elif ch1=='4':
        if ch2=='1':
            print("\n")
            x=input('Enter new Book Quantity:')
            z=input('Enter Book ID whose Book Quantity has to be changed:')
            y='update Library set qty={} where bid="{}"'.format(x,z)
        elif ch2=='2':
            print("\n")
            x=input('Enter new Book Quantity:')
            z=input('Enter Book Name whose Book Quantity has to be changed:')
            y='update Library set qty={} where name="{}"'.format(x,z)
        elif ch2=='3':
            print("\n")
            x=input('Enter new Book Quantity:')
            z=input('Enter Author Name whose Book Quantity has to be changed:')
            y='update Library set qty={} where author="{}"'.format(x,z)
        elif ch2=='4':
            print("\n")
            x=input('Enter new Book Quantity:')
            z=input('Enter Book Quantity to be removed:')
            y='update Library set qty={} where qty={}'.format(x,z)
    cursor.execute(y)
    mydb.commit()
    print('Record Updated')


def searchbook():
    import mysql.connector as db
    mydb=db.connect(host='localhost', user='root', passwd='shifa3', database='project')
    cursor=mydb.cursor()
    Q="select * from Library"
    cursor.execute(Q)
    rec=cursor.fetchall()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('********** SEARCH MENU **********')
    print('1.Book ID')
    print('2.Book Name')
    print('3.Author Name')
    print('\n')
    engine.say('Enter your choice from Search menu')
    engine.runAndWait()
    ch=input('Enter your choice from search menu:')
    if ch=='1':
        engine.say('Enter Book ID to be searched')
        engine.runAndWait()
        bid=input('Enter Book ID to be searched:')
        y="select * from Library where bid='{}'".format(bid)
        cursor.execute(y)
        r=cursor.fetchone()
        if r!=None:
            print(r)
        else:
            engine.say('ID Not Found!')
            engine.runAndWait()
            print("ID Not Found!")
                
    elif ch=='2':
        engine.say('Enter Book Name to be searched')
        engine.runAndWait()
        name=input('Enter Book Name to be searched:')
        y="select * from Library where name='{}'".format(name)
        cursor.execute(y)
        r=cursor.fetchone()
        if r!=None:
            print(r)
        else:
            engine.say('Name Not Found!')
            engine.runAndWait()
            print("Name Not Found!")
            
    elif ch=='3':
        engine.say('Enter Author Name to be searched')
        engine.runAndWait()
        author=input('Enter Author Name to be searched:')
        y="select * from Library where author='{}'".format(author)
        cursor.execute(y)
        r=cursor.fetchone()
        if r!=None:
            print(r)
        else:
            engine.say('Author Not Found!')
            engine.runAndWait()
            print("Author Not Found!")

    else:
        print('Wrong choice entered')



            
            
        



            
