"""
                                ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                                ##                                                                                      ##
                                ##                    @author     : "Yassine Baghdadi"                                  ##
                                ##                    @version    : "1.0"                                               ##
                                ##                    @email      : "yassine.baghdadi.deve@gmail.com"                   ##
                                ##                    @github     : https://github.com/DeveYassineBaghdadi              ##
                                ##                                                                                      ##
                                ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
"""
import os
import sys

import pyautogui
import vlc
import json
import pytz
import time
import pyowm
import random
import pickle
import socket
import pygame
import pyjokes
import getpass
import pyttsx3
import os.path
import platform
import datetime
import wikipedia
import webbrowser
import googletrans
import wolframalpha
from os import path
import pygame.camera
import parsedatetime
from gtts import gTTS
from PIL import Image
from twilio.rest import Client
from selenium import webdriver
from playsound import playsound  # Todo: sudo apt-get install pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev
import speech_recognition as sr
import gender_guesser.detector as gender
from googleapiclient.discovery import build
from selenium.webdriver.common.keys import Keys
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from matrix_splash import *
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# pip install --upgrade google-api-python-client oauth2client
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

json_file = 'intents.json'



logo = """

                            \033[5m\033[2m
                             █████╗ ██╗     ███████╗██╗  ██╗     ██╗    ██████╗
                            ██╔══██╗██║     ██╔════╝╚██╗██╔╝    ███║   ██╔═████╗
                            ███████║██║     █████╗   ╚███╔╝     ╚██║   ██║██╔██║
                            ██╔══██║██║     ██╔══╝   ██╔██╗      ██║   ████╔╝██║
                            ██║  ██║███████╗███████╗██╔╝ ██╗     ██║██╗╚██████╔╝
                            ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝     ╚═╝╚═╝ ╚═════╝\033[0m
                                                   By:
                    ##================================================================##
                    ##                                                                ##
                    ##                        \033[1m\033[97mYassine Baghdadi\033[0m                        ##
                    ##                                                                ##
                    ##================================================================##
                \n\n\n
                    """

clear = 'cls' if str(platform.system()).lower() == 'windows' else 'clear'




