# Final Project: CS Time Management Quiz Game
# CS 111, Hayes & Reckinger
# Zaid Haidry & Haider Bakhtiari
# Citations:
    #"arc.gif": https://pspm.uic.edu/planning-design/campus-architecture-and-learning-environments/classrooms/completed-east-campus-classroom-projects/
    #'calendar.gif': https://pspm.uic.edu/planning-design/campus-architecture-and-learning-environments/classrooms/completed-east-campus-classroom-projects/
    #'code.gif': https://www.lifewire.com/what-is-binary-and-how-does-it-work-4692749
    #'failed.gif':  https://backgroundlabs.com/failed-background/
    #'party.gif': https://creazilla.com/nodes/58253-party-popper-emoji-clipart
    #'partner.gif':https://www.alamy.com/stock-photo-depth-of-field-on-hand-drawn-project-presentation-on-blue-background-146917617.html?imageid=49C208F1-726A-415E-95EB-614CC9848495&p=149902&pn=1&searchId=c6343b75e6d0dc77a7208f7978020d60&searchtype=0
    #'person.gif': https://creazilla.com/nodes/7810339-man-pixel-art-clipart
    #'results.gif':https://deltacofranchise.com/hubfs/Franchise%20Fee%20Royalties%20What%20Do%20I%20Get%20in%20Return.png
    #'startbutton.gif': https://www.clker.com//cliparts/W/Z/O/i/x/H/start-hi.png
    #'tv1.gif': https://as2.ftcdn.net/v2/jpg/05/62/89/49/1000_F_562894938_QSc1V1soZOVP1zAK7QhAPtns5KyAapOq.jpg
    #'uic_banner.gif': https://www.pepperconstruction.com/sites/default/files/images/uic_banner.jpg
    #'test.gif': https://www.alamy.com/word-exam-made-of-letters-and-stationery-on-wooden-background-image256509147.html
    #'exam.gif': https://static.vecteezy.com/system/resources/previews/007/978/235/non_2x/close-up-and-top-view-of-answers-sheet-with-blue-sharp-pencil-in-hand-and-rubber-isolated-on-white-background-top-view-of-them-take-the-exam-timely-concept-selective-focus-free-photo.JPG
    #'scenario3.gif': https://cdn.pixabay.com/photo/2016/12/15/14/32/question-mark-background-1909040_1280.png

    #Program that uses Turtle graphics to test a user's observation skills on 7 different scenarios with 3 different options ranging from: poor, okay, and excellent. The user will be able to control a character using their arrow keys and moving the character to the option. A score would be stored for each option chosen and the user will receive an estimated outcome of their performance of the class. These outcomes are determined by the text file of "scores.txt".






import turtle
import random

#global variables used throughout the program
global score #score keeps track of the user's score after each choice is made
global notStarted #determines if the a button is clicked or not
global pros #pros is a string that includes the pros of each option chosen by the user
global cons #cons is a string that includes the cons of each option chosen by the user
#checked(1-7) variables are booleans that determine if a option in each scenario(1-7) is chosen.
global checked1
global checked2
global checked3
global checked4
global checked5
global checked6
global checked7

global cheat1 #determines if a certain option is chosen which would skip to the results screen
global pass1 #bool needed to double check if a scenario was checked or not so the check function would not be repeated
global colors #list of colors

colors = ['green', 'red', 'blue', 'yellow', 'pink', 'purple']

#making all checked variables false because check() functions were not used yet
checked1 = False
checked2 = False
checked3 = False
checked4 = False
checked5 = False
checked6 = False
checked7 = False

#pass1 is true because check() function is not used yet
pass1=True

pros = str()
cons = str()

score = 0

#function delete_extra removes any extra new line characters in a list, takes a list as a parameter
def delete_extra(list1):
    new_list = list()
    for i in range(len(list1)):
        new_list.append(list1[i].strip()) #uses strip() to remove new line characters and adds it to a new list
    return new_list 

#import data from scores.txt
score_file = open('scores.txt') 
score_file = score_file.readlines() #reads every line in text file
scores = list()
score_data = list()
outcomes = dict()
for i in range(len(score_file)):
    new_line = score_file[i].split(',') #creating a list for each line, seperating the score and the outcome
    scores.append(new_line) #adding each list to a new list
for i in range(len(scores)):
    score1 = scores[i][0] #storing the zero index(the number) as the score
    outcome = scores[i][1] #storing the first index(the outcome) as the outcome
    outcomes.update({score1: outcome.strip()}) #storing both elements of each line as a key and value in a dictionary named outcomes


