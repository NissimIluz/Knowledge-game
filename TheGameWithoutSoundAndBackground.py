import random
from tkinter import *

#!/usr/bin/env python
__author__ = "Nissim Iluz"
__copyright__ = "Copyright 2020, Hodaya Iluz"
__credits__ = "Hodaya Iluz"

"""Foobar.py: Computer game, final work in citizenship."""

window = Tk()


class Question:
    def __doc__(self):
        intro_str = "This class create and save the question "

        doc_str = "V1"
        return intro_str + '\n' + doc_str

    '''This functions respond to click on the button'''

    def runA(self):
        run(self.ID1)

    def runB(self):
        run(self.ID1 + 1)

    def __init__(self, question, answer, ID1, runA=runA, runB=runB):
        self.question = question
        self.answer = answer
        self.button1 = Button(text=question, fg="black", bg="white", command=self.runA)
        self.button2 = Button(text=answer, fg="black", bg="white", command=self.runB)
        self.ID1 = ID1


class Selected:
    def __doc__(self):
        intro_str = "This class save some variables for the game"

    def __init__(self):
        self.top = None
        self.bottom = None
        self.failure = 0


name_of_the_game = "משחק באזרחות"
s = Selected()

window.title(name_of_the_game)

w = frame = Frame(window, bg="#99c1ff")
w.place(relx=0.01, rely=0.01, relwidth=1, relheight=1)
title = Label(window, text="משחק באזרחות", fg="blue", bg="white", font=("Helvetica", 49))
title.place(relx=0.5, rely=0.15, anchor='n')
exitButton = Button(text="Exit", command=window.quit)

# this is the questions part
num_of_question = 11
qustions = []
qustions.append(Question(":" + "מאפיין יהודי הבא לידי ביטוי בהכרזת העצמאות", "נביאי ישראל", 1))
qustions.append(Question("?" + "בעקבות מה פרצה מלחמת העצמאות", "החלטת החלוקה", 3))
qustions.append(Question("?" + "על ידי מי נחתם מסמך הכרזת העצמאות", "דוד בן גוריון וחברי מועצת העם", 5))
qustions.append(Question("?" + "מתי קמה מדינת ישראל", "1948", 7))
qustions.append(Question("?" + "(181) " + "מתי הציעו את החלטת החלוקה ", "1947", 9))
qustions.append(Question("?" + "למי שלח השר החוץ בלפור את הצהרתו", "רוטשילד", 11))
qustions.append(
    Question("?" + "איך קראו להסכם שבעקבותיו קבלה בריטניה הסמכה להקים בית לאומי בארץ ישראל לעם היהודי", "כתב המנדט",
             13))
qustions.append(Question("" + "מדינת ישראל קמה ב__ במאי", "14", 15))
qustions.append(Question(":" + "מספר החלקים שהיו במסמך ההכרזה", "3", 17))
qustions.append(Question(":" + "את החלטת החלוקה הציעו", "האו\"ם", 19))
qustions.append(Question(":" + "בריטניה קיבלה הסכמה ליישם את הצהרת בלפור ע\"י", "חבר העמים", 21))

''''This function returns list of random number in size of the number of question'''


def randomList():
    preList = []
    for x in range(num_of_question):
        preList.append(x)
    list = []
    for i in range(num_of_question):
        r = random.choice(preList)
        list.append(r)
        preList.remove(r)
    return list


''''This function responds to click on button  and decides on the right response'''


def run(t):
    t = t - 1
    t1 = int(t / 2)
    if t % 2 == 0:
        qustions[t1].button1.config(bg="yellow")
        if s.top != None and s.top != t1:
            qustions[s.top].button1.config(bg="white")
        s.top = t1
    else:
        qustions[t1].button2.config(bg="yellow")
        if s.bottom != None and s.bottom != t1:
            qustions[s.bottom].button2.config(bg="white")
        s.bottom = t1
    if (s.bottom == s.top):
        qustions[s.top].button1.config(bg="green")
        qustions[s.top].button2.config(bg="green")
        qustions[s.top].button1.config(command="")
        qustions[s.top].button2.config(command="")
        s.top = None
        s.bottom = None
        out = True
        for index in range(num_of_question):
            print((qustions[index].button1["bg"]))
            if (qustions[index].button1["bg"] != "green"):
                out = False
        if (out):
            frame = Frame(window, bg="#99c1ff")
            if s.failure > 2:
                end_of_tje_game = Label(text="LOSER!!!", fg="brown", font=("Helvetica", 49))
            else:
                end_of_tje_game = Label(text="NICE!!!", fg="gold", font=("Helvetica", 49))
            frame.place(relwidth=1, relheight=1)
            end_of_tje_game.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.75, anchor='n')
            exitButton1 = Button(text="Exit", fg="red", bg="grey", font=("Helvetica", 28), command=window.quit)

            exitButton1.place(relx=0.5, rely=0.7, relwidth=0.15, relheight=0.15, anchor='n')

    if (s.bottom != s.top and s.top != None and s.bottom != None):
        s.failure = s.failure + 1
        qustions[s.top].button1.config(bg="red")
        qustions[s.bottom].button2.config(bg="red")
        s.top = None
        s.bottom = None



'''The display part, create  and initializing the game'''
randomList1 = randomList()
randomList2 = randomList()
distance = 0.05
y = 0.78
for index in range(num_of_question):
    qustions[randomList1[index]].button1.place(relx=0.7, rely=y, relwidth=0.4, relheight=0.035, anchor='n')
    qustions[randomList2[index]].button2.place(relx=0.22, rely=y, relwidth=0.2, relheight=0.035, anchor='n')
    y = y - distance
exitButton.place(relx=0.96, rely=0.95)

window.mainloop()
