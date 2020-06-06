import time

def consolelog(text):
    print(text)

def setTimeout(milliseconds):
    milliseconds = milliseconds/1000 
    time.sleep(milliseconds)

def function(name, code):
    def name():
        code

def alert(text):
    print("\n\n\n_____________________" + text + "\n\n\n______________________")

def var(name, value):
    global name
    name = value