#confetti() function creates rectangles with different colors and gets drawn in random spots throughout the last screen
def confetti():
    global colors
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    for i in range(50):
        t.color(colors[random.randint(0, len(colors)- 1)]) #choosing a random color from colors list
        #random number for each coordinate(x,y)
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        t.goto(x,y)
        #draws square
        t.speed(50)
        t.pendown()
        t.forward(6)
        t.right(90)
        t.forward(2)
        t.right(90)
        t.forward(6)
        t.right(90)
        t.forward(2)
        t.penup()
    t.hideturtle()



#nextbutton() imports a gif that is used for the user to click to move on to the next screen
def nextbutton():
    next1 = turtle.Turtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)

#up() function moves person.gif up on the screen
def up():
    global score
    global checked1
    global checked2
    global checked3
    global checked4
    global checked5
    global checked6 
    person.setheading(90) #sets the person to face 90 degrees
    person.forward(10) #moves person forward
    if pass1: #double checks if a check() function was completed or not
        if checked1 == False:
            check()
        elif checked1 == True: #only runs if the previous check() function was completed, same for the rest
            if checked2 == False:
                check2()
            elif checked2 == True:
                if checked3 == False:
                    check3()
                elif checked3 == True:
                    if checked4 == False:
                        check4()
                    elif checked4 == True:
                        if checked5 == False:
                            check5()
                        elif checked5 == True:
                            if checked6 == False:
                                check6()
                            elif checked6 == True:
                                if checked7 == False:
                                    check7()

#left() function moves person.gif left on the screen
def left():
    global score
    global checked1
    global checked2
    global checked3
    global checked4
    global checked5
    global checked6 
    global pass1
    person.setheading(180) #sets the person to face 180 degrees
    person.forward(10)
    if pass1:
        if checked1 == False:
            check()
        elif checked1 == True:
            if checked2 == False:
                check2()
            elif checked2 == True:
                if checked3 == False:
                    check3()
                elif checked3 == True:
                    if checked4 == False:
                        check4()
                    elif checked4 == True:
                        if checked5 == False:
                            check5()
                        elif checked5 == True:
                            if checked6 == False:
                                check6()
                            elif checked6 == True:
                                if checked7 == False:
                                    check7()
#down() function moves person.gif down on the screen
def down():
    global score
    global checked1
    global checked2
    global checked3
    global checked4
    global checked5
    global checked6 
    person.setheading(270) #sets the person to face 270 degrees
    person.forward(10)
    if pass1:
        if checked1 == False:
            check()
        elif checked1 == True:
            if checked2 == False:
                check2()
            elif checked2 == True:
                if checked3 == False:
                    check3()
                elif checked3 == True:
                    if checked4 == False:
                        check4()
                    elif checked4 == True:
                        if checked5 == False:
                            check5()
                        elif checked5 == True:
                            if checked6 == False:
                                check6()
                            elif checked6 == True:
                                if checked7 == False:
                                    check7()
#right() function moves person.gif right on the screen
def right():
    global score
    global checked1
    global checked2
    global checked3
    global checked4
    global checked5
    global checked6
    person.setheading(0) #sets the person to face 0 degrees
    person.forward(10)
    if pass1:
        if checked1 == False:
            check()
        elif checked1 == True:
            if checked2 == False:
                check2()  
            elif checked2 == True:
                if checked3 == False:
                    check3()
                elif checked3 == True:
                    if checked4 == False:
                        check4()         
                    elif checked4 == True:
                        if checked5 == False:
                            check5()                            
                        elif checked5 == True:
                            if checked6 == False:
                                check6()
                            elif checked6 == True:
                                if checked7 == False:
                                    check7()

#start() function determines if a certain button was clicked or not
def start(x, y):
    global notStarted
    notStarted = False
