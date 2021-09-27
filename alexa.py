from os import replace
import os
import pyaudio
import pyttsx3 
import speech_recognition as sp
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes

listner = sp.Recognizer()


engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def talk(talk):
    engine.say(talk)
    engine.runAndWait()


def main():
    try:
        with sp.Microphone() as source :
            print("listing...")
            talk('listing...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa' '')
                print(command)

    except:
        pass
    return command

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour <= 0 and hour > 12:
        print('Good morning sir! i am your voice assisstant. how may i help you')
        talk('Good morning sir! i am your voice assisstant. how may i help you')
    elif hour >= 12 and hour < 18:
        print('good afternoon sir! i am your voice assisstant. how may i help you. ')
        talk('good afternoon sir! i am your voice assisstant. how may i help you. ')
    else:
        print('good evening sir! i am your voice assisstant. how may i help you')
wish()
def alexa_run():
    # wish()
    command = main()
    if 'time'in command:
        if 'a.m.' in command:
            am = datetime.datetime.now().strftime('%I:%M %p')   
            print('current time is : ' +  am)
            talk('current time is : ' + am)
        elif '' in command:
            time = datetime.datetime.now().strftime('%H:%M') 
            print('current time is : ' +  time)
            talk('current time is : ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%D:%Y')
        print('today is: ' + date)
        talk('today is: ' + date)
    elif 'play on youtube' in command:
        song = command.replace('play on youtube', '')
        print('playing' + song + ' on youtube...')
        talk('playing'+ song + ' on youtube...')
        pywhatkit.playonyt(song)
    elif 'play music' in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[0]))
    elif 'brown' in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[0]))
    elif "childhood " in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[6]))
    elif "is this happening" in command :
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[5]))
    elif 'mask off' in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[4]))
    elif 'relaxing' in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[7]))
    elif 'i am peaky blinder' in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[3]))
    elif 'dj dusk' in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[2]))
    elif 'could you find me' in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[1]))
    elif '16 shots' in command:
        print('playing...')
        talk('playing...')
        music_directory = 'C:\\Users\HP\\Downloads\\Music'
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, music[8]))
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'search' in command:
        browse = command.replace('search', '')
        webbrowser.open('https://google.com/search?q=' + browse)
        print('searching...')
        talk('searching...')
    elif 'mushtaq tanneries' in command:
            # wixsite = command.replace('taimoor', '')
            webbrowser.open('https://taimoormushtaq08.wixsite.com//website-1')
            print('searching...')
            talk('searching...')
    elif 'are you single' in command:
        # sgl = command.replace('', '')
        print('no, i am in relation with wifi')
        talk('no, i am in relation with wifi')
    elif 'joke' in command:
        joke = command.replace('joke', '')
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'turn off' in command:
        print('good bye....my master')
        talk('good bye....my master')
        exit()
    elif 'what are you doing' in command:
        hour = int(datetime.datetime.now().hour)
        if hour <= 0 and hour > 12:
            print('i just took my breakfast. now i am ready to help you')
            talk('i just took my breakfast. now i am ready to help you')
        elif hour >= 12 and hour < 18:
            print("i was doing Kellogg's and you woke me up. now tell me what to do")
            talk("i was doing Kellogg's and you woke me up. now tell me what to do")
        else:
            print('i was just going to eat my dinner.  now tell me what to do')
    elif 'how are you' in command:
        print('morning i had a little bit headache beacause of your too much oders. i have taken my  medicine. now i am fine')
        talk('morning i had a little bit headache beacause of your too much oders. i have taken my  medicine. now i am fine')
    elif 'email' in command:
        print('checking your mail.')
        talk('checking your mail.')
        webbrowser.open('https://mail.google.com/')
    elif 'gmail' in command:
        # mail = command.replace('mail', '')
        print('checking your mail.')
        talk('checking your mail.')
        webbrowser.open('https://mail.google.com/')   
    elif 'thank you' and 'thanks'in command:
        # danke = command.replace('thanks', '')
        print('not a problem, you are just like bro')
        talk('not a problem, you are just like bro')
    elif 'youtube' in command:
        webbrowser.open('https://www.youtube.com/')
        print('searching.....')
        talk('searching.....')
    elif 'stackoverflow' in command:
        webbrowser.open('https://stackoverflow.com')
        print('searching.....')
        talk('searching.....')
    elif 'facebook' in command:
        webbrowser.open('https://www.facebook.com/')
        print('searching.....')
        talk('searching.....')
    elif 'instagram' in command:
        webbrowser.open('https://www.instagram.com/')
        print('searching.....')
        talk('searching.....')
    

    else:
        print('say again, I could not understand.')
        talk('say again, I could not understand.')

while True:
    alexa_run()