class Main:
    def __init__(self):
        self.music_played = False
        self.lang = 'en-us'
        self.refresh()
        # self.vlc_instance = vlc.Instance()
        # self.player = self.vlc_instance.media_player_new()

    def validFN(self, x):
        return x.replace('<', '').replace(' ', '_').replace('>', '').replace(':', '').replace('"', '').replace('/', '').replace('|', '').replace('?', '').replace('*', '')#:"/\|?*

    def splash(self):
        try:

            print('\x1b[8;36;106t')  # resize terminal window
            time.sleep(0.5)
            doit()
            os.system(clear)
            print('\033c')

        except: pass
        print(logo)

    def refresh(self):
        if str(platform.system()).lower() != 'windows': self.splash()
        print(f'\t\t\t\t\t\033[34m\033[1mcollecting data ...\033[0m')

        self.json_data = json.loads(open('intents.json').read())
        self.INTENTS = self.json_data['INTENTS']
        self.ASS_NAME = str(self.json_data['INFO']['ASSISTANT']['name']).capitalize()
        self.USER = f"{self.get_gender(str(self.json_data['INFO']['USER']['name']))} {str(self.json_data['INFO']['USER']['name'])}"

        # tts = gTTS(self.USER, lang=self.lang)
        # fn = "aud/username.mp3"
        # tts.save(fn)

        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        self.PATH = os.path.join(desktop, 'Alex_data')

        if not os.path.isdir(self.PATH):
            os.mkdir(self.PATH)

        self.aud_dir = os.path.join(self.PATH, 'audios')
        if not os.path.isdir(self.aud_dir):
            os.mkdir(self.aud_dir)

        current_files = [str(f).replace('.mp3', '') for f in os.listdir(self.aud_dir) if os.path.isfile(os.path.join(self.aud_dir, f))]
        to_tts = []
        for i in self.INTENTS:
            if i != 'commands':
                for x in self.INTENTS[i]:
                        if self.validFN(x) not in current_files:
                            f = str(x).replace(' ', '_')
                            # gTTS(x.replace('_', ' '), lang=self.lang).save(os.path.join(self.aud_dir, f'{f}.mp3'))

                            to_tts.append(str(os.path.join(self.aud_dir, f'{self.validFN(f)}.mp3')))
        exceptions = [
            "just the first name please",
            "say What should i write in it after the beep",
            "say What you want to write in it after the beep",
            'your note created successfully',
            "to who ?",
            "what you want to send ?",
            "translate from english to what ?",
            "plaese start talking after the beep",
            "i have some issues on this part, please try to solve them",
            "Unfortunately i did not get a proved answer from wikipedia, i will try on google search",
            "good morning",
            "good morning",
            "good morning"

        ]
        for i in exceptions:
            if self.validFN(i) not in current_files:
                # ttc = gTTS(i.replace('_', ' '), "en-us")
                i = str(i).replace(' ', '_')
                # ttc.save(os.path.join(self.aud_dir, f"{i}.mp3"))
                to_tts.append(str(os.path.join(self.aud_dir, f'{self.validFN(i)}.mp3')))

        for i in self.json_data['INFO']['ASSISTANT']['description']:
            if self.validFN(i) not in current_files:
                i = str(i).replace(' ', '_')
                to_tts.append(str(os.path.join(self.aud_dir, f'{self.validFN(i)}.mp3')))

        for t in to_tts:
            gTTS(os.path.basename(t).replace('.mp3', '').replace('_', ' '), lang=self.lang).save(t)


        dirs = ['Desktop', 'Documents', 'Downloads', 'Pictures', 'Videos', 'Music']
        ext = ['mp3', 'mpeg']
        self.music_tracks = []
        for dir in dirs:
            for root, dirs_, f1 in os.walk(os.path.join(os.path.expanduser('~'), dir)):
                for f_ in f1:
                    ff = str(f_).split('/')[-1].split(f'.{str(f_.split(".")[-1])}')[0]
                    if str(f_.split(".")[-1]) in ext and ff not in current_files:
                        self.music_tracks.append(os.path.join(root, f_))

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        self.welcome()

    def welcome(self):

        greeting = self.INTENTS['GREETING']

        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            # greeting.pop(greeting.index("good morning"))
            greeting.pop(greeting.index("good afternoon"))
            greeting.pop(greeting.index("Good Evening"))

        elif hour >= 12 and hour < 18:
            # greeting.pop(greeting.index("good afternoon"))
            greeting.pop(greeting.index("good morning"))
            greeting.pop(greeting.index("Good Evening"))

        else:
            greeting.pop(greeting.index("good afternoon"))
            greeting.pop(greeting.index("good morning"))
            # greeting.pop(greeting.index("Good Evening"))



        if not self.USER:
            playsound(f'{self.aud_dir}/{self.validFN(random.choice(self.INTENTS["get_user_name_Q"]))}.mp3')
            while True:
                name = self.listen_(False)
                if name and len(name.split(' ')) == 1:
                    # self.say(f"{random.choice(self.INTENTS['GREETING_first_time'])} {self.get_gender(name)} {name} !, how can i help you ?")
                    with open(json_file, 'r+') as f:
                        self.json_data["INFO"]["USER"]["name"] = str(name)
                        f.seek(0)
                        json.dump(self.json_data, f, indent=4)
                        f.truncate()

                    self.refresh()
                    self.say(f'{random.choice(["nice to meet you ", "its great to meet you ", "its pleasure to meet you ", "am glad to meet you"])} {self.USER}, please say "alex" for start listen to you .')
                    playsound(os.path.join(self.aud_dir, f'{self.validFN(random.choice(self.INTENTS["give_help"]))}.mp3'))
                    return
                else:
                    playsound(os.path.join(self.aud_dir, f"{self.validFN('just_the_first_name_please')}.mp3"))

        greet = random.choice(greeting)
        g2 = random.choice(self.INTENTS['give_help'])

        print(f"{self.ASS_NAME} : {greet.replace('_', ' ')}, {g2.replace('_', ' ')}")

        playsound(os.path.join(self.aud_dir, f"{self.validFN(greet)}.mp3"))
        playsound(os.path.join(self.aud_dir, f"{self.validFN(g2)}.mp3"))

    def get_gender(self, n):
        name_ = str(n).capitalize()
        if gender.Detector().get_gender(name_) == 'female' or gender.Detector().get_gender(name_) == 'mostly_female':
            return 'madame'
        else:
            return 'Mister'

    def google_auth(self): #TODO bag

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'src/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)
        return service

    def is_connected(self):
        try:
            host = socket.gethostbyname("216.58.206.228")
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:
            return False

    def get_events(self, date, service):
        utc = pytz.UTC

        start_date = datetime.datetime.combine(date, datetime.datetime.min.time()).astimezone(utc)
        end_date = datetime.datetime.combine(date, datetime.datetime.max.time()).astimezone(utc)
        events_result = service.events().list(calendarId='primary', timeMin=start_date.isoformat(),
                                              timeMax=end_date.isoformat(),
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            self.say('No upcoming events found.')
        else:
            self.say(f'you have {len(events)} events for this date.')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start + event['summary'])
                time_ = f"{str(start).split('T')[1].split('-')[0].split(':')[0]}, {str(start).split('T')[1].split('-')[0].split(':')[1]}"
                if int(str(start).split('T')[1].split('-')[0].split(':')[0]) <= 12:
                    time_ += ' am'
                else:
                    time_ = f"{int(str(start).split('T')[1].split('-')[0].split(':')[0]) - 12}, {str(start).split('T')[1].split('-')[0].split(':')[1]}"
                    time_ += ' pm'
                print(time_)
                self.say(f"{event['summary']}, at {time_}")

    def say(self, txt, print_ = True):

        f = 'temp.mp3'
        gTTS(txt, lang=self.lang).save(f)

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        if print_:
            print(f'{self.ASS_NAME} : {txt} \n')
        replay = False
        if self.music_played:
            self.music('pause')
            replay = True
        playsound(f)
        os.remove(f)

        if replay:
            self.music('resume')


    def listen_(self, print_ = True):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        if print_:
            print('\n\033[32m\033[1m\033[5mListening ...\033[0m')

        self.said = ''
        replay = False
        if self.music_played:
            self.music('pause')
            replay = True
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                r.adjust_for_ambient_noise(source)
                self.said = r.recognize_google(audio)
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f"{self.USER} : {self.said}\n")
            except sr.UnknownValueError:
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                s = random.choice(self.INTENTS['UNDERSTAND_ESSUE'])
                print('', end='')
                playsound(f'aud/{self.validFN(s)}.mp3')

            except Exception as e:
                print(f'ERROR in listening function: {e}')
                exit()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        print(' ')
        if replay:
            self.music('resume')
        return self.said.lower()

    def get_date(self, txt):
        try:
            p = parsedatetime.Calendar()
            date = p.nlp(txt)[0][0].date()
            return date
        except Exception as e:
            print(e)
            return None

    def get_email(self):
        frommail = ''
        self.say('add an email address')
        while str(frommail).split('@')[1] != 'gmail.com':
            frommail = input('add email (i\'ll keep it for you): ')

        with open(json_file, 'r+') as f:
            data = json.load(f)
            data['INFO']['USER']['email'] = frommail
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        return frommail

    def sendEmail(self):
        self.say('creating mail,')
        tomail = input('send mail to : ')
        msg = ''
        self.say('you will write or say the content ?.')
        answer = self.listen_()
        if 'write' in answer:
            msg = input('Message : ')
        elif 'say' in answer:
            print('\033[5msay your mail message \033[0m')
            msg = self.listen_()
            # sys.stdout.write('\x1b[1A')
            # sys.stdout.write('\x1b[2K')
        frommail = self.json_data['INFO']['USER']['email']
        if not frommail:
            frommail = self.get_email()

        self.say('confirm your email address please .')
        print(f'{frommail} (say : yes/no) : ')
        if 'no' in self.listen_():
            frommail = self.get_email()

        pssw = getpass.getpass(prompt=f'Enter password for "{frommail}" (it safe) : ')

        server = smtplib.SMTP('smtp.gmail.com', 587)  # todo bug -- NameError: name 'smtplib' is not defined
        server.ehlo()
        server.starttls()

        server.login(frommail, pssw)
        server.sendmail(frommail, tomail, msg)
        server.close()

    def wikipedia_search(self, key):
        key = key.replace("wikipedia", "")
        self.say(f'Searching Wikipedia for {key}...')
        k = ['that\'s what i found, ', 'the answer is, ', 'i think the answer is, ', 'here is what i found on Wikipedia, ']
        results = f'{wikipedia.summary(key, sentences=3)}'
        # self.say("According to Wikipedia")
        f = 'temp.mp3'
        gTTS(f'{random.choice(k)}, {results} .', lang=self.lang).save(f)
        replay = False
        if self.music_played:
            self.music('pause')
            replay = True

        self.wplayer = vlc.MediaPlayer(f)
        self.wplayer.audio_set_volume(75)
        self.wplayer.play()
        print(f"{str(self.json_data['INFO']['ASSISTANT']['name'])} : {random.choice(k)}, {results}")



    def open_url(self, url):

        self.say(f'going to {url.replace("http://www.", "").replace("https://www.", "")} ...')
        if platform.system() == 'Windows':
            self.brower = webdriver.Chrome(executable_path=path.join(path.dirname(__file__), "src/chromedriver.exe"))
        else:
            self.brower = webdriver.Chrome(executable_path=path.join(path.dirname(__file__), "src/chromedriver"))
        if self.json_data['links'][url]:
            self.brower.get(url)
            return
        self.google_serch(url)

    def google_serch(self, key):
        key = key.replace('google', '').replace('alex', '').replace('hey', '').replace('hello', '')
        self.say(f'searching on google')
        # self.open_url('http://www.google.com')
        if platform.system() == 'Windows':
            self.brower = webdriver.Chrome(executable_path=path.join(path.dirname(__file__), "src/chromedriver.exe"))
        else:
            self.brower = webdriver.Chrome(executable_path=path.join(path.dirname(__file__), "src/chromedriver"))

        self.brower.get('http://www.google.com')
        self.brower.maximize_window()
        search = self.brower.find_element_by_name('q')
        search.send_keys(key)
        search.send_keys(Keys.RETURN)

    def open_app(self, app):
        try:
            self.say(f'Trying to open {app} ...')
            os.system(app)
        except:
            self.say(f'sorry i could not open {app} ...')

    def joke(self):
        self.say(pyjokes.get_joke())

        playsound(f"aud/laugh{random.randint(0, 2)}.mp3")

    def wolframe_serach(self, query):
        try:
            client = wolframalpha.Client("8YPXJH-PX8LJTH2PP")
            res = client.query(query)
            k = ['that what i found, ', 'the answer is, ', 'i think the answer is, ',
                 'here is what i found on internet, ']
            answer = f'{random.choice(k)}{next(res.results).text}'
            f = 'temp.mp3'
            gTTS(answer, lang=self.lang).save(f)
            if self.music_played:
                self.music('pause')

            self.wplayer = vlc.MediaPlayer(f)
            self.wplayer.audio_set_volume(75)
            self.wplayer.play()
            print(answer)
        except AttributeError:
            self.google_serch(query)

    def music(self, q):

        state = ''
        if self.music_tracks:
            try:
                state = str(self.player.get_state()).split('.')[1].lower()
            except:
                pass

            if 'play' in q:
                if state == 'playing':
                    print(f'{self.track.split("/")[-1]} already played (say (pause OR stop OR change) + music')
                else:
                    self.track = random.choice(self.music_tracks)
                    self.player = vlc.MediaPlayer(self.track)
                    self.player.audio_set_volume(75)
                    self.player.stop()
                    self.player.play()
                    self.Vol = int(self.player.audio_get_volume())
                    self.music_played = True
                    print(f'\033[2mmusic played \033[0m: {self.track.split("/")[-1]}')


            elif 'pause' in q:
                if state == 'playing':
                    self.player.pause()
                    self.music_played = False

            elif 'stop' in q:
                if state == 'playing':
                    self.player.stop()
                    self.music_played = False


            elif 'resume' in q:
                if state == 'paused':
                    self.player.play()
                    self.music_played = True

            elif 'change' in q:
                self.player.stop()
                self.music('play')

            elif 'down' in q or 'low' in q or 'lower' in q:
                self.Vol = int(self.player.audio_get_volume()) - 10
                self.player.audio_set_volume(self.Vol)

            elif 'raise' in q or 'upraise' in q or 'up':
                if int(self.player.audio_get_volume()) <= 75:
                    self.Vol = int(self.player.audio_get_volume()) + 10
                    self.player.audio_set_volume(self.Vol)
                else:
                    print(
                        f'\033[97m\033[41m\033[5m  Warning : \033[0m \033[31mvolume is \033[1m\033[4m{int(self.player.audio_get_volume())}%\033[0m\033[31 and this so high for your Ears, please make it lower\033[0m')
            else:
                self.say('incorrect command say play or pause or stop music ')

        else:
            try:
                os.system('spotify')
            except:
                self.say('i haven\'t find any, but i will open it on youtube')
                self.open_url(
                    'https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbUFoSmV6TVhZY0RqWHZlQzZmak84OQ%3D%3D')

    def get_weather(self, city):
        try:
            owm = pyowm.OWM('7c612686bc962b4f2e388ff3f26ba43f')
            # owm = pyowm.OWM('a930aa35ee42cf74b1a2ea7b4fdf4dec')
            # weath = owm.weather_around_coords(lat=34.225997, lon=-3.351764)
            weath = owm.weather_at_place(city).get_weather().get_temperature('celsius')
            return weath
        except:
            self.google_serch(f'{city} weather')

    def take_pic(self):

        now = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        pic_name = os.path.join(self.PATH, f'alex_pic_{now}.jpg')
        pygame.camera.init()
        cams = pygame.camera.list_cameras()
        cam = pygame.camera.Camera(cams[0], (640, 480))
        cam.start()
        time.sleep(0.1)
        img = cam.get_image()
        pygame.image.save(img, pic_name)
        cam.stop()

        img_ = Image.open(pic_name)
        img_.show()

    def take_note(self):
        now = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        # self.say("say What should i write in it after the beep")
        playsound(random.choice([os.path.join(self.aud_dir, f'{self.validFN("say_What_you_want_to_write_in_it_after_the_beep")}.mp3'),
                                 os.path.join(self.aud_dir, f'{self.validFN("say_What_should_i_write_in_it_after_the_beep")}.mp3')]))
        playsound(f'aud/beep.aif')
        # self.player = vlc.MediaPlayer('beep.aif')
        # self.player.play()

        note = self.listen_()
        if 'cancel' in note.lower() or 'never mind' in note.lower():
            self.say('operation canceled .')
            return
        file = os.path.join(self.PATH, f"alex_note_{now}.txt")
        with open(file, 'w') as f:
            f.write(f'{note} .')

        vlc.MediaPlayer(os.path.join(self.aud_dir, f"{self.validFN('your note created successfully')}.mp3")).play()
        webbrowser.open(file)

    def send_SMS(self):
        # self.say('to who ?')
        vlc.MediaPlayer(os.path.join(self.aud_dir, f"{self.validFN('to who ?')}.mp3")).play()

        to = str(input('send SMS to : '))

        self.say('what you want to send ?')
        vlc.MediaPlayer(os.path.join(self.aud_dir, f"{self.validFN('what you want to send ?')}.mp3")).play()

        msg = self.listen_()
        account_sid = 'AC5fb41b8756e48118cc8db0c019bfc43d'
        auth_token = 'b0c82483b8992bcc8f4ce6110fa2dd23'
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=f'"{msg}"',
            from_='+18577635294',
            to=to
        )
        self.say(f'SMS sent .to : {to}')

    def translate(self):

        trs = googletrans.Translator()
        langs = googletrans.LANGCODES
        while True:

            playsound(os.path.join(self.aud_dir, f'{self.validFN("translate_from_english_to_what_?")}.mp3'))
            a = self.listen_()
            try:
                l = langs[a]
                print(l)
                break
            except KeyError:
                print(f'{a} isnt lang')

        txt = ''
        while not txt:
            playsound(os.path.join(self.aud_dir, f'{self.validFN("plaese_start_talking_after_the_beep")}.mp3'))
            playsound(os.path.join(os.getcwd(), 'aud', 'beep.aif'))
            txt = self.listen_()
        try:
            nTxt = trs.translate(text=txt, dest=l, src='en')
            print(nTxt)
            if nTxt:
                try:
                    f = 'temp.mp3'
                    gTTS(txt, lang=l).save(f)
                    playsound(f)
                    os.remove(f)
                except Exception as e:
                    print(f'error : {e}')
        except Exception as e:
            print(f'ERROR -.{e}')