#check() determines if a person interacted with a option on the screen
#code is similar from (check() to check7())
def check():
    global score
    global checked1
    global pass1
    global pros
    global cons
    if (person.distance(option1.xcor(), option1.ycor()) < 200): #determines if the person has intereacted with the first option
        checked1 = True #declares that the check() function is completed
        score += 3 #adds on to the score
        pass1 = False #makes sure this check() function is not repeated
        option1.hideturtle() #removes the option
        next1.showturtle() #shows the next button
        #concatenates a string to 'pros' variable showing what was good about this option
        pros += 'QUESTION 1: Reading the syllabus thoroughly helped you.\n' 
        pros += 'gain a clear understanding of the course. \n'
        pros += '\n'
    elif (person.distance(option2.xcor(), option2.ycor()) < 200):#determines if the person has intereacted with the second option
        checked1 = True
        score += 2
        pass1= False
        option2.hideturtle()
        next1.showturtle()
        pros += 'QUESTION 1: Only listening to the teacher talk about the syllabus will get you some understanding of the course. \n'
        #concatenates a string to 'cons' variable showing what was bad about this option
        cons += 'QUESTION 1: Only listening to the teacher talk will lead you to miss out on some information that will be beneficial to you for the course. \n'
        pros += '\n'
        cons += '\n'
    elif (person.distance(option3.xcor(), option3.ycor()) < 200): #determines if the person has intereacted with the third option
        checked1 = True
        score += 1
        pass1= False
        option3.hideturtle()
        next1.showturtle()
        cons += 'QUESTION 1: Not reading or listening to the teacher at all will not help you understand the course and will make you miss out on a lot of important info.\n'
        cons += '\n'
def check2():
    global score
    global checked2
    global pass1
    global pros
    global cons
    pass1 = True 
    if (person.distance(option1.xcor(), option1.ycor()) < 200):
        checked2 = True
        score += 3
        pass1 = False
        option1.hideturtle()
        next1.showturtle()
        pros += 'QUESTION 2: Starting early on the project will give you enough time to work on the project and possibly allow you to earn extra credit for early submission.\n'
        pros += '\n'
    elif (person.distance(option2.xcor(), option2.ycor()) < 200):
        checked2 = True
        score += 2
        pass1 = False
        option2.hideturtle()
        next1.showturtle()
        pros += 'QUESTION 2: Starting a week after on the project will give you a little bit of time to work on it and get help.\n'
        cons += 'QUESTION 2: Starting a week after will make you rush and it will be tough getting help since office hours would be busy.\n'
        pros += '\n'
        cons += '\n'
    elif (person.distance(option3.xcor(), option3.ycor()) < 200):
        checked2 = True
        score += 1
        pass1 = False
        option3.hideturtle()
        next1.showturtle()
        cons += "QUESTION 2: Waiting until the last day to work on the project is not a good idea because there is a high chance that \n"
        cons +=  "you will not have enough time to finish and you will be behind.\n"
        cons += '\n'
    
def check3():
    global score
    global checked3
    global pass1
    global pros
    global cons
    global cheat1
    cheat1 = False
    pass1 = True
    if (person.distance(option1.xcor(), option1.ycor()) < 200):
        checked3 = True
        score += 3
        pass1 = False
        option1.hideturtle()
        next1.showturtle()
        pros += "QUESTION 3: Going to office hours will allow you to fix your problem immediately and will assure you that you won't be behind.\n"
        cons += '\n'
    elif (person.distance(option2.xcor(), option2.ycor()) < 200):
        checked3 = True
        score += 2
        pass1 = False
        option2.hideturtle()
        next1.showturtle()
        pros += 'QUESTION 3: Waiting for the last 2 days for the TA Zoom calls will help you fix your problem in the milestone. \n'
        cons += 'QUESTION 3: Watiing for the last 2 days for the TA Zoom calls is not a good idea because the Zoom calls would be busy and you \n'
        cons += 'would have to wait. \n'
        pros += '\n'
        cons += '\n'
    elif (person.distance(option3.xcor(), option3.ycor()) < 200):
        cheat1 = True #cheat1 is True here because this is a unique option that ends the game
        checked3 = True
        score += 1
        pass1 = False
        option3.hideturtle()
        next1.showturtle()
        cons += "QUESTION 3: You cheated on the exam and you got caught and now you have to face bigger penalties.\n"
        cons += '\n'

def check4():
    global score
    global checked4
    global pass1
    global pros
    global cons
    pass1 = True
    if (person.distance(option1.xcor(), option1.ycor()) < 200):
        checked4 = True
        score += 3
        pass1 = False
        next1.showturtle()
        option1.hideturtle()
        pros += 'QUESTION 4: Making a planner 2 weeks before the exam will allow you to undestand more concepts and be more prepared. \n'
        pros += '\n'
    elif (person.distance(option2.xcor(), option2.ycor()) < 200):
        checked4 = True
        score += 2
        pass1 = False
        next1.showturtle()
        option2.hideturtle()
        pros += 'QUESTION 4: Waiting until the day before an exam to study will help you understand some concepts.\n'
        cons += 'QUESTION 4: Waiting until the day before an exam to study will be very stressful since you would have to review\n'
        cons +=  'many concepts, this will make you forget some things on the exam.\n'
        pros += '\n'
        cons += '\n'
    elif (person.distance(option3.xcor(), option3.ycor()) < 200):
        checked4 = True
        score += 1
        pass1 = False
        next1.showturtle()
        option3.hideturtle()
        cons += 'QUESTION 4: Not studying at all for the exam is not a good idea because you will be confused on many \n'
        cons += 'concepts on the exam and you will be very stressed out.\n'
        cons += '\n'
