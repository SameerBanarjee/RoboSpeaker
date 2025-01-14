import pyttsx3
engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Sameer")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q" :
            op = 'bye bye friend'
            engine.say(op)
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()