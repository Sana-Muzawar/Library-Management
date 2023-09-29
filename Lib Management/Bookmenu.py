
import Books
import Bookuser
import Bookissue
import pyttsx3
engine=pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty('voice',sound[1].id)

def book():
    while True:
        print("*"*50)
        print('****** BOOK DETAILS MENU ******')
        print("*"*50)
        print('1.Adding more books')
        print('2.Removing books')
        print('3.Display books')
        print('4.Search book')
        print('5.Update book')
        print('6.Return to main menu')
        print("*"*50)
        engine.say('Enter your choice from Book details menu')
        engine.runAndWait()
        ch=int(input('Enter your choice from book details menu: '))
        print("*"*50)
        if ch==1:
            Books.addbook()
        elif ch==2:
            Books.deletebook()
        elif ch==3:
            Books.displaybook()
        elif ch==4:
            Books.searchbook()
        elif ch==5:
            Books.updatebook()
        elif ch==6:
            break
        else:
            engine.say('Press any key to go back to menu')
            engine.runAndWait()
            print('Press any key to go back to menu')
            cho=input('Enter choice:')


def user():
    while True:
        print("*"*50)
        print('****** USER DETAILS MENU ******')
        print("*"*50)
        print('1.Add user')
        print('2.Display details')
        print('3.Search')
        print('4.Update')
        print('5.Delete')
        print('6.Return to main menu')
        print("*"*50)
        engine.say('Enter your choice from user details menu')
        engine.runAndWait()
        ch=int(input('Enter your choice from user details menu: '))
        print("*"*50)
        if ch==1:
            Bookuser.adduser()
        elif ch==2:
            Bookuser.display()
        elif ch==3:
            Bookuser.search()
        elif ch==4:
            Bookuser.update()
        elif ch==5:
            Bookuser.delete()
        elif ch==6:
            break
        else:
            engine.say('Wrong choice entered')
            engine.runAndWait()
            print('Wrong choice entered')


def issue():
    while True:
        print("*"*50)
        print('****** ISSUE BOOK MENU ******')
        print("*"*50)
        print('1.Issue book')
        print('2.Search person details')
        print('3.Return books')
        print('4.Update books')
        print('5.Return to main menu')
        print("*"*50)
        engine.say('Enter your choice from issue book menu')
        engine.runAndWait()
        ch=int(input('Enter your choice from issue book menu: '))
        print("*"*50)
        if ch==1:
            Bookissue.issue()
        elif ch==2:
            Bookissue.search()
        elif ch==3:
            Bookissue.returnbook()
        elif ch==4:
            Bookissue.updatebook()
        elif ch==5:
            break
        else:
            engine.say('Wrong choice entered')
            engine.runAndWait()
            print('Wrong choice entered')






    
        