def check5():
    global score
    global checked5
    global pass1
    global pros
    global cons
    pass1 = True
    if (person.distance(option1.xcor(), option1.ycor()) < 200):
        checked5 = True
        score += 3
        pass1 = False
        next1.showturtle()
        option1.hideturtle()
        pros += 'QUESTION 5: Prioritizing the project over the show will allow you to not get distracted and get the project finished early.\n'
        pros += '\n'
    elif (person.distance(option2.xcor(), option2.ycor()) < 200):
        checked5 = True
        score += 2
        pass1 = 5
        pass1 = False
        next1.showturtle()
        option2.hideturtle()
        pros += 'QUESTION 5: Watching the show and doing the project will give you some time to work on the project.\n'
        cons += 'QUESTION 5: Watching the show and doing the project will get you distracted and will effect your work on the project.\n'
        pros += '\n'
        cons += '\n'
    elif (person.distance(option3.xcor(), option3.ycor()) < 200):
        checked5 = True
        score += 1
        pass1 = False
        next1.showturtle()
        option3.hideturtle()
        cons += 'QUESTION 5: Prioritizing the show before the project is not a good idea because you will be behind \n'
        cons += 'on the project and you will likely have to submit it late.\n'
        cons += '\n'
def check6():
    global score
    global checked6
    global pass1
    global pros
    global cons
    pass1 = True
    if (person.distance(option1.xcor(), option1.ycor()) < 200):
        checked6 = True
        score += 3
        pass1 = False
        next1.showturtle()
        option1.hideturtle()
        pros += 'QUESTION 6: helping you partner right away for the project is a good idea because you will be able to have more time to make more progress on the project.\n'
        pros += '\n'
    elif (person.distance(option2.xcor(), option2.ycor()) < 200):
        checked6 = True
        score += 2
        pass1 = False
        next1.showturtle()
        option2.hideturtle()
        pros += 'QUESTION 6: You waiting until the last week to help your partner allows you to get closer on completing the project.\n'
        cons += 'QUESTION 6: You waiting until the last week to help your partner would delay your plans on the project and you would have to rush to complete it.\n'
        pros += '\n'
        cons += '\n'
    elif (person.distance(option3.xcor(), option3.ycor()) < 200):
        checked6 = True
        score += 1
        pass1 = False
        next1.showturtle()
        option3.hideturtle()
        cons += 'QUESTION 6: You not helping your partner at all will lead to your project being unfinished.\n'
        cons += '\n'

def check7():
    global score
    global checked7
    global pass1
    global pros
    global cons
    pass1 = True
    if (person.distance(option1.xcor(), option1.ycor()) < 200):
        checked7 = True
        score += 3
        pass1 = False
        next1.showturtle()
        option1.hideturtle()
        pros += "QUESTION 7: Skipping the problem and going back to it at the end allows you to answer\n"
        pros += "more questions and you won't waste any time on the test.\n"
        pros += '\n'
    elif (person.distance(option2.xcor(), option2.ycor()) < 200):
        checked7 = True
        score += 2
        pass1 = False
        next1.showturtle()
        option2.hideturtle()
        pros += 'QUESTION 7: You stayed on the problem for a couple of minutes and then skipped the \n'
        pros += 'which allowed you to answer more questions.\n'
        cons += 'QUESTION 7: You staying on the problem for a couple of minutes wasted time on the exam.\n'
        pros += '\n'
        cons += '\n'
    elif (person.distance(option3.xcor(), option3.ycor()) < 200):
        checked7 = True
        score += 1
        pass1 = False
        next1.showturtle()
        option3.hideturtle()
        cons += 'QUESTION 7: Staying on the problem until you think of an answer is not a good idea because\n'
        cons += 'you are wasting a lot of time that could be used to answer the rest of the questions.\n'
        cons += '\n'

