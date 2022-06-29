import random
from random import sample
from tkinter import *

q_sets = {
    'A': {'number': 5, 'diff': 1, 'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1},
    'B': {'number': 5, 'diff': 2, 'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1},
    'C': {'number': 5, 'diff': 3, 'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}
    }

"""
all_questions: dictionary with
    key = code of question
    value = dictionary, topic: first letter, diff: integer
"""


all_questions = {}

"""
Getting question codes.
For more info, look at the spreadsheet.
"""
question_codes = []

topic = ["A", "B", "C", "D", "E"]

subtopics = ["01", "02", "03", "04", "05", "06", "07", "08"]
levels = ["1", "2", "3"]
variants = ["1", "2", "3"]

noquestions = []
for i in range(len(topic)):
    for j in range(len(subtopics)):
        for k in range(len(levels)):            
            if topic[i] == "A" and subtopics[j] == "07" and levels[k] == "3":
                noquestions.append(topic[i] + subtopics[j] + levels[k])
            elif topic[i] == "B" and ((subtopics[j] in ["01", "02", "06", "07", "08"] and levels[k] == "3")
                                      or (subtopics[j] == "05" and levels[k] == "1")):
                noquestions.append(topic[i] + subtopics[j] + levels[k])
            elif topic[i] == "E" and (subtopics[j] in ["02", "03", "06", "08"] and levels[k] == "3"):
                noquestions.append(topic[i] + subtopics[j] + levels[k])

            elif topic[i] == "C" and (subtopics[j] in ["07", "08"]):
                noquestions.append(topic[i] + subtopics[j] + levels[k])
            elif topic[i] == "C" and subtopics[j] in ["02", "03", "05"] and levels[k] == "3":
                noquestions.append(topic[i] + subtopics[j] + levels[k])
            
            elif topic[i] == "D" and (subtopics[j] == "08"):
                noquestions.append(topic[i] + subtopics[j] + levels[k])
            elif topic[i] == "D" and (((subtopics[j] == "01" and levels[k] == "3")) or(subtopics[j] in ["02", "03"] and levels[k] in ["2", "3"])):
                noquestions.append(topic[i] + subtopics[j] + levels[k])
                    
for i in range(len(topic)):
    for j in range(len(subtopics)):
        for k in range(len(levels)):
            for m in range(len(variants)):
                if (topic[i] + subtopics[j] + levels[k]) in noquestions:
                    continue
                else:
                    question_codes.append(topic[i] + subtopics[j] + levels[k] + variants[m])




# Add question codes to question bank
for i in range(len(question_codes)):
    splitcode = list(question_codes[i])
    all_questions[question_codes[i]] = {'topic': splitcode[0], 'diff': int(splitcode[3])}
    

# Making worksheets
def make_worksheet(difficulty):
    q_set = difficulty
    difficulty = q_sets[q_set]['diff']

    question_number_A = []
    question_number_B = []
    question_number_C = []
    question_number_D = []
    question_number_E = []

    for key, value in all_questions.items():
        if value['diff'] == difficulty and value['topic'] == 'A':
            question_number_A.append(key)
        elif value['diff'] == difficulty and value['topic'] == 'B':
            question_number_B.append(key)
        elif value['diff'] == difficulty and value['topic'] == 'C':
            question_number_C.append(key)
        elif value['diff'] == difficulty and value['topic'] == 'D':
            question_number_D.append(key)
        elif value['diff'] == difficulty and value['topic'] == 'E':
            question_number_E.append(key)

    # now select questions randomly from the list
    # no duplicates
    questions = []
    questions.append(sample(question_number_A, k=q_sets[q_set]['A']))
    questions.append(sample(question_number_B, k=q_sets[q_set]['B']))
    questions.append(sample(question_number_C, k=q_sets[q_set]['C']))
    questions.append(sample(question_number_D, k=q_sets[q_set]['D']))
    questions.append(sample(question_number_E, k=q_sets[q_set]['E']))

    questionlist = []
    for i in range(len(questions)):
        questionlist.append(questions[i][0])

    questionlist=' '.join([str(item) for item in questionlist])

    return questionlist

def number_of_all_questions():
    return print(len(list(all_questions.keys())))

def easyq():
    output_txt["text"] = make_worksheet("A")

def mediumq():
    questionset = make_worksheet("B")
    output_txt["text"] = questionset

def hardq():
    questionset = make_worksheet("C")
    output_txt["text"] = questionset

def incorrectscore():
    global click
    if click <= 5:
        add = 0
        current = scores_txt["text"]
        scores_txt["text"] = add + int(current)
        click += 1
        
def partial():
    global click
    if click <= 5:
        add = 1
        current = scores_txt["text"]
        scores_txt["text"] = add + int(current)
        click += 1
        
def seasy():
    global click
    if click <= 5:
        add = 2
        current = scores_txt["text"]
        scores_txt["text"] = add + int(current)
        click += 1

def smedium():
    global click
    if click <= 5:
        add = 3
        current = scores_txt["text"]
        scores_txt["text"] = add + int(current)
        click += 1

def shard():
    global click
    if click <= 5:
        add = 4
        current = scores_txt["text"]
        scores_txt["text"] = add + int(current)
        click += 1

click = 1

# tkinter time
window = Tk()
window.title("Question generator")
window.geometry("500x450")

label = Label(text = "Click one button to choose your question set.")
label.place(x = 50, y = 20, width = 350, height = 25)

buttonq1 = Button(text = "Easy", command = easyq)
buttonq1.place(x = 50, y = 80, width = 75, height = 25)

buttonq2 = Button(text = "Medium", command = mediumq)
buttonq2.place(x = 150, y = 80, width = 75, height = 25)

buttonq3 = Button(text = "Hard", command = hardq)
buttonq3.place(x = 250, y = 80, width = 75, height = 25)

output_label = Label(text = "Questions chosen: ")
output_label.place(x = 50, y = 150, width = 125, height = 25)

output_txt = Message(text = 0)
output_txt.place(x = 200, y = 150, width = 125, height = 75)
output_txt["bg"] = "white"
output_txt["relief"] = "ridge"

instructions_label = Label(text = "Refer to the Excel spreadsheet and do the questions.")
instructions_label.place(x = 10, y = 225, width = 450, height = 50)

scores_label = Label(text = "Scores: ")
scores_label.place(x = 50, y = 300, width = 50, height = 25)

scores_txt = Message(text = 0)
scores_txt.place(x = 100, y = 300, width = 50, height = 25)

button1S = Button(text = "Incorrect", command = incorrectscore)
button1S.place(x = 50, y = 350, width = 150, height = 25)

button2S = Button(text = "Partially correct", command = partial)
button2S.place(x = 250, y = 350, width = 150, height = 25)

button3S = Button(text = "Easy", command = seasy)
button3S.place(x = 50, y = 400, width = 100, height = 25)

button4S = Button(text = "Medium", command = smedium)
button4S.place(x = 175, y = 400, width = 100, height = 25)

button5S = Button(text = "Hard", command = shard)
button5S.place(x = 300, y = 400, width = 100, height = 25)



window.mainloop()
