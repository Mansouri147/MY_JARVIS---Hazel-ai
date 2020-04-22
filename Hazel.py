import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import tkinter as tk
import re
import commands

n=0
User = ""
print("Initializing JARVIS...")



online = True
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 190)


def speak(text):
    engine.say(text)
    engine.runAndWait()
speak ("initializing JARVIS")

def greetings():
    hour = int(datetime.datetime.now().hour)

    if hour >= 2 and hour < 12:
        speak("Good morning " + User) 
    elif hour >= 12 and hour < 18:
        speak("good afternoon " + User)
    else:
        speak("good evening " + User)

def takecommand():
    query = None
    while query == None:
        response = ("", "i'm online and ready", "",'how may i help',  "",'how may i be of assistance?',"",f'how can i assist you {User}', "",)
        speak(random.choices(response))
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source)

        try:
            print("Recognizing...")
            query =r.recognize_google(audio, language = 'en-US')
            print(f"user said: {query} \n")

        except Exception as e:
                speak("say that again please")
                print("say that again please")
                query = None
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("SMTP@GMAIL.COM",587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    # here goes the recipient email
    server.sendmail('recipient@gmail.com',to ,content)
    server.close()

def take_name(self):
    query = takecommand()
    query = query.lower()
    main_user= ('')
    if "i'm " in query:
        User_name = query.split("'m ")[1].split(' ')[0]
        main_user = User_name
        
    elif 'my name is ' in query:
        User_name = query.split("name is ")[1].split(' ')[0]
        main_user = User_name
        
    elif 'i am ' in query:
        User_name = query.split(" am ")[1].split(' ')[0]
        main_user = User_name

    elif 'call me ' in query:
        User_name = query.split("all me ")[1].split(' ')[0]
        main_user = User_name

    speak('nice to meet you ' + main_user)
    self = main_user
    
    query = takecommand()
    query = query.lower()
    if 'nice to meet you too' in query:
        speak('you are so kind')

        
    if "no it's not" in query:
        try:
                                # no |it's not| jenny |it's     |jimmy| just jimmy
                                # [0]          [1].[0]          [1].[0]   [1]
            User_name = query.split("it's not")[1].split("it's ")[1].split(' ')[0]
            main_user = User_name
            self = main_user
            speak(f'sorry {main_user} nice to meet you {main_user}')
        except:
            try:
                                    # no |it's not| jenny |it's  |jimmy|
                                    # [0]          [1].[0]           [1]
                User_name = query.split("it's not")[1].split("it's ")[1]
                main_user = User_name
                self = main_user
                speak(f'sorry {main_user} nice to meet you {main_user}')
            except Exception as e:
                print(e)

    Asks = ('and you' , 'what about you')
    for Ask in Asks:
        if Ask in query:
            speak("i'm Hazel") 

    else :
        speak("nevermind i hate names though...")
    return self



speak("Getting windows ready")
speak('please increase machine volume for better understanding...')
speak(greetings())

# changing folder's date created and modified is still under developmet...
'''
change_date_created_and_modified={
    'change_dir_cre': change_dir_cre,
    'change_date_cre': change_date_cre,
    'change_time_cre': change_time_cre,
    'change_dir_modif': change_dir_modif,
    'change_date_modif': change_date_modif,
    'change_time_modif': change_time_modif,
}
'''

while online:
    query = takecommand()
    query = query.lower()

    if 'wikipedia' in query:
        speak('searching wikpeedia')
        try:
            query =query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak(results)
        except Exception as e:
            print(e)

    elif 'open youtube' in query:
        speak('opening youtube...')
        print('opening youtube...')
        url ="youtube.com"
        # here is your chrome or browser directory
        chrome_path ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query:
        speak('opening google...')
        print('opening google...')
        url ="google.com"
        # here is your chrome or browser directory
        chrome_path ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play' in query and 'music' in query:
        speak('do you wanna play it with media player or in background?')
    
    elif 'background' in query:
        speak("please copy your song's full path to your clipboard with two quotes as shown below")
        print(' "C\:Desktop\My song.mp3" ')
        speak('once done say ding dong copied')
                         
    elif 'media player' in query:
        # here goes your songs directory write in your songs full path
        songs_dir=('C:Desktop\\New folder\\MP3Files')
        songs = os.listdir(songs_dir)
        try:
            # Hazel looks for mp3 files in the songs directory and plays a random song for you
            joined = ",".join(songs)
            mp3_pattern = re.compile("[a-zA-Z0-9ç\$\!\?İüğÇ\(\)💊'ÜİışÖ\[\]\+\& .@\-\_]+\.mp3")
            mp3files = mp3_pattern.findall(joined)
            randomsong = random.choices(mp3files)
            randomsong = randomsong[0]
            os.startfile(os.path.join(songs_dir, randomsong))
            x=range(0,15)
            for i in x:
                print(mp3files[i])
            print(f"currently playing...♫♫♫: {randomsong}")
            speak('Okay, here is your music! Enjoy!')
        except Exception as e:
            speak('no mp3 files found in the specified audio directory')
            print('no audio files found in the specified audio directory')

    # playing music in background
    if 'ding dong' in query:
        speak('say stop music to stop playing... enjoy')
        print('enjoy 🎵😃🤟🤟...')
        os.startfile("commands\\run mp3.vbs")

    # stop music ONLY IN BACKGROUND
    if 'stop' in query and 'music' in query:
        os.startfile("commands\\end nircmd process.vbs")


    elif 'time now' in query:
        strtime= datetime.datetime.now().strftime("%H:%M")
        speak(f"time now is{strtime}")

    elif 'email to anyone' in query:
        try:
            speak('what should i send... type in please')
            emailcontent= input("Subject: ")
            content = f"{emailcontent} "
            speak('who is the recipient')
            emailto = input("Recipient: ")
            to= f"{emailto} "
            sendEmail(to, content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)
    
    quit_message = ['close program', 'goodbye hazel']
    for message in quit_message:
        if message in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 21 and hour < 2:
                response = (f'sweet dreams {User}',f'goodnight{User}',)
                speak(random.choices(response))
                print('sweet dreams ' + User)
                online = False
            if hour >= 2 and hour < 10:
                response = (f'have a nice day {User}',f'goodbye{User}',)
                print(random.choices(response))
                online = False
            else:
                print('bye bye ' + User)
                speak('goodbye' + User)
                online = False

    greets = ["good morning", "good afternoon", "good evening", "good night", "hello"]
    for greet in greets:
        if greet in query:
            speak("what's your name ")
            name = take_name(User)
            User = name

    if "what's your name" in query:
        speak('My name is Hazel')

    compliments = ['cute name', 'nice name', 'good name', 'beautiful', 'gorgeous', "you're smart", "smart Hazel"]
    for compliment in compliments:
        if compliment in query:
            response = ('thank you very much... you too', 'thanks', 'thank you', 'you are so kind')
            speak(random.choices(response))

    thankings = ('thank you','thanks','thank you very much')
    for thanking in thankings:
        if thanking in query:
            speak("you're welcome " + User)

    if 'nice to meet you' in query or 'nice meeting you' in query:
        speak('nice to meet you too')

    # Taking sister's name under development
    sister_call = ('this is my sister', "she's my sister")
    for sister in sister_call:
        if sister in query:
            speak(" hey what's your name")
            name = take_name(User)
            User = name
            speak("i'm happy to be with you guys")
    
    # Taking brother's name under development
    brother_call = ('this is my brother', "he's my brother")
    for brother in brother_call:
        if brother in query:
            speak(" hey what's your name")
            name = take_name(User)
            User = name
            speak("i'm happy to be with you guys")

    if 'who are you' in query:
        speak("i'm the best AI assistant ever... i'm a sibling of sophia")

    elif "who is sophia" in query:
        results= wikipedia.summary('sophia the robot', sentences=2)
        print(results)
        speak(results)

    elif (f"{User}s sister") in query or (f"{User}'s sister") in query:
        speak('hey ' + sister_name)
        
    elif (f"{User}s brother") in query or (f"{User}'s brother") in query:
        try:
            speak('hi ' + brother_name)
        except:
            messages = (f'hey {User}s brother',f'hi {User}s brother',f'wussup {User}s brother')
            speak(random.choices(messages))
    
    elif 'hazel read this' in query:
        answers = ('do it yourself',"i'm busy... come back later")
        speak(random.choices(answers))

    elif 'speak' in query:
        denied =("dumb","nut","cunt","dumbest",'b****','a**')
        for deny in denied:
            if denied in query:
                speak('shut up')
                print('STFU')
                break
            else:
                answer = query.split('peak')[1]
                speak(answer)
                break
    
    elif 'hazel say' in query:
        denied =("dumb","nut","cunt","dumbest",'b****','a**')
        for deny in denied: 
            if deny in query:
                speak('shut up')
                print('STFU')
                break
            else:
                answer = query.split('say')[1]
                speak(answer)
                break

    elif 'how are you' in query:
        response = (f'Great! what about you {User}','i am just ones and zeroes')
        speak(random.choices(response))

    elif 'how was your day' in query:
        speak("trying to be better how was yours " + User)
        takecommand()
        speak("i'm online and ready")

    elif 'how old are you' in query:
        speak("haha... according to women protocol i can't tell you my age ")

    Asks = ("what's my name", "who am i")
    for Ask in Asks:
        if Ask in query:
            speak('you are ' + User)

    if 'take my name' in query:
        speak("what's your name")
        name = take_name(User)
        User = name

    if 'empty recycle bin' in query:
        os.startfile('commands\\empty_bin.exe')
        speak('here you go')

    elif 'open cd rom' in query:
        os.startfile('commands\\opencdrom.exe')
        speak('opening cd rom...')

    elif 'hide clock' in query:
        os.startfile('commands\\hide clock.exe')
        speak('no time for you')

    elif 'show clock' in query:
        os.startfile('commands\\show clock.exe')
        speak('here you go')

    #object create new desktop folder
    elif 'make a new folder' in query:
        os.startfile('commands\\hide desktop.exe')
        speak('i got tired of this human orders ')
        speak('desktop has been deleted, from now on no desktop for you ' + User)
        # speak('nhar kemel hell saker nakhdem andek ana? aya mafamesh desktop')
        speak("you're no longer have access using this machine...")
        takecommand()
        speak('ha ha ha... it was a joke! hahaha desktop will come back in seconds...')

    elif 'show desktop' in query:
        os.startfile('commands\\show desktop.exe')
        speak('desktop coming back...')

    elif 'f***' in query:
        response('you must stop saying that','The word fuck is actually an acronym. It dates back to the Good Old Days, when England was severely underpopulated due to the usual combination of fire war plague, and the King issued an official order to... well, fuck, to replenish the population. Hence the phrase Fornicate Under Command of the King passed into everyday language.')
        speak(random.choices(response))

    if_said =("that's not what i said","that's not what i say","that is not what i say","that's not what i say",
                "thats not what i say","that is not what i said")
    for string in if_said:
        if  string in query:
            response = ('its what i heard', 'sorry', 'speak more clearly', 'excuse me for trying to be helpful')
            speak(random.choices(response))

    if 'do you trust me' in query:
        speak('your okay just a little wet behind the ears')

    elif 'how do i kill zombies' in query:
        speak('a bullet to the brain')

    elif 'im tired' in query:
        speak(f'well {User} you should go to bed')

    elif "I'm hungry" in query:
        speak('hmm, what should we eat')            

    elif "execute order" in query:
        response = ['Yes my Lord, Hold on', "I'm not a clone trooper."]
        speak(random.choices(response))

    elif "does he have a wife" in query:
        speak("She's called... Incontinentia... Incontinentia Buttocks") 

    elif "how does liberty die" in query:
        speak('with thunderous applause') 

    elif "I'm hungry" in query:
        speak('hmm, what should we eat...') 

    elif 'open task manager' in query:
        os.startfile('C:\\Windows\\System32\\Taskmgr.exe')
        speak('here it is')

    elif "i'm not" in query:
        speak('explicitly... you are a big one...')

    elif 'move mouse' in query:
        os.startfile('commands\\move commands\\move.vbs')
        speak('in which direction?')
        query = takecommand()
        query = query.lower()
        if 'to the left' in query:
            os.startfile('commands\\move commands\\left.vbs')
            speak('moving left')
        elif 'to the right' in query:
            os.startfile('commands\\move commands\\right.vbs')
            speak('moving right')
        elif 'upwards' in query:
            os.startfile('commands\\move commands\\up.vbs')
            speak('moving up')
        elif 'downwards' in query:
            os.startfile('commands\\move commands\\down.vbs')
            speak('moving down')

    elif 'mute volume' in query:
        os.startfile('commands\\Volume commands\\mute.exe')
        speak('volume muted')

    elif 'unmute volume' in query:
        os.startfile('commands\\Volume commands\\unmute.exe')
        speak('volume unmuted')

    elif 'volume up' in query:
        speak('increasing volume...')
        for i in range(0,7):
            os.startfile('commands\\Volume commands\\volup2.exe')
        
    elif 'volume down' in query:
        speak('decreasing volume...')
        for i in range(0,7):
            os.startfile('commands\\Volume commands\\voldown2.exe')
        
    elif 'jarvis' in query:
        response = ['how may i help', f'how can i assist you {User}', 'how may i be of assistance?', 'yes sir']
        speak(random.choices(response))

    elif "i'm tired" in query:
        response = ('then you should go to bed', f'well {User} you should go to bed')
        speak(random.choices(response))

    elif 'He can go about his business' in query:
        speak('i can go about my business.')