#Setting up screen 1 with Welcome Message 
cheat1 = False 
s = turtle.Screen() 
s.title("Welcome Message") #titles screen
s.bgpic('uic_banner.gif') #sets background picture
text = turtle.Turtle() #creates new turtle named text
text.penup()
text.hideturtle()
text.goto(0, 200)
s.bgcolor("black")
text.color("black")
text.write("Welcome to the CS Story game!", False, align='center', font=('Times New Roman', 30, 'bold')) #writes welcome message
text.goto(0, 140)
text.write('Click the Start button to continue!', False, align='center', font=('Times New Roman', 30, 'bold')) #prompts user to click the start button
#creating new turtle which is the start button
start_button = turtle.Turtle() 
turtle.addshape('startbutton.gif') 
start_button.shape('startbutton.gif')
start_button.penup()
start_button.goto(0, -150)

notStarted = True  #determines if the start button was clicked or not
while notStarted: #waits for the button to be clicked
    start_button.onclick(start) #callls onclick() function

#Next screen: Tells user what game is about
s.clearscreen()
s.title("About the game")
s.bgcolor("black")
s.bgpic('code.gif')
text.color("red")
text.goto(0, 250)
text.write("This game will test your observations on different", False, align='center', font=('Times New Roman', 25, 'bold'))
text.goto(0, 220)
text.write("scenarios throughtout a semester of CS111", False, align='center', font=('Times New Roman', 25, 'bold'))
text.goto(0, 180)
text.write("For each scenario, use the arrow keys to move the character to the choice that you would", False, align='center', font=('Times New Roman', 25, 'bold'))
text.goto(0, 150)
text.write("realistically choose if you were to really go through these scenarios.", False, align='center', font=('Times New Roman', 25, 'bold'))
text.goto(0, 90)
text.write("Then, click the NEXT button that will appear to continue.", False, align='center', font=('Times New Roman', 25, 'bold'))
text.goto(0, 30)
text.write("CLICK THE NEXT BUTTON TO START!", False, align='center', font=('Times New Roman', 30, 'underline')) #prompts the user to click the next button
#creating new turtle which is the next button
next1 = turtle.Turtle()
turtle.addshape("next.gif")
next1.shape("next.gif")
next1.penup()
next1.goto(0, -150)
#determines if the button was clicked or not
notStarted = True 
while notStarted:
    next1.onclick(start) #calls function onclick()

#Next Screen: Scenario 1
s.clearscreen()
s.title("Scenario 1")
s.bgpic('arc.gif')
s.bgcolor('black')
#Inserts person as a turtle for the user to control
person = turtle.Turtle()
person.speed(10)
turtle.addshape('person.gif')
person.shape('person.gif')
person.penup()
person.goto(-450, -200)
#inserting question 1
question1 = turtle.Turtle()
question1.penup()
turtle.addshape('Question1.gif')
question1.shape('Question1.gif')
question1.goto(0, 280)
#inserts option1a
option1 = turtle.Turtle()
option1.penup()
turtle.addshape('Option1a.gif')
option1.shape('Option1a.gif')
option1.goto(350, 150)
#inserts option2a
option2 = turtle.Turtle()
option2.penup()
turtle.addshape('Option2a.gif')
option2.shape('Option2a.gif')
option2.goto(350, -10)
#inserts option3a
option3 = turtle.Turtle()
option3.penup()
turtle.addshape('Option3a.gif')
option3.shape('Option3a.gif')
option3.goto(350, -200)

#s.listen() listens for the arrow keys to be pressed
s.listen()

#calls differnet functions for each key that is pressed(up, left, right, or down)
s.onkey(up, 'Up')
s.onkey(left, 'Left')
s.onkey(right, 'Right')
s.onkey(down, 'Down')


#sets up next button
next1 = turtle.Turtle()
next1.hideturtle()
turtle.addshape("next.gif")
next1.shape("next.gif")
next1.penup()
next1.goto(0, -250)
#waits for button to be clicked
notStarted = True 
while notStarted:
    next1.onclick(start)



#clears first screen
s.clearscreen()
#Next screen: Scenario 2
s2 = turtle.Screen()
s2.bgcolor('black')
s2.bgpic('calendar.gif')
s2.title('Scenario 2')
#Inserts person as a turtle for the user to control
person = turtle.Turtle()
person.speed(10)
turtle.addshape('person.gif')
person.shape('person.gif')
person.penup()
person.goto(-450, -200)
#inserts question2
question2 = turtle.Turtle()
question2.penup()
turtle.addshape('Question2.gif')
question2.shape('Question2.gif')
question2.goto(0, 280)
#creating option1b
option1 = turtle.Turtle()
option1.penup()
turtle.addshape('option1b.gif')
option1.shape('option1b.gif')
option1.goto(300, 150)
#creating option2b
option2 = turtle.Turtle()
option2.penup()
turtle.addshape('option2b.gif')
option2.shape('option2b.gif')
option2.goto(300, -10)
#creating option3b
option3 = turtle.Turtle()
option3.penup()
turtle.addshape('option3b.gif')
option3.shape('option3b.gif')
option3.goto(300, -200)
pass1 = True #allows check() functions to be called

