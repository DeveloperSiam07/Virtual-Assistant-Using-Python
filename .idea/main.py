#import point
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

#main body
listener = sr.Recognizer()
zein = pyttsx3.init()
voices = zein.getProperty('voices')
zein.setProperty('voice', voices[1].id)
def talk(text):
    zein.say(text)
    zein.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening......')
            print('Ready for talk......')
            talk('Hi Commander, This is zein')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'zein' in command:
                print('I,m listening......')
                talk('I,m listening')

    # Failure part
    except:
        pass
    return command


# Brain
def run_zein():
    command = take_command()


    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Now its '+ time)
        talk('Now its ' + time)

    elif 'date' in command:
        date = datetime.date.today().strftime('%DD:%MM:%YY')
        talk('Today is' + date)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('Now playing' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)

    elif 'whats your name' in command:
          talk('my name is doctor zein froster aka lady thor')

    elif 'is ai dengerous' in command:
        talk('yeah, it can be dengerous for human civilization by its exploit')

    elif 'joke' in command:
        talk(pyjokes.get_jokes())

    elif 'i like you' in command:
        talk('It was at the moment he knew, he fucked up')

    else:
        talk('I didn"t understand, Please repeat it')
        pywhatkit.search(command)

#Timing loop
while True:
  run_zein()