from lib2to3.pytree import convert
import json
from opencc import OpenCC
from turtle import position
import pyautogui as pt
import pyperclip as pc 
from pynput.mouse import Controller ,Button
from time import sleep
from whatsapp_response import response
import traceback
import chatterBot
from chatterbot import ChatBot
from chatterbot.response_selection import get_first_response
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from PIL import Image
import pytesseract
mouse = Controller()
# converter = OpenCC('s2hk')
# bot = ChatBot("Zadis",logic_adapters=[{                       
#                     'import_path': 'chatterbot.logic.BestMatch',
#                     "statement_comparision_function": "chatterbot.comparisions.levenshtein_distance",
#                     "response_selection_method": "get_first_response"
#                     }])
# # bot.set_trainer(ListTrainer)
# trainer=ChatterBotCorpusTrainer(bot)
# # bot.set_trainer(ChatterBotCorpusTrainer)
# trainer.train("chatterbot.corpus.chinese")
# trainer.train("chatterbot.corpus.english")
class WhatsApp:
    def __init__(self,speed=.5,clickspeed = .3,phoneNumber = 1234) :
        self.phoneNumber = phoneNumber
        self.speed = speed
        self.clickspeed = clickspeed
        self.message = ''
        self.lastMessage = ''
        self.applicationName='chrome'
    def findApplication(self):
        pt.keyDown('command')
        pt.press('space')
        pt.keyUp('command')
        pt.write(self.applicationName)
        pt.hotkey('enter')
    def nav_green_dot(self):
        try:
            sleep(2)
            position = pt.locateOnScreen('assets/green_dot.png',confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.clickspeed)
        except Exception as err:
            print('Exception',err)
            traceback.print_exc()
    def nav_input_box(self):
        try:
            sleep(2)
            position = pt.locateOnScreen('assets/paperclip.png',confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(100,10,duration=self.speed)
            pt.doubleClick(interval=self.clickspeed)
        except Exception as err :
            print('Exception',err)
            traceback.print_exc()
    def nav_message(self):
        try:
            sleep(3)
            position = pt.locateOnScreen('assets/paperclip.png',confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(10,-50,duration=self.speed)
        except Exception as err :
            print('Exception',err)
            traceback.print_exc()
    def get_url(self):
        try:
            pt.hotkey('command','t')
            position = pt.locateOnScreen('assets/googleSearch.png',confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(10,0,duration=self.speed)
            pt.doubleClick(interval=self.clickspeed)
            pt.write('wa.me/852'+str(self.phoneNumber))
            pt.press('enter')
        except Exception as err :
            print('Exception',err)
            traceback.print_exc()
    def get_message(self):
        sleep(5)
        mouse.click(Button.left,3)
        sleep(self.speed)
        mouse.click(Button.right,1)
        sleep(self.speed)
        pt.moveRel(10,10,duration=self.speed)
        mouse.click(Button.left,1)
        sleep(1)
        self.message = pc.paste()
    
    def send_message(self,article):
        try:
            # if self.message != self.lastMessage:
            # usersay = response(self.message)
            # bot_response = 'bot testing'
            # print(usersay)
            # bot_response = bot_response.encode('UTF-8')
            #bot_response = bot.get_response(usersay)
         
            bot_response =article
            #bot_response = converter.convert(bot_response)
            # print(bot_response)
            # attachment = Image.open('assets/attachment.jpeg')
            # textattachment = pytesseract.image_to_string(Image.open(attachment),lang="eng")
            # textattachment= attachment.copy()
            pc.copy(bot_response)
            pt.keyDown('command')
            pt.press('v')
            pt.keyUp('command')
            # pt.write(textattachment,interval=.2)
            pt.press('enter')
            print('YOU SAY : ',bot_response)
            self.lastMessage = self.message
            # else:
            #     print("No new Message ....")
        except Exception as err :
            print('Exception',err)
            traceback.print_exc()
    def closeGoogleTab(self):
        try:
            pt.keyDown('command')
            pt.press('w')
            pt.keyUp('command')
        except Exception as err :
            print('Exception',err)
            traceback.print_exc()
# f =open('assets/phoneNumber11.json')
# data = json.load(f)
# for i in data:             
#     # wa_bot = WhatsApp(speed=.5,clickspeed=.4,phoneNumber=53007785)
#     wa_bot = WhatsApp(speed=.5,clickspeed=.4,phoneNumber=i['phoneNumber'])
#     sleep(2)
#         # wa_bot.nav_green_dot(

#     wa_bot.findApplication()
#     wa_bot.closeGoogleTab()
#     wa_bot.get_url()
#     wa_bot.nav_message()
#     # wa_bot.get_message()
#     wa_bot.send_message()
#     sleep(30)
def webController(phoneNumber,article):
    wa_bot = WhatsApp(speed=.5,clickspeed=.4,phoneNumber=phoneNumber)
    sleep(2)
    wa_bot.findApplication()
    wa_bot.closeGoogleTab()
    wa_bot.get_url()
    wa_bot.nav_message()
    wa_bot.send_message(article)
    sleep(30)
# wa_bot.send_message()
# wa_bot.nav_message()
# wa_bot.get_message() 
# wa_bot.nav_input_box()
# wa_bot.send_message()