s2.listen()
s2.onkey(up, 'Up')
s2.onkey(left, 'Left')
s2.onkey(right, 'Right')
s2.onkey(down, 'Down')
#inserts next button
next1 = turtle.Turtle()
next1.hideturtle()
turtle.addshape("next.gif")
next1.shape("next.gif")
next1.penup()
next1.goto(0, -250)

#determines if button was clicked or not
notStarted = True 
while notStarted:
    next1.onclick(start) #calls function onclick()





s2.clearscreen()
#next screen: Scenario3
s3 = turtle.Screen()
s3.bgpic('scenario3.gif')
s3.title('Scenario 3')
#inserts person as a turtle for the user to control
person = turtle.Turtle()
person.speed(10)
turtle.addshape('person.gif')
person.shape('person.gif')
person.penup()
person.goto(-450, -200)
#inserts Question 3
question3 = turtle.Turtle()
question3.penup()
turtle.addshape('Question3.gif')
question3.shape('Question3.gif')
question3.goto(0, 280)
#inserts option1c
option1 = turtle.Turtle()
option1.penup()
turtle.addshape('option1c.gif')
option1.shape('option1c.gif')
option1.goto(350, 150)
#inserts option2c
option2 = turtle.Turtle()
option2.penup()
turtle.addshape('option2c.gif')
option2.shape('option2c.gif')
option2.goto(350, -10)
#inserts option3c
option3 = turtle.Turtle() 
option3.penup()
turtle.addshape('option3c.gif')
option3.shape('option3c.gif')
option3.goto(350, -175)
pass1 = True
s3.listen()

s3.onkey(up, 'Up')
s3.onkey(left, 'Left')
s3.onkey(right, 'Right')
s3.onkey(down, 'Down')

next1 = turtle.Turtle()
next1.hideturtle()
turtle.addshape("next.gif")
next1.shape("next.gif")
next1.penup()
next1.goto(0, -250)

notStarted = True 
while notStarted:
    next1.onclick(start)