if __name__ == '__main__':

    # todo json intents : "GREETING_first_time, GREETING, GOOD_BYE, UNDERSTAND_ESSUE, THANK"
    m = Main()
    try:
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.record(source, duration=5)
                try:
                    text = ''
                    try:
                        text = r.recognize_google(audio).lower()
                    except:pass
                    # if str(m.json_data['INFO']['ASSISTANT']['name']).lower() in text:
                    if 'alex' in text.split():

                        try:
                            m.wplayer.stop()
                        except: pass

                        wake = random.choice(m.INTENTS['wake'])
                        print(f"{m.ASS_NAME} : {str(wake).replace('_', ' ')}\n")
                        playsound(os.path.join(m.aud_dir, f"{m.validFN(wake)}.mp3"))
                        query = m.listen_()

                        if ('what i have' in query or 'my events' in query):
                            playsound(os.path.join(m.aud_dir, f'{m.validFN("i_have_some_issues_on_this_part,_please_try_to_solve_them")}.mp3'))
                            # s = m.google_auth()
                            # m.get_events(m.get_date(query), s)



                        elif ('send' in query or 'create' in query or 'new' in query) and 'email' in query:
                            m.sendEmail()

                        elif 'search' in query:
                            r = random.choice(m.INTENTS['search'])
                            print(f"{m.ASS_NAME} : {str(r).replace('_', ' ')}")
                            playsound(os.path.join(m.aud_dir, f"{m.validFN(r)}.mp3"))
                            q = m.listen_()
                            # q = q.replace('search', '').replace('what\'s', '').replace('which', '').replace(
                            #     'what', '').replace('why', '').replace('how', '').replace('who', '').replace('where',
                            #                                                                                  '').replace(
                            #     'are', '').replace('is', '').replace('for', '').replace('alex', '')
                            if 'wikipedia' in query:
                                try:
                                    m.wikipedia_search(q)
                                except:
                                    vlc.MediaPlayer(os.path.join(m.aud_dir, f'{m.validFN("Unfortunately_i_did_not_get_a_proved_answer_from_wikipedia,_i_will_try_on_google_search")}.mp3')).play()
                                    m.google_serch(q)
                            else: m.google_serch(q)

                        elif 'joke' in query:
                            m.joke()

                        elif 'open' in query or 'go to' in query:
                            site = query.replace('open', '').replace('go to', '')
                            m.open_url(site)

                        elif 'start' in query:
                            m.open_app(
                                query.replace('start', '').replace('please', '').replace('for me', '').replace(
                                    'can you', '').replace(m.ASS_NAME, ''))

                        elif 'weather' in query:
                            if 'for' in query or 'of' in query:
                                try:
                                    m.get_weather(
                                        query.replace('weather', '').replace('for', '').replace('of', '').replace(
                                            'today', ''))
                                except:
                                    m.google_serch(query)
                            else:
                                try:
                                    m.get_weather(m.json_data['INFO']['USER']['city'])
                                except:
                                    m.google_serch(f"{query} {m.json_data['INFO']['USER']['city']}")

                        elif 'music' in query:
                            m.music(query)

                        elif ('take' in query or 'get' in query) and ('picture' in query or 'pictures' in query or 'photo' in query):
                            print("taking a picture")
                            [playsound(os.path.join(os.getcwd(), 'aud', f'{m.validFN(str(i))}.mp3')) for i in [3, 2, 1]]
                            m.take_pic()
                            vlc.MediaPlayer(os.path.join(os.getcwd(), 'aud', 'pic.mp3')).play()

                        elif 'take' in query and 'note' in query:
                            m.take_note()

                        elif 'sms' in query:
                            m.send_SMS()

                        elif 'exit' in query or 'bye' in query or 'goodbye' in query or 'stop' in query:
                            playsound(os.path.join(m.aud_dir, f"{m.validFN(random.choice(m.INTENTS['GOOD_BYE']))}.mp3"))
                            os.system(clear)
                            doit()
                            print(logo)
                            exit()

                        elif ('shutdown' in query or 'off' in query) and 'computer' in query:
                            m.say(f'the computer will shutdown in 1 minute, {random.choice(m.INTENTS["GOOD_BYE"])}')
                            time.sleep(0.5)
                            os.system('shutdown')
                            time.sleep(0.5)
                            os.system(clear)
                            doit()
                            print(logo)



                        elif ('what is' in query or 'what\'s' in query or 'what' in query ) and 'time' in query:
                            m.say(datetime.datetime.now().strftime('%H:%M'))

                        elif ('what is' in query or 'what\'s' in query or 'what' in query ) and ('date' in query or 'dates' in query):
                            if 'for' in query or 'in' in query or 'next' in query or 'tomorrow' in query or 'was' in query or 'of' in query:
                                try:
                                    p = parsedatetime.Calendar()
                                    date = p.nlp(query)[0][0].date()
                                    m.say(date)
                                except: m.say(f"sorry i can't find this date, but today is {datetime.datetime.now().strftime('%m-%d-%Y')} anyway")
                            else:m.say(f" {datetime.datetime.now().strftime('%m-%d-%Y')} .")

                        elif ('make' in query or 'take' in query or 'do' in query ) and 'screenshot' in query:
                            myScr = pyautogui.screenshot()
                            now = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
                            pt = os.path.join(m.PATH, f'alex-screenshot-{now}.png')
                            myScr.save(pt)
                            time.sleep(2)
                            img = Image.open(pt)
                            img.show()

                        elif 'how you work' in query or 'how do you work' in query or 'how can you help' in query or 'commends' in query or 'your rules' in query or 'the rules' in query or 'help' in query:
                            commands = m.INTENTS['commands']

                            m.say(f'i can help you with {len(commands)} operations so far :')
                            for x in commands:
                                print(f'\t#\t{x.capitalize()} \033[5m==>\033[0m {commands[x].capitalize()} .\n')
                                # m.say(commands[x].capitalize(), False)
                            print()

                            m.say('just say alex and i will be there for you', False)
                            for i in range(len(commands)):
                                sys.stdout.write('\x1b[1A')
                                sys.stdout.write('\x1b[2K')



                        elif 'created you' in query or 'made you' in query or 'maker name' in query or 'your father' in query:
                            r = random.choice(m.INTENTS['made_reponses'])
                            print(f'{m.ASS_NAME} : {r} .')
                            playsound(os.path.join(m.aud_dir, f'{m.validFN(r)}.mp3'))


                        elif 'not funny' in query:
                            m.say('take this ')
                            m.joke()


                        elif 'refresh' in query or 'reload' in query or 'rebuild' in query :
                            m.refresh()

                    elif 'hi' in text or 'hey' in text or 'hey' in text or 'hay' in text or 'hello' in text:
                        r = random.choice(m.INTENTS['GREETING'])
                        print(f'{m.ASS_NAME} : {r.replace("_", " ")}')
                        try:
                            playsound(os.path.join(m.aud_dir, f"{m.validFN(r)}.mp3"))
                        except:
                            m.say(r, False)

                    elif 'and you' in text or 'what about you' in text:
                        r = random.choice(m.INTENTS['howdy_reponses'])
                        print(f'{m.ASS_NAME} : {r.replace("_", " ")}')
                        playsound(os.path.join(m.aud_dir, f"{m.validFN(r)}.mp3"))

                    elif 'how are you' in text or 'how do you do' in text or 'howdy' in text or 'are you fine' in text or 'are you ok' in text:
                        r = random.choice(m.INTENTS['howdy_reponses'])
                        print(f'{m.ASS_NAME} : {r.replace("_", " ")}')
                        playsound(os.path.join(m.aud_dir, f"{m.validFN(r)}.mp3"))

                    elif 'who are you' in text or 'about you' in text or 'your name' in text:
                        r = random.choice(m.json_data["INFO"]["ASSISTANT"]["description"]).replace('_', ' ')
                        print(f'{m.ASS_NAME} : {r}')
                        playsound(os.path.join(m.aud_dir, f"{m.validFN(r)}.mp3"))

                # except sr.WaitTimeoutError as e:
                #     print("Timeout; {0}".format(e))
                # except sr.UnknownValueError:
                #     pass
                except Exception as e:
                    pass

    except KeyboardInterrupt:
        print('\nexit ...')
        if str(platform.system()).lower() != 'windows': m.splash()

    # except Exception as e:
    #     print(f'{e}\nExiting ...')
    #     exit()
