import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import netguy
import em
import note

from tensorflow.keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
print("Words: ",words)
print("Classes: ",classes)

context = ""
cache = []
cache_num = 0
pass_flag = 0
info = []
def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    print("Sentence words: ",sentence_words)
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    print("Going to clean_up_sentence")
    sentence_words = clean_up_sentence(sentence)
    print("Back to bow")
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    print("Bag: ", np.array(bag))
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    print("Going to bow")
    p = bow(sentence, words,show_details=False)
    print("Back to predict class")
    res = model.predict(np.array([p]))[0]
    print("Res: ",res)
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    print("Results :", results)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    print("Return list: ",return_list)
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    print("Result: ",result)
    return result

def chatbot_response(msg):
    global context
    global cache
    global cache_num
    print("Going to predict_class")
    ints = predict_class(msg, model)
    print("Ints: ", ints)
    print("Back to chatbot response")
    print("Going to getResponse")
    res = getResponse(ints, intents)
    print("Back to chatbot_response")
    print("Res: ",res)
    if ints[0]['intent'] == 'answer':
        response = res + "\n" + search(msg) + "\nmore?(y/n)"
        return response
    if ints[0]['intent'] == 'more':
        if cache_num < len(cache):
            response = cache[cache_num] + "\nmore?(y/n)"
            cache_num += 1
        else:
            response = 'No more results'
            cache = []
            cache_num = 0
        return response
    if ints[0]['intent'] == 'email_info':
        global info
        info = msg.split('~')
        request_password()
    if ints[0]['intent'] == 'note':
        request_note()
    if ints[0]['intent'] == 'note_search':
        note_search()
    if ints[0]['intent'] == 'get_all':
        response = note.get_all()
        return response

    return res


def search(msg):
    global cache
    global cache_num
    cache_num = 0
    result = netguy.search(msg)
    print(result)
    cache = result
    cache_num += 1
    try:
        return result[cache_num - 1]
    except:
        return 'No results :('

#Creating GUI with tkinter
import tkinter
from tkinter import *

def request_password():
    msg = 'Enter password:\n\n'
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, msg)
    ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)
    EntryBox.config(show='*')
    global pass_flag
    pass_flag = 1

def request_note():
    msg = 'Noting...\n\n'
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, msg)
    ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)
    EntryBox.config(show="")
    global pass_flag
    pass_flag = 2

def note_search():
    msg = 'What to look for?\n\n'
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, msg)
    ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)
    EntryBox.config(show="")
    global pass_flag, cache_num
    pass_flag = 3
    cache_num = 0
    

def send(s):
    global pass_flag
    msg = EntryBox.get().strip() #"1.0",'end-1c'
    EntryBox.delete(0,END)

    if msg != '' and not pass_flag:
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    else:
        if pass_flag == 1:
            m = {}
            m['receiver'] = info[0]
            m['sender'] = info[1]
            m['password'] = msg
            m['subject'] = info[2]
            m['body'] = info[3]
            res = em.mailer(m)
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Bot: " + res + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))    
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            pass_flag = 0
            EntryBox.config(show="")
        elif pass_flag == 2:
            res = note.noter(msg)
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Bot: " + res + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))    
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            pass_flag = 0
            EntryBox.config(show="")
        elif pass_flag == 3:
            global cache
            global cache_num
            result = note.note_searcher(msg)
            print(result)
            cache = result
            cache_num += 1
            if result[0] == 'Nothing Found':
                res = result[0]
            else:
                res = "Here's what I found:\n" + result[cache_num - 1] + "\nmore?(y/n)"
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Bot: " + res + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))    
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            pass_flag = 0
            EntryBox.config(show="")
    

base = Tk()
base.title("Hello")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Entry(base, bd=0, bg="white",width="29", font="Arial")
EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