if cheat1 == False: #determines if option3c was chosen or not, since it is not chosen, the game will move on normally.
    s3.clearscreen()
    #next screen: Scenario 4
    s4 = turtle.Screen()
    s4.bgcolor('black')
    s4.bgpic('exam.gif')
    s4.title('Scenario 4')
    #inserts person as a turtle for the user to control
    person = turtle.Turtle()
    person.speed(10)
    turtle.addshape('person.gif')
    person.shape('person.gif')
    person.penup()
    person.goto(-450, -200)
    #inserts question 4
    question4 = turtle.Turtle()
    question4.penup()
    turtle.addshape('question4.gif')
    question4.shape('question4.gif')
    question4.goto(0, 280)
    #inserts option1d
    option1 = turtle.Turtle()
    option1.penup()
    turtle.addshape('option1d.gif')
    option1.shape('option1d.gif')
    option1.goto(350, 95)
    #inserts option2d
    option2 = turtle.Turtle() 
    option2.penup()
    turtle.addshape('option2d.gif')
    option2.shape('option2d.gif')
    option2.goto(350, -90)
    #inserts option3d
    option3 = turtle.Turtle()
    option3.penup()
    turtle.addshape('option3d.gif')
    option3.shape('option3d.gif')
    option3.goto(350, -240)
    pass1 = True
    s4.listen()
    s4.onkey(up, 'Up')
    s4.onkey(left, 'Left')
    s4.onkey(right, 'Right')
    s4.onkey(down, 'Down')

    next1 = turtle.Turtle()
    next1.hideturtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)

    notStarted = True 
    while notStarted:
        next1.onclick(start)




    s4.clearscreen()
    #next screen: scenario 5
    s5 = turtle.Screen()
    s5.bgcolor('black')
    s5.bgpic('tv1.gif')
    s5.title('Scenario 5')
    #Inserts person as a turtle for the user to control
    person = turtle.Turtle()
    person.speed(10)
    turtle.addshape('person.gif')
    person.shape('person.gif')
    person.penup()
    person.goto(-450, -200)
    question5 = turtle.Turtle()
    question5.penup()
    turtle.addshape('question5.gif')
    question5.shape('question5.gif')
    question5.goto(0, 280)
    #inserting option1e
    option1 = turtle.Turtle()
    option1.penup()
    turtle.addshape('option1e.gif')
    option1.shape('option1e.gif')
    option1.goto(310, 130)
    #Inserting option2e
    option2 = turtle.Turtle()
    option2.penup()
    turtle.addshape('option2e.gif')
    option2.shape('option2e.gif')
    option2.goto(310, -40)
    #Inserting option3e
    option3 = turtle.Turtle()
    option3.penup()
    turtle.addshape('option3e.gif')
    option3.shape('option3e.gif')
    option3.goto(310, -240)
    pass1 = True
    s5.listen()
    s5.onkey(up, 'Up')
    s5.onkey(left, 'Left')
    s5.onkey(right, 'Right')
    s5.onkey(down, 'Down')

    next1 = turtle.Turtle()
    next1.hideturtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)

    notStarted = True 
    while notStarted:
        next1.onclick(start)




    s5.clearscreen()
    #next screen: Scenario 6
    s6 = turtle.Screen()
    s6.bgcolor('black')
    s6.bgpic('partner.gif')
    s6.title('Scenario 6')
    #Inserts person as a turtle for the user to control
    person = turtle.Turtle()
    person.speed(10)
    turtle.addshape('person.gif')
    person.shape('person.gif')
    person.penup()
    person.goto(-450, -200)
    #Inserts question 6
    question6 = turtle.Turtle()
    question6.penup()
    turtle.addshape('question6.gif')
    question6.shape('question6.gif')
    question6.goto(0, 280)
    #Inserts option1f
    option1 = turtle.Turtle() 
    option1.penup()
    turtle.addshape('option1f.gif')
    option1.shape('option1f.gif')
    option1.goto(350, 120)
    #Inserts option2f
    option2 = turtle.Turtle() 
    option2.penup()
    turtle.addshape('option2f.gif')
    option2.shape('option2f.gif')
    option2.goto(350, -50)
    #Inserts option3f
    option3 = turtle.Turtle()
    option3.penup()
    turtle.addshape('option3f.gif')
    option3.shape('option3f.gif')
    option3.goto(350, -200)
    pass1 = True
    s6.listen()
    s6.onkey(up, 'Up')
    s6.onkey(left, 'Left')
    s6.onkey(right, 'Right')
    s6.onkey(down, 'Down')

    next1 = turtle.Turtle()
    next1.hideturtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)

    notStarted = True 
    while notStarted:
        next1.onclick(start)



    s6.clearscreen()
    #next screen: Scenario 7
    s7 = turtle.Screen()
    s7.bgcolor('black')
    s7.bgpic('test.gif')
    s7.title('Scenario 7')
    #Inserts person as a turtle for the user to control
    person = turtle.Turtle()
    person.speed(10)
    turtle.addshape('person.gif')
    person.shape('person.gif')
    person.penup()
    person.goto(-450, -200)
    #Inserting question6
    question6 = turtle.Turtle()
    question6.penup()
    turtle.addshape('question7.gif')
    question6.shape('question7.gif')
    question6.goto(0, 280)
    #Inserting option1f
    option1 = turtle.Turtle() 
    option1.penup()
    turtle.addshape('option1g.gif')
    option1.shape('option1g.gif')
    option1.goto(350, 150)
    #Inserting option2f
    option2 = turtle.Turtle()
    option2.penup()
    turtle.addshape('option2g.gif')
    option2.shape('option2g.gif')
    option2.goto(350, -10)
    #Inserting option3f
    option3 = turtle.Turtle()
    option3.penup()
    turtle.addshape('option3g.gif')
    option3.shape('option3g.gif')
    option3.goto(350, -200)
    pass1 = True
    s7.listen()
    s7.onkey(up, 'Up')
    s7.onkey(left, 'Left')
    s7.onkey(right, 'Right')
    s7.onkey(down, 'Down')

    next1 = turtle.Turtle()
    next1.hideturtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)

    notStarted = True 
    while notStarted:
        next1.onclick(start)
    
    s.clearscreen()
    #Next screen: results
    s.title('Results')
    s.bgpic('results.gif')
    text.goto(0, 250)
    text.color('blue')
    text.write("HERE ARE YOUR RESULTS!", False, align='center', font=('Times New Roman', 40, 'underline'))
    text.goto(0, 180)
    text.color('blue')
    text.write('YOUR ESTIMATED GRADE WOULD BE: ', False, align='center', font=('Times New Roman', 40, 'bold'))
    text.goto(0, 0)
    #changes the text color depending on the estimated grade
    if outcomes[str(score)] == 'POOR': 
        text.color('red')
    elif outcomes[str(score)] == 'OKAY':
        text.color('yellow')
    elif outcomes[str(score)] == 'EXCELLENT':
        text.color('green')
    text.write(outcomes[str(score)], False, align='center', font=('Times New Roman', 100, 'underline')) #writes final outcome
    #inserts next button
    next1 = turtle.Turtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)
    next1.showturtle()
    #determines if next button was clicked or not
    notStarted = True 
    while notStarted:
        next1.onclick(start)

    s.clearscreen()
    #Next screen: PROS
    s.title('PROS')
    s.bgcolor('black')
    text.goto(0, 250)
    text.color('green')
    text.write('PROS', False, align='center', font=('Times New Roman', 40, 'underline'))
    text.goto(0,-220)
    text.write(pros, False, align='center', font=('Times New Roman', 15, 'bold'))

    next1 = turtle.Turtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)
    next1.showturtle()

    notStarted = True 
    while notStarted:
        next1.onclick(start)

    s.clearscreen()
    #next screen: CONS
    s.title('CONS')
    s.bgcolor('black')
    text.goto(0, 250)
    text.color('red')
    text.write('CONS', False, align='center', font=('Times New Roman', 40, 'underline'))
    text.goto(0, -220)
    text.write(cons, False, align='center', font=('Times New Roman', 15, 'bold'))

    next1 = turtle.Turtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)
    next1.showturtle()

    notStarted = True 
    while notStarted:
        next1.onclick(start)

    s.clearscreen()
    #Next screen: Congratulations 
    s8 = turtle.Screen()
    s8.title('Congrats')
    s8.bgcolor('sky blue')
    #inserting new image party1 as a turtle
    party1 = turtle.Turtle()
    turtle.addshape('party.gif')
    party1.shape('party.gif')
    party1.penup()
    party1.goto(-350, 200)
    confetti() #calls confetti function to make confettis
    text.goto(0, 0)
    text.color('purple')
    text.write('CONGRATULATIONS ON FINISHING THE GAME!!!!!', False, align='center', font=('Courier', 40, 'underline'))
