
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import time
import keyboard 
import shutil
from selenium import webdriver
import pyautogui



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
att_dir=r'C:\Users\naman\OneDrive\Desktop\ATTACHMENTS'

attachment_dir='C:/Users/naman/OneDrive/Desktop/ATTACHMENTS'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def remove(string): 
    return string.replace(" ", "") 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")   
  
    else:
        speak("Good Evening Sir !")  
  
    assname =("jason ")
    speak("I am your Assistant")
    speak(assname)

def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
     
    return query

def facebook() :
    
    operation=True
    driver = webdriver.Chrome('C:/Users/naman/OneDrive/Desktop/automation project/chromedriver.exe') 
    driver.get('https://www.facebook.com')
    driver.implicitly_wait(60)
    driver.find_element_by_id('email').send_keys('namanrocks84@gmail.com')
    driver.find_element_by_id('pass').send_keys('namanjain2706')
    driver.find_element_by_id('u_0_b').click()
    
    time.sleep(3)
    
    driver.maximize_window()
    speak("WELCOME TO FACEBOOK")
    
    while operation:
        
        command=takeCommand().lower()
        
        
        if 'log out' in command:
            speak('LOGGING YOU OUT ')
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/i').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span').click()
            operation=False
            
        if 'post content' in command:
            speak('SAY THE CONTENTS')
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span').click()
            time.sleep(3)
            
            
            
        if 'attachment'in command :
            
            speak('OK ADDING ATTACHMENT')
            time.sleep(2)

            os.chdir('C:/Users/naman/OneDrive/Desktop/screenshots')
            b=pyautogui.locateCenterOnScreen('att.png')
            pyautogui.click(b[0],b[1])
            
            li=os.listdir(attachment_dir)
            for i in range(0,len(li)):
                final_str=""
                final_str='"'+att_dir+'\\'+li[i]+'"'
                time.sleep(3)
                pyautogui.typewrite(final_str)
                print(final_str)
            pyautogui.keyDown('enter')


            

def gmail():
    url = 'https://www.gmail.com'
    gmail_username = 'naman.jain19@vit.edu'
    gmail_password = 'vit1234$'
    driver = webdriver.Chrome('C:/Users/naman/OneDrive/Desktop/automation project/chromedriver.exe')
    driver.get(url)

    driver.implicitly_wait(60)
    driver.find_element_by_id('identifierId').send_keys(gmail_username)
    driver.find_element_by_id('identifierNext').click()

    driver.implicitly_wait(60)
    driver.find_element_by_name('password').send_keys(gmail_password)
    driver.find_element_by_id('passwordNext').click()
    driver.maximize_window()
    
    speak("YOU HAVE LOGGED IN  INTO GMAIL")

    further_cmd=True
    while further_cmd :
        cmd=takeCommand().lower()
        if 'compose mail' in cmd :
            speak('composing mail ')
            driver.find_element_by_id(':iw').click()
            time.sleep(2)
            speak('TO WHOM TO SEND MAIL')
            
            to_address=takeCommand().lower()
            toadd=remove(to_address)
            time.sleep(1)
            driver.find_element_by_id(':o9').send_keys(toadd)
           
            
                
            
        if 'search' in cmd :
            speak("What to search")
            time.sleep(2)
            reply=takeCommand().lower()
            edited_reply=remove(reply)
            
            driver.find_element_by_class_name('gb_of').send_keys(edited_reply)
            pyautogui.keyDown('enter')
        
        if 'attachment' in cmd :
            speak("OK")
            os.chdir('C:/Users/naman/OneDrive/Desktop/screenshots')
            time.sleep(3)
            b=pyautogui.locateCenterOnScreen('ga.png')
            pyautogui.click(b[0],b[1])
            time.sleep(3)
            li=os.listdir(attachment_dir)
            for i in range(0,len(li)):
                final_str=""
                final_str='"'+att_dir+'\\'+li[i]+'"'
                time.sleep(3)
                pyautogui.typewrite(final_str)
                print(final_str)
            pyautogui.keyDown('enter')
            
        if 'send mail'in cmd:
            driver.find_element_by_xpath('//*[@id=":nh"]').click()
                
                

        if 'log out' in cmd :
            speak("logging you out")
            driver.find_element_by_class_name('gb_la').click()
            
            driver.find_element_by_id('gb_71').click()
            further_cmd =False
            driver.close()
            return True

def application() :
    cont=True
    speak('WHAT YOU WANT ME TO OPEN ')
    time.sleep(1)
    

    while cont:
        app=takeCommand().lower()
        if 'ms excel' in app:
            speak('HERE YOU  GO  ')
            os.startfile('C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe')
            cont=False

        if 'powerpoint' in app:
            speak('HERE YOU  GO  ')
            os.startfile('C:/Program Files/Microsoft Office/root/Office16/POWERPNT.exe')
            cont=False

        if 'ms word' in app:
            speak('HERE YOU  GO  ')
            os.startfile('C:/Program Files/Microsoft Office/root/Office16/WINWORD.exe')
            cont=False


def music(a):
              
    music_dir = "C:/Users/naman/OneDrive/Desktop/SONGS"
    songs = os.listdir(music_dir)
    if a > len(songs):
        a=0
    if a<0 :
        a=len(songs)-1
    
    os.startfile(os.path.join(music_dir, songs[a]))

 
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    a=True
    i=0  
    #clear()
    #wishMe()
    #usrname()
   
   
    
    while a:
         
        query = takeCommand().lower()
        if 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            speak("Here you go to facebook\n")
            facebook()

        elif 'open gmail' in query:
            speak("Here you go to gmail\n")
            
            a=gmail()

        elif 'play music' in query :
            speak("Here you go with music")
            music(i)
        elif'next song' in query:
            speak("OK changing song ")
            i=i+1
            music(i)
        elif'previous song' in query:
            speak("OK changing song ")
            i=i-1
            music(i)

        elif'open application' in query:
            application()
        
        elif 'search google' in query :
            
            driver = webdriver.Chrome('C:/Users/naman/OneDrive/Desktop/automation project/chromedriver.exe')
            driver.get('https://www.google.com')
            driver.maximize_window()
            time.sleep(1)
            speak("what to search")
            sea=takeCommand().lower()

            pyautogui.write(sea)
            pyautogui.keyDown('enter')
        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jason from listening commands")
            time.sleep(2)
            a = int(takeCommand())
            time.sleep(a)
            
            
            
            

        
            
            


 