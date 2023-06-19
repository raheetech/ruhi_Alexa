
import speech_recognition as ek
import pyttsx3
import  pywhatkit
import datetime
import  wikipedia
import  pyjokes

listener = ek.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
engine.say('I am Ruhi')
engine.say('what can i do for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with ek.Microphone() as source:
            print('Ruhi is listening..........')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ruhi' in command:
                command=command.replace('ruhi', '')
                print(command)

    except:
        pass
    return command
def run_ruhi():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the person is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('i am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'what the heck is ' in command:
        viva = command.replace('what the heck is', '')
        info = wikipedia.summary(viva, 1)
        print(info)
        talk(info)
    else:
        talk('please say it again')

while True:
    run_ruhi()