elif cheat1 == True: #only runs if option3c was chosen, which ends the game
    s3.clearscreen()
    #next screen: Results
    s.title('Results')
    s.bgpic('failed.gif')
    text.goto(0, 250)
    text.color('blue')
    text.write("UH OH!", False, align='center', font=('Times New Roman', 40, 'underline'))
    text.goto(0, 180)
    text.color('blue')
    text.write('YOUR ESTIMATED GRADE WOULD BE: ', False, align='center', font=('Times New Roman', 40, 'bold'))
    
    next1 = turtle.Turtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)
    next1.showturtle()

    notStarted = True 
    while notStarted:
        next1.onclick(start)

    s.clearscreen()
    #Next screen: Pros 
    s.title('PROS')
    s.bgcolor('black')
    text.goto(0, 250)
    text.color('green')
    text.write('PROS', False, align='center', font=('Times New Roman', 40, 'underline'))
    text.goto(0,0)
    text.write(pros, False, align='center', font=('Times New Roman', 15, 'bold'))

    next1 = turtle.Turtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)
    next1.showturtle()

    notStarted = True 
    while notStarted:
        next1.onclick(start)

    s.clearscreen()
    #Next screen: Cons
    s.title('CONS')
    s.bgcolor('black')
    text.goto(0, 250)
    text.color('red')
    text.write('CONS', False, align='center', font=('Times New Roman', 40, 'underline'))
    text.goto(0, -200)
    text.write(cons, False, align='center', font=('Times New Roman', 15, 'bold'))

    next1 = turtle.Turtle()
    turtle.addshape("next.gif")
    next1.shape("next.gif")
    next1.penup()
    next1.goto(0, -250)
    next1.showturtle()

    notStarted = True 
    while notStarted:
        next1.onclick(start)


    s.clearscreen()
    s8 = turtle.Screen()
    #next screen: Congratulations 
    s8.title('Congrats')
    s8.bgcolor('sky blue')
    party1 = turtle.Turtle()
    turtle.addshape('party.gif')
    party1.shape('party.gif')
    party1.penup()
    party1.goto(-350, 200)
    confetti() #calls confetti function to display confettis on the screen
    text.goto(0, 0)
    text.color('purple')
    text.write('CONGRATULATIONS ON FINISHING THE GAME!!!!!', True, align='center', font=('Courier', 40, 'underline'))

        



#keeps code running
turtle.mainloop()