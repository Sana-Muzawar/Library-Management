
import Bookmenu
import pyttsx3
engine=pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty('voice',sound[1].id)

engine.say('Welcome to my Library!')
engine.runAndWait()
while True:
    print('********** MAIN MENU **********')
    print('1.BOOK DETAILS MENU')
    print('2.USER DETAILS MENU')
    print('3.BOOK ISSUE AND RETURN BOOK MENU')
    print('4.EXIT')
    engine.say('Enter choice from MAIN MENU : ')
    engine.runAndWait()
    ch=int(input('Enter choice from MAIN MENU : '))
    if ch==1:
        Bookmenu.book()
    elif ch==2:
        Bookmenu.user()
    elif ch==3:
        Bookmenu.issue()
    elif ch==4:
        break
    else:
        engine.say('Wrong choice entered')
        engine.runAndWait()
        print('Wrong choice entered')

engine.say("Thank You For using Library!")
engine.runAndWait()    
print('Thank You For using Library!')




















    
        
