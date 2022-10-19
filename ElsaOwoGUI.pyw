import datetime
from time import sleep
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import messagebox 
from PIL import Image, ImageTk

from json import load, dump

import base64
import subprocess
import sys
import requests
from signal import signal, SIGINT
from colorama import init
from requests import get,post
init()
import os
from os import execl, name, system
from sys import executable, argv
from time import sleep, strftime, localtime, time
#from solvecaptchalink import solvecaptchalink
import atexit
import random
from re import findall, sub
from base64 import b64encode
import json

from information import information
import threading
from api import CAPI
try:
    from playsound import playsound
    from twocaptcha import TwoCaptcha
    from inputimeout import inputimeout, TimeoutOccurred
    from discum import *
    from discum.utils.slash import SlashCommander
    from discord_webhook import DiscordWebhook
except:
	from setup import install
	install()
	from discum import *
	from discum.utils.slash import SlashCommander
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import pyglet, os

pyglet.font.add_file('Lobster.ttf')
pyglet.font.add_file('Prototype.ttf')
pyglet.font.add_file('Frozito.ttf')

client=information()



def create_form(Form):       

    varprayother = tk.BooleanVar(value=False)
    varexp = tk.BooleanVar(value=False)
    varsleep = tk.BooleanVar(value=True)
    varhunt = tk.BooleanVar(value=True)
    varbattle = tk.BooleanVar(value=True)
    vardaily = tk.BooleanVar(value=True)
    varprefix = tk.BooleanVar(value=False)
    varowo = tk.BooleanVar(value=True)
    varpray = tk.BooleanVar(value=True)
    varbuyring = tk.BooleanVar(value=True)
    varapi = tk.BooleanVar(value=False)
    varwcrate = tk.BooleanVar(value=False)
    varlbox = tk.BooleanVar(value=False)
    varwebhook=tk.BooleanVar(value=False)
    vargem = StringVar()
    varsell=tk.BooleanVar(value=False)
    
    vsell=tk.StringVar(Form)     
    vapi=tk.StringVar(Form)    
    vwebhookping=tk.StringVar(Form)
    vwebhook=tk.StringVar(Form)
    vsleeptime = IntVar(Form, value=2700)
    vsleepduration = IntVar(Form, value=300)
    vprefix = StringVar(Form, value="el!")
    vtoken=StringVar(Form)
    vchannelid=StringVar(Form)
    vprayuserid=StringVar(Form)
    vchannelspamid=StringVar(Form)
    vcfbet=IntVar(Form)
    vcfrate=IntVar(Form)
    vosbet=IntVar(Form)
    vosrate=IntVar(Form)
    vchannelcasinoid=StringVar(Form)
    vtime = StringVar(Form, value="00:00:00")
    vDMS=StringVar(Form)
    style = ttk.Style(Form)
    style.configure('My.TEntry', padding=(5,0, 0,0))

    def only_numbers(char):
        return char.isdigit()
    OnlyNumber = Form.register(only_numbers)    
    
    def command(text,color):  
        TextCommand.config(state=NORMAL)
        if color != '': 
            TextCommand.tag_config(color, foreground=color)
            TextCommand.insert(END, text, color ) 
            TextCommand.see('end')
        else:
            TextCommand.insert(END, text)
            TextCommand.see('end')
        TextCommand.config(state=DISABLED)
    def endcommand():
        TextCommand.config(state=NORMAL)
        TextCommand.insert(END, "\n")    
        TextCommand.see('end')
        TextCommand.config(state=DISABLED)
    
    def dms(text,color):  
        TextDirectOwo.config(state=NORMAL)
        if color != '': 
            TextDirectOwo.tag_config(color, foreground=color)
            TextDirectOwo.insert(END, text, color ) 
            TextDirectOwo.see('end')
        else:
            TextDirectOwo.insert(END, text)
            TextDirectOwo.see('end')
        TextDirectOwo.config(state=DISABLED)
    
    def enddms():
        TextDirectOwo.config(state=NORMAL)
        TextDirectOwo.insert(END, "\n")    
        TextDirectOwo.see('end')
        TextDirectOwo.config(state=DISABLED)
    
    def casino(text,color):  
        TextCasino.config(state=NORMAL)
        if color != '': 
            TextCasino.tag_config(color, foreground=color)
            TextCasino.insert(END, text, color )
            TextCasino.see('end') 
        else:
            TextCasino.insert(END, text)
            TextCasino.see('end')
        TextCasino.config(state=DISABLED)
    
    def endcasino():
        TextCasino.config(state=NORMAL)
        TextCasino.insert(END, "\n")    
        TextCasino.see('end')
        TextCasino.config(state=DISABLED)
 
    
    def clickpray():
        if not varpray.get():
            cbPrayOther.config(state=DISABLED)
            tbPrayUserID.config(state=DISABLED)
            comboPray.config(state=DISABLED)
        else:
            cbPrayOther.config(state=NORMAL)
            tbPrayUserID.config(state=NORMAL)
            comboPray.config(state=NORMAL)

    def clickprefix():
        if not varprefix.get():
            tbPrefix.config(state=DISABLED)      
        else:
            tbPrefix.config(state=NORMAL)

    def clickprayother():
        if not varprayother.get():
            tbPrayUserID.config(state=DISABLED)      
        else:
            tbPrayUserID.config(state=NORMAL)
            
    def clickexp():
        if not varexp.get():
            tbChannelSpamingID.config(state=DISABLED)      
        else:
            tbChannelSpamingID.config(state=NORMAL)

    def clicksleep():
        if not varsleep.get():
            tbSleepDuration.config(state=DISABLED)      
            tbSleepTime.config(state=DISABLED)   
            labelsleep1.config(state=DISABLED)   
            labelsleep2.config(state=DISABLED)   
        else:
            tbSleepDuration.config(state=NORMAL)      
            tbSleepTime.config(state=NORMAL)   
            labelsleep1.config(state=NORMAL)   
            labelsleep2.config(state=NORMAL) 
    
    def clickAPI():
        if not varapi.get():
            tbAPI.config(state=DISABLED)
        else:
            tbAPI.config(state=NORMAL)
            
    def clicksell():
        if not varsell.get():
            tbsell.config(state=DISABLED)
        else:
            tbsell.config(state=NORMAL)
            
    def clickwebhook():
        if not varwebhook.get():
            tbwebhook.config(state=DISABLED)
            tbwebhookping.config(state=DISABLED)
            lbwebhookping.config(state=DISABLED)
        else:
            tbwebhook.config(state=NORMAL)
            tbwebhookping.config(state=NORMAL)
            lbwebhookping.config(state=NORMAL)
    
    def clicknocasino():
        if varNoCasino.get():
            cbCoinFlip.config(state=DISABLED)
            cbSlot.config(state=DISABLED)
        else:
            cbCoinFlip.config(state=NORMAL)
            cbSlot.config(state=NORMAL)        

    def clickos():
        if not varSlot.get():
            tbOSbet.config(state=DISABLED)
            tbOSrate.config(state=DISABLED)
            lbosbet.config(state=DISABLED)
            lbosrate.config(state=DISABLED)
            if not varCoinFlip.get():
                lbchannelcasino.config(state=DISABLED)
                tbChannelCasinoID.config(state=DISABLED)
                lbmaxbet.config(state=DISABLED)
                comboMaxBet.config(state=DISABLED)
            else:
                lbchannelcasino.config(state=NORMAL)
                tbChannelCasinoID.config(state=NORMAL)
                lbmaxbet.config(state=NORMAL)
                comboMaxBet.config(state='readonly')                       

        else:
            tbOSbet.config(state=NORMAL)
            tbOSrate.config(state=NORMAL)
            lbosbet.config(state=NORMAL)
            lbosrate.config(state=NORMAL)
            lbchannelcasino.config(state=NORMAL)
            tbChannelCasinoID.config(state=NORMAL)
            lbmaxbet.config(state=NORMAL)
            comboMaxBet.config(state='readonly')  

    def clickcf():
        if not varCoinFlip.get():
            tbCFbet.config(state=DISABLED)
            tbCFrate.config(state=DISABLED)
            lbcfbet.config(state=DISABLED)
            lbcfrate.config(state=DISABLED)
            if not varCoinFlip.get():
                lbchannelcasino.config(state=DISABLED)
                tbChannelCasinoID.config(state=DISABLED)
                lbmaxbet.config(state=DISABLED)
                comboMaxBet.config(state=DISABLED)
            else:
                lbchannelcasino.config(state=NORMAL)
                tbChannelCasinoID.config(state=NORMAL)
                lbmaxbet.config(state=NORMAL)
                comboMaxBet.config(state='readonly')    
        else:
            tbCFbet.config(state=NORMAL)
            tbCFrate.config(state=NORMAL)
            lbcfbet.config(state=NORMAL)
            lbcfrate.config(state=NORMAL)
            lbchannelcasino.config(state=NORMAL)
            tbChannelCasinoID.config(state=NORMAL)
            lbmaxbet.config(state=NORMAL)
            comboMaxBet.config(state='readonly')  

    def clickNogem():
        if vargem.get()==3:
            
            rbMaxMin.config(state=DISABLED)
            rbMinMax.config(state=DISABLED) 
            lbMaxGem.config(state=DISABLED) 
            comboGemTiers.config(state=DISABLED)
        else:
            
            rbMaxMin.config(state=NORMAL)
            rbMinMax.config(state=NORMAL)        
            lbMaxGem.config(state=NORMAL)     
            comboGemTiers.config(state="readonly")        

    #Action Sound Button
    def actionSound():
        if btSound['text']=='Stop Sound':
            btSound.config(text='Start Sound')
            client.sound=False
        else:
            btSound.config(text='Stop Sound')
            client.sound=True
    
    def checkclick():
        clickAPI()
        clickcf()
        clickos()
        clickexp()
        clicknocasino()
        clickNogem()
        clickpray()
        clickprayother()
        clickprefix()
        clicksleep()
        clickwebhook()
        clicksell()
     
    def SaveJson():        
        with open("settingsOWO.json", "r") as f:
            data = load(f)
        if tbToken.get()=="":
            vtoken.set("nothing")
        if tbChannelID.get()=="":
            vchannelid.set("nothing")
        data['token']=tbToken.get()
        data['channel']=tbChannelID.get()

        #Sleepmode
        data['sleep']['enable']=varsleep.get()
        if tbSleepTime.get()=="":
            vsleeptime.set(2700)
        if tbSleepDuration.get()=="":
            vsleepduration.set(300)
        data['sleep']['time']=int(tbSleepTime.get())
        data['sleep']['duration']=int(tbSleepDuration.get())
        #Spam exp
        data['exp']['enable']=varexp.get()
        if tbChannelSpamingID.get()=="":
            vchannelspamid.set("nothing")          
        data['exp']['channelspamid']=tbChannelSpamingID.get() 
        #runner
        data['runner']['hunt']=varhunt.get()
        data['runner']['battle']=varbattle.get()
        data['runner']['daily']=vardaily.get()
        data['runner']['sayowo']=varowo.get()
        data['runner']['buyring']=varbuyring.get()
        #Pray
        data['praycurse']['enable']=varpray.get()
        data['praycurse']['mode']=comboPray.get().strip()
        data['praycurse']['prayother']['enable']=varprayother.get()
        if tbPrayUserID.get()=="":
            vprayuserid.set("nothing")      
        data['praycurse']['prayother']['userid']=tbPrayUserID.get()   
        #Sell
        data['sell']['enable']=varsell.get()
        data['sell']['type']=tbsell.get()             
        #prefix
        data['prefix']['enable']=varprefix.get()
        data['prefix']['key']=tbPrefix.get()
        #UseGem
        data['gem']['mode']=vargem.get() # 1:use3gem; 2:useallgem; 3:usenogem        
        data['gem']['maxtier']=comboGemTiers.get().strip()
        data['gem']['minmax']=varminmax.get() #1:min to max; 2:max to min
        data['gem']['lbox']=varlbox.get()
        data['gem']['wcrate']=varwcrate.get()
        #Casino
        if varNoCasino.get():
            data['casino']['enable']=False
        else:
            data['casino']['enable']=True 
        
        data['casino']['maxbet']=comboMaxBet.get().strip()
        if tbChannelSpamingID.get()=="":

            vchannelcasinoid.set("nothing")
        data['casino']['channelcasinoid']=tbChannelCasinoID.get() 
        data['casino']['cf']['enable']=varCoinFlip.get()
        if tbCFbet.get()=="":
            vcfbet.set(1)
        if tbCFrate.get()=="":
            vcfrate.set(4)      
        if tbOSbet.get()=="":
            vosbet.set(1)
        if tbOSrate.get()=="":
            vosrate.set(3)     
        data['casino']['cf']['bet']=int(tbCFbet.get())
        data['casino']['cf']['rate']=int(tbCFrate.get())
        data['casino']['os']['enable']=varSlot.get()
        data['casino']['os']['bet']=int(tbOSbet.get())
        data['casino']['os']['rate']=int(tbOSrate.get())    
        #Sound
        if btSound['text']=='Stop Sound':
            data['sound']=True
        else:
            data['sound']=False
        #Webhook
        data['webhook']['enable']=varwebhook.get()
        if tbwebhook.get()=="":    
            vwebhook.set("none")   
        if tbwebhookping.get()=="":    
            vwebhookping.set("none")    
        data['webhook']['link']=tbwebhook.get()
        data['webhook']['pingid']=tbwebhookping.get()       
        #2Captcha      
        data['twocaptcha']['enable']=varapi.get()
        if tbAPI.get()=="":    
            vapi.set("none")        
        data['twocaptcha']['api']=tbAPI.get()
        file = open("settingsOWO.json", "w")
        dump(data, file, indent = 4)
        file.close()

            
    def LoadJson():
        with open("settingsOWO.json", "r") as f:
            data = load(f)
            vtoken.set(data['token'])
            vchannelid.set(data['channel'])
            #Sleepmode
            varsleep.set(data['sleep']['enable'])  
            vsleeptime.set(data['sleep']['time'])
            vsleepduration.set(data['sleep']['duration'])
            #Spam exp
            varexp.set(data['exp']['enable'])            
            vchannelspamid.set(data['exp']['channelspamid'])
            #runner
            varhunt.set(data['runner']['hunt'])
            varbattle.set(data['runner']['battle'])
            vardaily.set(data['runner']['daily'])
            varowo.set(data['runner']['sayowo'])
            varbuyring.set(data['runner']['buyring'])
            #Pray
            varpray.set(data['praycurse']['enable'])
            if data['praycurse']['mode']=='Pray':
                comboPray.current(0)
            if data['praycurse']['mode']=='Curse':
                comboPray.current(1)   
            varprayother.set(data['praycurse']['prayother']['enable'])       
            vprayuserid.set(data['praycurse']['prayother']['userid'])        
            #Sell
            varsell.set(data['sell']['enable'])
            vsell.set(data['sell']['type'])   
            #prefix
            varprefix.set(data['prefix']['enable'])
            vprefix.set(data['prefix']['key'])
            #UseGem
            vargem.set(data['gem']['mode']) # 1:use3gem; 2:useallgem; 3:usenogem
            if data['gem']['maxtier']=='Common':
                comboGemTiers.current(0)
            if data['gem']['maxtier']=='Uncommon':
                comboGemTiers.current(1)
            if data['gem']['maxtier']=='Rare':
                comboGemTiers.current(2)
            if data['gem']['maxtier']=='Epic':
                comboGemTiers.current(3)
            if data['gem']['maxtier']=='Mythic':
                comboGemTiers.current(4)
            if data['gem']['maxtier']=='Legend':
                comboGemTiers.current(5)
            if data['gem']['maxtier']=='Fabled':
                comboGemTiers.current(6)    
            varminmax.set(data['gem']['minmax']) #1:min to max; 2:max to min
            varlbox.set(data['gem']['lbox'])
            varwcrate.set(data['gem']['wcrate'])
            #Casino
            if data['casino']['enable']:
                varNoCasino.set(False)
            else:
                varNoCasino.set(True)           
            if data['casino']['maxbet']=='All In to Die':
                comboMaxBet.current(0)
            if data['praycurse']['mode']=='Reset to First Bet':
                comboMaxBet.current(1)     
            vchannelcasinoid.set(data['casino']['channelcasinoid'])
            varCoinFlip.set(data['casino']['cf']['enable'])                
            vcfbet.set(data['casino']['cf']['bet'])
            vcfrate.set(data['casino']['cf']['rate'])
            varSlot.set(data['casino']['os']['enable'])
            vosbet.set(data['casino']['os']['bet'])
            vosrate.set(data['casino']['os']['rate']) 
            #Sound
            if data['sound']==True:
                btSound.config(text='Stop Sound')
                
            else:
                btSound.config(text='Start Sound')            
            #Webhook
            varwebhook.set(data['webhook']['enable'])        
            vwebhook.set(data['webhook']['link'])
            vwebhookping.set(data['webhook']['pingid'])     
            #2Captcha      
            varapi.set(data['twocaptcha']['enable'])
            vapi.set(data['twocaptcha']['api'])
        checkclick()            

    def DefaultJson():
        with open("defaultsettting.json", "r") as f:
            data = load(f)
            vtoken.set(data['token'])
            vchannelid.set(data['channel'])
            #Sleepmode
            varsleep.set(data['sleep']['enable'])  
            vsleeptime.set(data['sleep']['time'])
            vsleepduration.set(data['sleep']['duration'])
            #Spam exp
            varexp.set(data['exp']['enable'])            
            vchannelspamid.set(data['exp']['channelspamid'])
            #runner
            varhunt.set(data['runner']['hunt'])
            varbattle.set(data['runner']['battle'])
            vardaily.set(data['runner']['daily'])
            varowo.set(data['runner']['sayowo'])
            varbuyring.set(data['runner']['buyring'])
            #Pray
            varpray.set(data['praycurse']['enable'])
            if data['praycurse']['mode']=='Pray':
                comboPray.current(0)
            if data['praycurse']['mode']=='Curse':
                comboPray.current(1)   
            varprayother.set(data['praycurse']['prayother']['enable'])       
            vprayuserid.set(data['praycurse']['prayother']['userid'])  
            #Sell
            varsell.set(data['sell']['enable'])
            vsell.set(data['sell']['type'])       
            #prefix
            varprefix.set(data['prefix']['enable'])
            vprefix.set(data['prefix']['key'])
            #UseGem
            vargem.set(data['gem']['mode']) # 1:use3gem; 2:useallgem; 3:usenogem
            if data['gem']['maxtier']=='Common':
                comboGemTiers.current(0)
            if data['gem']['maxtier']=='Uncommon':
                comboGemTiers.current(1)
            if data['gem']['maxtier']=='Rare':
                comboGemTiers.current(2)
            if data['gem']['maxtier']=='Epic':
                comboGemTiers.current(3)
            if data['gem']['maxtier']=='Mythic':
                comboGemTiers.current(4)
            if data['gem']['maxtier']=='Legend':
                comboGemTiers.current(5)
            if data['gem']['maxtier']=='Fabled':
                comboGemTiers.current(6)    
            varminmax.set(data['gem']['minmax']) #1:min to max; 2:max to min
            varlbox.set(data['gem']['lbox'])
            varwcrate.set(data['gem']['wcrate'])
            #Casino
            if data['casino']['enable']:
                varNoCasino.set(False)
            else:
                varNoCasino.set(True)     
            if data['casino']['maxbet']=='All In to Die':
                comboMaxBet.current(0)
            if data['praycurse']['mode']=='Reset to First Bet':
                comboMaxBet.current(1)     
            vchannelcasinoid.set(data['casino']['channelcasinoid'])
            varCoinFlip.set(data['casino']['cf']['enable'])                
            vcfbet.set(data['casino']['cf']['bet'])
            vcfrate.set(data['casino']['cf']['rate'])
            varSlot.set(data['casino']['os']['enable'])
            vosbet.set(data['casino']['os']['bet'])
            vosrate.set(data['casino']['os']['rate']) 
            #Sound
            if data['sound']==True:
                btSound.config(text='Stop Sound')
                
            else:
                btSound.config(text='Start Sound')            
            #Webhook
            varwebhook.set(data['webhook']['enable'])        
            vwebhook.set(data['webhook']['link'])
            vwebhookping.set(data['webhook']['pingid'])     
            #2Captcha      
            varapi.set(data['twocaptcha']['enable'])
            vapi.set(data['twocaptcha']['api'])
        checkclick()

    def CheckInput():
            WarningList=[]
            checkwarning=False
            if tbToken.get()== 'nothing' or tbToken.get()=='':
                WarningList.append('Please input your token')
                checkwarning=True
            else:
                response = get('https://discord.com/api/v9/users/@me',headers={"Authorization": tbToken.get()})
                if response.status_code != 200:
                    WarningList.append('Invalid token')
                    checkwarning=True       
            if tbChannelID.get()== 'nothing' or tbChannelID.get()=='':
                WarningList.append("Please input your ChannelID")  
                checkwarning=True        
            if varexp.get():
                if tbChannelSpamingID.get()== 'nothing' or tbChannelSpamingID.get()=='':
                    WarningList.append("Please input your Channel Spaming ID")  
                    checkwarning=True             
            if varprayother.get():
                if tbPrayUserID.get()== 'nothing' or tbPrayUserID.get()=='':
                    WarningList.append("Please input your UserID you want to %s to" %(comboPray.get().strip()))  
                    checkwarning=True
            if varsell.get():
                if tbsell.get()=="":
                    WarningList.append("Please input type pet you want to sell[All,C U R E M L F S P CP ...]")
                    checkwarning=True
            if varprefix.get():
                if tbPrefix.get()=='':
                    WarningList.append("Please input your prefix key")  
                    checkwarning=True        
            if varwebhook.get():
                if tbwebhook.get()=='' or tbwebhook.get()=='none':
                    WarningList.append("Please input your webhook link")  
                    checkwarning=True          
                if tbwebhookping.get()=='' or tbwebhook.get()=='none':
                    WarningList.append("Please input your webhook Ping UserID")  
                    checkwarning=True       
            if varapi.get():
                if tbAPI.get()=='':
                    WarningList.append("Please input your 2catpcha API")  
                    checkwarning=True             
            if varsleep.get():
                if tbSleepTime.get()=="":
                    vsleeptime.set(2700)
                if tbSleepDuration.get()=="":
                    vsleepduration.set(300)              
            if not varNoCasino.get():           
                if varCoinFlip.get() or varSlot.get():
                    if varCoinFlip.get():
                        if tbCFbet.get()=="":
                            vcfbet.set(1)
                        if tbCFrate.get()=="":
                            vcfrate.set(4)   
                    if varSlot.get():
                        if tbOSbet.get()=="":
                            vosbet.set(1)
                        if tbOSrate.get()=="":
                            vosrate.set(3)      
                    if tbChannelCasinoID.get()=="" or tbChannelCasinoID.get()=='nothing':
                        WarningList.append("Please input Channel Casino ID")  
                        checkwarning=True   
            if checkwarning==True:
                meswarning = '\n'.join(WarningList)         
                messagebox.showwarning("Warning Input",meswarning)       
            return checkwarning
    
    def ClickStart():
        checkinput=CheckInput()

        if not checkinput:
            print('Start')
            client.CheckRunningAuto=True
            Information()
            client.FlagRunAuto=True
            client.stopped=False
            btStart.config(state=DISABLED)
            threading.Thread(target=AutoBot).start()
            
    def ClickStop():
        
        if client.CheckRunningAuto:
            client.FlagRunAuto=False  
            client.CheckRunningAuto=False
            
            print('Stop Auto')
            btStart.config(state=NORMAL)

    def Information():
        client.token=tbToken.get()
        client.channel=tbChannelID.get()
        #Sleepmode
        client.sleep['enable']=varsleep.get()
        client.sleep['time']=int(tbSleepTime.get())
        client.sleep['duration']=int(tbSleepDuration.get())
        #Spam exp
        client.exp['enable']=varexp.get()          
        client.exp['channelspamid']=tbChannelSpamingID.get() 
        #runner
        client.runner['hunt']=varhunt.get()
        client.runner['battle']=varbattle.get()
        client.runner['daily']=vardaily.get()
        client.runner['sayowo']=varowo.get()
        client.runner['buyring']=varbuyring.get()
        #Pray
        client.praycurse['enable']=varpray.get()
        client.praycurse['mode']=comboPray.get().strip()
        client.praycurse['prayother']['enable']=varprayother.get()  
        client.praycurse['prayother']['userid']=tbPrayUserID.get()         
        #Sell
        client.sell['enable']=varsell.get()
        client.sell['type']=tbsell.get()    
        #prefix
        client.prefix['enable']=varprefix.get()
        client.prefix['key']=tbPrefix.get()
        #UseGem
        client.gem['mode']=vargem.get() # 1:use3gem; 2:useallgem; 3:usenogem        
        client.gem['maxtier']=comboGemTiers.get().strip()
        client.gem['minmax']=varminmax.get() #1:min to max; 2:max to min
        client.gem['lbox']=varlbox.get()
        client.gem['wcrate']=varwcrate.get()
        #Casino
        if varNoCasino.get():
            client.casino['enable']=False
        else:
            client.casino['enable']=True       
        client.casino['maxbet']=comboMaxBet.get().strip()
        client.casino['channelcasinoid']=tbChannelCasinoID.get() 
        client.casino['cf']['enable']=varCoinFlip.get()
        client.casino['cf']['bet']=int(tbCFbet.get())
        client.casino['cf']['rate']=int(tbCFrate.get())
        client.casino['os']['enable']=varSlot.get()
        client.casino['os']['bet']=int(tbOSbet.get())
        client.casino['os']['rate']=int(tbOSrate.get())    
        #Sound
        if btSound['text']=='Stop Sound':
            client.sound=True
        else:
            client.sound=False
        #Webhook
        client.webhook['enable']=varwebhook.get()

        client.webhook['link']=tbwebhook.get()
        client.webhook['pingid']=tbwebhookping.get()       
        #2Captcha      
        client.twocaptcha['enable']=varapi.get()     
        client.twocaptcha['api']=tbAPI.get()

        client.tokenbackup=client.token
        client.channelspambackup=client.exp['channelspamid']        

        client.currentcfbet=client.casino['cf']['bet']
        client.currentosbet=client.casino['os']['bet']
        
    def ImgCaptcha():
        imagecaptcha = Image.open("captcha.png")
        zoom = 302/196
        pixels_x, pixels_y = tuple([int(zoom * x)  for x in imagecaptcha.size])
        captcha = ImageTk.PhotoImage(imagecaptcha.resize((pixels_x, pixels_y)))
        lbCaptcha.config(image=captcha)
        lbCaptcha.image = captcha       
    
    def ImgElsa() :   
        imgelsa = Image.open("Elsadefaultpicture.png")
        elsadefault = ImageTk.PhotoImage(imagedefault)    
        lbCaptcha.config(image=elsadefault)
        lbCaptcha.image = elsadefault
      
    def Test():
        ImgCaptcha()
         
    def VoteOwo():
        driver = uc.Chrome()
        driver.set_window_size(1920, 1080)
        token = vtoken.get()
        driver.get('https://discord.com/login?redirect_to=%2Foauth2%2Fauthorize%3Fscope%3Didentify%2520guilds%2520email%26redirect_uri%3Dhttps%253A%252F%252Ftop.gg%252Flogin%252Fcallback%26response_type%3Dcode%26client_id%3D422087909634736160%26state%3DL2JvdC80MDg3ODUxMDY5NDIxNjQ5OTIvdm90ZQ%3D%3D')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'

        driver.execute_script(js + f'login("{token}")')

        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]'))
            )

        driver.find_element(By.CSS_SELECTOR, value='button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]').click()

        if WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#__next > div > div > div.page__PageContentWrapper-sc-iv577v-0.bKsFTH > div.chakra-container.css-15i7o5c > div > div.css-d171a1 > div > div > div > div.css-axnous > main > div.css-4illix > div > div.css-j4hctk > p"), "You can vote now")):
        
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="chakra-button css-ed599q"]')))     
            driver.find_element(By.CSS_SELECTOR, value='button[class="chakra-button css-ed599q"]').click()
            print('VOTED')
            sleep(3)
            driver.quit()
        if WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#__next > div > div > div.page__PageContentWrapper-sc-iv577v-0.bKsFTH > div.chakra-container.css-15i7o5c > div > div.css-d171a1 > div > div > div > div.css-axnous > main > div.css-4illix > div > div.css-j4hctk > p"), "You have already voted for OwO in the past 12 hours")):
            sleep(3)
            driver.quit()
         
    def ClickVote():
        WarningList=[]
        checkwarning=False
        if tbToken.get()== 'nothing' or tbToken.get()=='':
            WarningList.append('Please input your token')
            checkwarning=True
        else:
            response = get('https://discord.com/api/v9/users/@me',headers={"Authorization": tbToken.get()})
            if response.status_code != 200:
                WarningList.append('Invalid token')
                checkwarning=True       
        if checkwarning==True:
                meswarning = '\n'.join(WarningList)         
                messagebox.showwarning("Warning Input",meswarning)   
        threadvote = threading.Thread(name="VoteOwo", target=VoteOwo)  
        threadvote.start() 

    #Groupbox Information
    GroupboxInformation=LabelFrame(Form,bg='#beedff',foreground='#8b0a50',text='  Information  ',height=362,width=822,font="Lobster 12 ")
    GroupboxInformation.place(x=12,y=12)

    cbPrayOther=Checkbutton(GroupboxInformation,text='UserID receive Pray/Curse',variable=varprayother,onvalue=True, offvalue=False,command=clickprayother)
    cbPrayOther.config(bg='#beedff')
    cbPrayOther.place(x=11,y=93)
    cbExp=Checkbutton(GroupboxInformation,text='Spam Exp at ChannelSpamingID',variable=varexp,onvalue=True, offvalue=False,command=clickexp)
    cbExp.config(bg='#beedff')
    cbExp.place(x=11,y=133)
    cbSleep=Checkbutton(GroupboxInformation,text='After Every',variable=varsleep,onvalue=True, offvalue=False,command=clicksleep)
    cbSleep.config(bg='#beedff')
    cbSleep.place(x=11,y=172)
    cbRhunt=Checkbutton(GroupboxInformation,text='owohunt',variable=varhunt,onvalue=True, offvalue=False)
    cbRhunt.config(bg='#beedff')
    cbRhunt.place(x=11,y=209)
    cbRbattle=Checkbutton(GroupboxInformation,text='owobattle',variable=varbattle,onvalue=True, offvalue=False)
    cbRbattle.config(bg='#beedff')
    cbRbattle.place(x=140,y=209)
    cbRdaily=Checkbutton(GroupboxInformation,text='owodaily',variable=vardaily,onvalue=True, offvalue=False)
    cbRdaily.config(bg='#beedff')
    cbRdaily.place(x=225,y=209)
    cbPrefix=Checkbutton(GroupboxInformation,text='Prefix:',variable=varprefix,onvalue=True, offvalue=False,command=clickprefix,state=DISABLED)
    cbPrefix.config(bg='#beedff')
    cbPrefix.place(x=11,y=243)
    cbRowo=Checkbutton(GroupboxInformation,text='owo',variable=varowo,onvalue=True, offvalue=False)
    cbRowo.config(bg='#beedff')
    cbRowo.place(x=141,y=243)
    cbRpray=Checkbutton(GroupboxInformation,text='owo',variable=varpray,onvalue=True, offvalue=False,command=clickpray)
    cbRpray.config(bg='#beedff')
    cbRpray.place(x=11,y=277)
    cbRbuyring=Checkbutton(GroupboxInformation,text='owobuy 1',variable=varbuyring,onvalue=True, offvalue=False)
    cbRbuyring.config(bg='#beedff')
    cbRbuyring.place(x=141,y=277)
    cbwcrate=Checkbutton(GroupboxInformation,text='owc',variable=varwcrate,onvalue=True, offvalue=False,command=clickpray)
    cbwcrate.config(bg='#beedff')
    cbwcrate.place(x=225,y=243)

    cblbox=Checkbutton(GroupboxInformation,text='olb',variable=varlbox,onvalue=True, offvalue=False)
    cblbox.config(bg='#beedff')
    cblbox.place(x=225,y=277)


    cbAPI=Checkbutton(GroupboxInformation,text='API 2captcha',variable=varapi,onvalue=True, offvalue=False,command=clickAPI)
    cbAPI.config(bg='#beedff')
    cbAPI.place(x=420,y=307)
    tbAPI=ttk.Entry(GroupboxInformation,style='My.TEntry',state=DISABLED,show='*',textvariable=vapi)
    tbAPI.config(width=45)
    tbAPI.place(x=530,y=307)

    cbsell=Checkbutton(GroupboxInformation,text='osell',variable=varsell,onvalue=True, offvalue=False,command=clicksell,state=DISABLED)
    cbsell.config(bg='#beedff')
    cbsell.place(x=290,y=243)
    tbsell=ttk.Entry(GroupboxInformation,style='My.TEntry',state=DISABLED,show='*',textvariable=vsell)
    tbsell.config(width=7)
    tbsell.place(x=340,y=245)    

    cbwebhook=Checkbutton(GroupboxInformation,text='Webhook link:',variable=varwebhook,onvalue=True, offvalue=False,command=clickwebhook)
    cbwebhook.config(bg='#beedff')
    cbwebhook.place(x=11,y=305)
    tbwebhook=ttk.Entry(GroupboxInformation,style='My.TEntry',state=DISABLED,textvariable=vwebhook)
    tbwebhook.config(width=17)
    tbwebhook.place(x=112,y=307)
    lbwebhookping=Label(GroupboxInformation,text='Ping UserId:')
    lbwebhookping.config(bg='#beedff')
    lbwebhookping.place(x=220,y=305)
    tbwebhookping=ttk.Entry(GroupboxInformation,style='My.TEntry',state=DISABLED,textvariable=vwebhookping)
    tbwebhookping.config(width=15)
    tbwebhookping.place(x=290,y=307)

    PrayAction=[
        "  Pray",
        "  Curse"
    ]
    comboPray=ttk.Combobox(GroupboxInformation,value=PrayAction,width=7,state="readonly")
    comboPray.current(0)
    comboPray.place(x=67,y=278)


    lbToken=Label(GroupboxInformation,text='Token')
    lbToken.config(bg='#beedff')
    lbToken.place(x=31,y=31)
    lbChannelID=Label(GroupboxInformation,text='Channel ID')
    lbChannelID.config(bg='#beedff')
    lbChannelID.place(x=31,y=64)


    labelsleep1=Label(GroupboxInformation,text='(seconds) Auto will sleep in ')
    labelsleep1.config(bg='#beedff')
    labelsleep1.place(x=131,y=172)
    labelsleep2=Label(GroupboxInformation,text='(seconds)')
    labelsleep2.config(bg='#beedff')
    labelsleep2.place(x=333,y=172)




    tbToken=ttk.Entry(GroupboxInformation,style='My.TEntry',textvariable =vtoken)
    tbToken.config(width=46, show="*")
    tbToken.place(x=105,y=25)
    tbChannelID=ttk.Entry(GroupboxInformation,style='My.TEntry',textvariable =vchannelid)
    tbChannelID.config(width=46)
    tbChannelID.place(x=105,y=60)
    tbPrayUserID=ttk.Entry(GroupboxInformation,style='My.TEntry',state=DISABLED,textvariable =vprayuserid)
    tbPrayUserID.config(width=34)
    tbPrayUserID.place(x=178,y=93)
    tbChannelSpamingID=ttk.Entry(GroupboxInformation,style='My.TEntry',state=DISABLED,textvariable =vchannelspamid)
    tbChannelSpamingID.config(width=29)
    tbChannelSpamingID.place(x=209,y=131)
    tbSleepTime=ttk.Entry(GroupboxInformation,textvariable =vsleeptime,style='My.TEntry')
    tbSleepTime.config(width=5)
    tbSleepTime.place(x=93,y=173)
    tbSleepDuration=ttk.Entry(GroupboxInformation,textvariable =vsleepduration,style='My.TEntry')
    tbSleepDuration.config(width=7)
    tbSleepDuration.place(x=285,y=173)
    tbPrefix=ttk.Entry(GroupboxInformation,textvariable =vprefix,style='My.TEntry',state=DISABLED)
    tbPrefix.config(width=9)
    tbPrefix.place(x=72,y=243)

    #Groupbox Autohunt
    GroupboxAutohunt=LabelFrame(GroupboxInformation,foreground='#8b0a50',bg='#c7fbf7',text='  Auto hunt option  ',height=138,width=403,font="Lobster 12")
    GroupboxAutohunt.place(x=410,y=2)
    GroupUseGem=LabelFrame(GroupboxAutohunt,height=98,width=163,bg='#c7fbf7')
    GroupUseGem.place(x=6,y=8)
    PanelUseGem=PanedWindow(GroupUseGem,height=91,width=157,bg='#c7fbf7')
    PanelUseGem.place(x=1,y=1)


        


    rbUse3Gems=Radiobutton(PanelUseGem, text = "Use 3 Gems Same Tiers",bg='#c7fbf7',value=1,variable=vargem,command=clickNogem)
    rbUse3Gems.place(x=6,y=2)
    rbUseAllGems=Radiobutton(PanelUseGem, text = "Use All Gems",bg='#c7fbf7',value=2,variable=vargem,command=clickNogem)
    rbUseAllGems.place(x=6,y=32)
    rbUseNoGem=Radiobutton(PanelUseGem, text = "Use No Gem",bg='#c7fbf7',value=3,variable=vargem,command=clickNogem)
    rbUseNoGem.place(x=6,y=62)
    vargem.set(1)

    lbMaxGem=Label(GroupboxAutohunt,text='Max Gem Tier:')
    lbMaxGem.config(bg='#c7fbf7')
    lbMaxGem.place(x=190,y=7)

    GemList=[
        " Common",
        " Uncommon",
        " Rare",
        " Epic",
        " Mythic",
        " Legend",
        " Fabled"
    ]
    comboGemTiers=ttk.Combobox(GroupboxAutohunt,value=GemList,width=12,state="readonly")
    comboGemTiers.current(4)
    comboGemTiers.place(x=275,y=6)
    


    

    GroupMinMax=LabelFrame(GroupboxAutohunt,height=72,width=180,bg='#c7fbf7')
    GroupMinMax.place(x=190,y=34)
    PanelMinMax=PanedWindow(GroupMinMax,height=65,width=157,bg='#c7fbf7')
    PanelMinMax.place(x=4,y=2)


    varminmax = StringVar()
    rbMinMax=Radiobutton(PanelMinMax, text = "Use Gem Min to Max",bg='#c7fbf7',value=1,variable=varminmax)
    rbMinMax.place(x=6,y=2)
    rbMaxMin=Radiobutton(PanelMinMax, text = "Use Gem Max to Min",bg='#c7fbf7',value=2,variable=varminmax)
    rbMaxMin.place(x=6,y=32)
    varminmax.set(1)



    #Groupbox Auto Casino
    GroupboxCasino=LabelFrame(GroupboxInformation,bg='#c7fbf7',foreground='#8b0a50',text='  Auto Casino option  ',height=153,width=403,font="Lobster 12")
    GroupboxCasino.place(x=410,y=148)

    varCoinFlip = tk.BooleanVar(value=False)
    varSlot = tk.BooleanVar(value=False)
    varNoCasino = tk.BooleanVar(value=True)




    cbCoinFlip=Checkbutton(GroupboxCasino,text='Auto CoinFlip',variable=varCoinFlip,onvalue=True, offvalue=False,state=DISABLED,command=clickcf)
    cbCoinFlip.config(bg='#c7fbf7',activebackground='#c7fbf7')
    cbCoinFlip.place(x=14,y=7)
    cbSlot=Checkbutton(GroupboxCasino,text='Auto Slots',variable=varSlot,onvalue=True, offvalue=False,state=DISABLED,command=clickos)
    cbSlot.config(bg='#c7fbf7',activebackground='#c7fbf7')
    cbSlot.place(x=14,y=30)
    cbNoCasino=Checkbutton(GroupboxCasino,text='Casino is not good',variable=varNoCasino,onvalue=True, offvalue=False,state=NORMAL,command=clicknocasino)
    cbNoCasino.config(bg='#c7fbf7',activebackground='#c7fbf7')
    cbNoCasino.place(x=14,y=58)

    lbcfbet=Label(GroupboxCasino,text='[OCF] First Bet:',state=DISABLED)
    lbcfbet.config(bg='#c7fbf7')
    lbcfbet.place(x=156,y=7)
    lbcfrate=Label(GroupboxCasino,text='Rate x',state=DISABLED)
    lbcfrate.config(bg='#c7fbf7')
    lbcfrate.place(x=302,y=7)
    lbosbet=Label(GroupboxCasino,text='[O S] First Bet:',state=DISABLED)
    lbosbet.config(bg='#c7fbf7')
    lbosbet.place(x=156,y=38)
    lbosrate=Label(GroupboxCasino,text='Rate x',state=DISABLED)
    lbosrate.config(bg='#c7fbf7')
    lbosrate.place(x=302,y=38)
    lbmaxbet=Label(GroupboxCasino,text='Max Bet Method',state=DISABLED)
    lbmaxbet.config(bg='#c7fbf7')
    lbmaxbet.place(x=156,y=67)
    lbchannelcasino=Label(GroupboxCasino,text='Channel Casino ID',state=DISABLED)
    lbchannelcasino.config(bg='#c7fbf7')
    lbchannelcasino.place(x=49,y=98)


    tbCFbet=ttk.Entry(GroupboxCasino)
    tbCFbet.config(width=6,validate="key",validatecommand=(OnlyNumber,"%P"),style='My.TEntry',state=DISABLED,textvariable=vcfbet)
    tbCFbet.place(x=248,y=6)
    tbCFrate=ttk.Entry(GroupboxCasino)
    tbCFrate.config(width=6,validate="key",validatecommand=(OnlyNumber,"%P"),style='My.TEntry',state=DISABLED,textvariable=vcfrate)
    tbCFrate.place(x=347,y=6)
    tbOSbet=ttk.Entry(GroupboxCasino)
    tbOSbet.config(width=6,validate="key",validatecommand=(OnlyNumber,"%P"),style='My.TEntry',state=DISABLED,textvariable=vosbet)
    tbOSbet.place(x=248,y=38)
    tbOSrate=ttk.Entry(GroupboxCasino)
    tbOSrate.config(width=6,validate="key",validatecommand=(OnlyNumber,"%P"),style='My.TEntry',state=DISABLED,textvariable=vosrate)
    tbOSrate.place(x=347,y=38)
    tbChannelCasinoID=ttk.Entry(GroupboxCasino)
    tbChannelCasinoID.config(width=37,style='My.TEntry',state=DISABLED,textvariable=vchannelcasinoid)
    tbChannelCasinoID.place(x=161,y=97)

    MaxBet=[
        "  All In to Die",
        "  Reset to First Bet"

    ]
    comboMaxBet=ttk.Combobox(GroupboxCasino,value=MaxBet,width=18,state=DISABLED)
    comboMaxBet.current(1)
    comboMaxBet.place(x=258,y=67)





    tbTimeBot=Entry(Form,font=('Miryad 20'), justify=CENTER,state=tk.DISABLED,textvariable =vtime)
    tbTimeBot.config(disabledforeground='#8b0a50',disabledbackground="#daf3ff")
    tbTimeBot.place(x=947,y=12,width=204,height=114)







    lbDirect=Label(Form,text='Direct OWO Area')
    lbDirect.config(bg='#aad6ff',foreground='#447c92',font='Prototype 11')
    lbDirect.place(x=850,y=241)
    TextDirectOwo=Text(Form,state=DISABLED)
    TextDirectOwo.config(background='#fffafa',foreground='#035e83',padx=10,pady=10,font="Miryad 10")
    TextDirectOwo.place(x=849,y=264,width=302,height=237+25)

    lbCommand=Label(Form,text='Command Area')
    lbCommand.config(bg='#aad6ff',foreground='#447c92',font='Prototype 11')
    lbCommand.place(x=12,y=354+25)
    
 
    TextCommand=Text(Form,state=DISABLED)
    TextCommand.config(background='#fffafa',foreground='#035e83',padx=10,pady=10,font="Miryad 10")
    TextCommand.place(x=12,y=375+25,width=388,height=288)

    lbCasino=Label(Form,text='Casino Area')
    lbCasino.config(bg='#aad6ff',foreground='#447c92',font='Prototype 11')
    lbCasino.place(x=440,y=354+25)
    TextCasino=Text(Form,state=DISABLED)
    TextCasino.config(background='#fffafa',foreground='#035e83',padx=10,pady=10,font="Miryad 10")
    TextCasino.place(x=437,y=375+25,width=388,height=288)

    imagecaptcha = Image.open("captcha.png")
    zoom = 302/196
    pixels_x, pixels_y = tuple([int(zoom * x)  for x in imagecaptcha.size])
    captcha = ImageTk.PhotoImage(imagecaptcha.resize((pixels_x, pixels_y)))

    imagedefault=Image.open("Elsadefaultpicture.png") 
    elsadefault = ImageTk.PhotoImage(imagedefault)

    lbCaptcha = Label()
    lbCaptcha.config(image=elsadefault)
    lbCaptcha.image = elsadefault
    lbCaptcha.place(x=850,y=510+25,width=302,height=92)

    lbMes=Label(Form,text='Type message here')
    lbMes.config(bg='#aad6ff',foreground='#447c92',font='Prototype 11 italic')
    lbMes.place(x=850,y=610+25)

    tbMes=ttk.Entry(Form,state=DISABLED,textvariable =vDMS)
    tbMes.config(style='My.TEntry')
    tbMes.place(x=850,y=635+25,width=302,height=30)

        
    btSave=Button(Form,text='Save Json')
    btSave.config(font='("MyriadPro-Cond") 9 bold',background='#d3f8ff',foreground='#b452cd',command=SaveJson)
    btSave.place(x=849,y=12,width=89,height=33)

    btLoad=Button(Form,text='Load Json')
    btLoad.config(font='("MyriadPro-Cond") 9 bold',background='#b0abff',foreground='#8b0a50',command=LoadJson)
    btLoad.place(x=849,y=61,width=89,height=33)

    btDefault=Button(Form,text='Default')
    btDefault.config(font='("MyriadPro-Cond") 9 bold',background='#ffffe8',foreground='#447c92',command=DefaultJson)
    btDefault.place(x=849,y=111,width=89,height=33)

    # btTest=Button(Form,text='Test')
    # btTest.config(font='("MyriadPro-Cond") 9 bold',background='#ffffe8',foreground='#447c92',command=Test)
    # btTest.place(x=849,y=154,width=89,height=33)
    
    
    
    btVote=Button(Form,text='Vote Owo')
    btVote.config(font='("MyriadPro-Cond") 9 bold',background='#d3f8ff',foreground='#b452cd',command=ClickVote)
    btVote.place(x=849,y=198,width=89,height=33)


    btStart=Button(Form,text='Start',command=ClickStart)
    btStart.config(font='("MyriadPro-Cond") 9 bold',background='#d3f8ff',foreground='#b452cd')
    btStart.place(x=947,y=154,width=89,height=33)

    btStop=Button(Form,text='Stop',command=ClickStop)
    btStop.config(font='("MyriadPro-Cond") 9 bold',background='#b0abff',foreground='#8b0a50')
    btStop.place(x=1060,y=154,width=89,height=33)

    btSound=Button(Form,text='Stop Sound')
    btSound.config(font='("MyriadPro-Cond") 9 bold',background='#c7fbf7',foreground='#035e83',command=actionSound)
    btSound.place(x=947,y=198,width=204,height=33)

    
    def AutoBot():
        
        bot = discum.Client(token=client.token, log=False, build_num=0, x_fingerprint="None", user_agent=[
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36/PAsMWa7l-11',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.7.2) Gecko/20100101 / Firefox/60.7.2'])       
        checkvip=client.twocaptcha['enable']
        if client.twocaptcha['enable']:
            api_key = os.getenv('APIKEY_2CAPTCHA', client.twocaptcha['api'])
            solver = TwoCaptcha(api_key, defaultTimeout=100, pollingInterval=5)
            
        @bot.gateway.command
        def on_ready(resp):
            if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
                client.guildID = bot.getChannel(client.channel).json()['guild_id']
                if client.exp['enable']:      
                    client.guildspamID=bot.getChannel(client.exp['channelspamid']).json()['guild_id']
                for i in range(len(bot.gateway.session.DMIDs)):
                    if client.OwOID in bot.gateway.session.DMs[bot.gateway.session.DMIDs[i]]['recipients']:
                        client.dmsID = bot.gateway.session.DMIDs[i]
                    
                user = bot.gateway.session.user
                client.username = user['username']
                client.userid = user['id']  
                command(f'{at()} ','#b452cd')
                command('Logged in as ','')
                command(f"{user['username']}#{user['discriminator']}",'#8b0a50')
                endcommand()
                #print(f"Logged in as {color.yellow}{user['username']}#{user['discriminator']}{color.reset}")
                sleep(1)    
        
                client.starttime=time()
                loopie()


        def PmtoOwo(text):
            text=vDMS.get()
            print(f'{text}')
            bot.sendMessage(client.dmsID, text)
            tbMes.delete(0,'end')
        tbMes.config(state=NORMAL)
        tbMes.bind('<Return>',PmtoOwo)
        
        
  

            

        
        def getMessages(num: int=1, channel: str=client.channel) -> object:
            messageObject = None
            retries = 0
            while not messageObject:
                if not retries > 10:
                    messageObject = bot.getMessages(channel, num=num)
                    messageObject = messageObject.json()
                    if not type(messageObject) is list:
                        messageObject = None
                    else:
                        break
                    retries += 1
                    continue
                if type(messageObject) is list:
                    break
                else:
                    retries = 0
            return messageObject

        def issuechecker(resp: object) -> str:
            
            #user = bot.gateway.session.user
            def solve(image_url: str, msgs: str) -> str:
                img_data = requests.get(image_url).content                
                with open('captcha.png', 'wb') as handler:
                    handler.write(img_data)
                ImgCaptcha()
                client.stopped = True
                encoded_string = b64encode(get(image_url).content).decode('utf-8')
          
                client.stopped = True
                api = CAPI(client.userid)
                r = api.solve(Json={'data': encoded_string, 'len': msgs[msgs.find("letter word") - 2]})
                if r:
                    command(f' !! [INFO] Solved Captcha [Code: {r["code"]}]','red')
                    endcommand()  
                  
                    bot.sendMessage(client.dmsID, r['code'])
                    sleep(10)
                    msgs = getMessages(channel=client.dmsID)
                    try:
                        msgs = msgs[0]
                    except Exception as e:
                        command(str(e),"red")
                        endcommand()
                        command(f"[INFO] There's An Issue With Rerunner","")
                        endcommand            
                        sleep(2)
                        return "captcha"
                    if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:
                        api.report(Json={'captchaId': r['captchaId'], 'correct': 'True'})
                        return "solved"
                    else:
                        command(f"[INFO] Selfbot Stopped As The Captcha Code Is Wrong!","")
                        endcommand()
                        api.report(Json={'captchaId': r['captchaId'], 'correct': 'False'})
                        return "captcha"
                elif r == False:
                    command(f"[INFO] You Haven't Registered To Our Captcha Solving API!\n","")
                    command('To Register Join Our Discord Server: https://discord.gg/9uZ6eXFPHD And Send \"bot register\" in bot command channel','')
                    endcommand()
                    return "captcha"
                else:
                    command(f"[INFO] Captcha Solver API Is Having An Issue...","")
                    endcommand()       
                    return "captcha"

            def getAnswer(img,lenghth,code):
                count=0
                timeanswer=time()
                while True:
                    if time() - timeanswer < 300 :
                        count+=1
                        r = solver.normal(img,numeric=2,minLen=lenghth,maxLen=lenghth,phrase=0,caseSensitive=0,calc=0,lang='en',textinstructions=code,)
                
                        if r['code'].isalpha():
                            if len(r['code'])==lenghth:
                                command(f"Check result 2captcha","")
                                endcommand()                                              
                                return r
                            else:
                                solver.report(r['captchaId'], False) 
                                command(f"Time: {count}. The length of result {r['code']} is not right.Try again","")
                                endcommand()     
                                
                        else:
                            solver.report(r['captchaId'], False) 
                            command(f'Time: {count}. The result {r["code"]} contants number.Try again',"")
                            endcommand()    
            
                    else:
                        print(f'TIME OUT 5 MINUTES for SOLVE')
                        return 'captcha'
            
            def solvevip(image_url: str, msgs: str) -> str:
                img_data = requests.get(image_url).content                
                with open('captcha.png', 'wb') as handler:
                    handler.write(img_data)                    
                ImgCaptcha()
                client.stopped = True	
                encoded_string = b64encode(get(image_url).content).decode('utf-8')		
                countlen=int(msgs[msgs.find("letter word") - 2])

                #Check balance of 2Captcha
                captchabalance = solver.balance()    
                if captchabalance==0:
                    command(f"Balance 2CAPCHA : {captchabalance} $ Out of money","")
                    endcommand()      
                    if client.webhook['enable']:
                        webhookPing(f"<@{client.webhook['pingid']}> [FAIL]Out of money . User: {client.username} <@{client.userid}>")
                        webhookPing(f"=========================================================================================")
                    return "captcha"

                #Solve by 2Captcha
                code=""
                r = getAnswer(encoded_string,countlen,code)
                try:
                    if r=='captcha':
                        return 'captcha'
                except:
                    pass
                captchabalance = solver.balance()
                command(f'Balance 2CAPCHA : {captchabalance} $','')
                endcommand()
                command(f"[INFO] Solving Captcha at 1st chance: [Code: {r['code']}]",'')
                endcommand()     
                

                bot.sendMessage(client.dmsID, r['code'])
                sleep(5)
            
                msgs = bot.getMessages(client.dmsID)
                try:
                    msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
                except:
                    command(f"[INFO] There's An Issue With Rerunner",'')
                    endcommand()
                    if client.webhook['enable']:                    
                        webhookPing(f"=========================================================================================")
                    sleep(2)
                    return "captcha"					
                if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:	
                    solver.report(r['captchaId'], True)
                    return "solved"
                if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:
                    if client.webhook['enable']:     
                        webhookping()
                        webhookPing(f"<@{client.webhook['pingid']}> [FAIL]I have solved the captcha fail in the 1st chance. Wait me at the 2nd chance. Sorry . User: {client.username} <@{client.userid}>")
                        solver.report(r['captchaId'], False)  #Báo kết quả sai 
                    textand='and'
                    textwrong='IS WRONG'
                    textjoin=[r['code'],textwrong]
                    texthint=' '.join(textjoin)
                    code=texthint
                    r2 = getAnswer(encoded_string,countlen,code)
                    try:
                        if r=='captcha':
                            return 'captcha'
                    except:
                        pass
                    command(f"[INFO] Solving Captcha at 2nd chance: [Code: {r2['code']}]",'')
                    endcommand()
    
                    bot.sendMessage(client.dmsID, r2['code'])						
                    captchabalance = solver.balance()
                    command(f"Balance 2CAPCHA : {captchabalance} $",'')
                    endcommand()
                    sleep(3)
                    
                    msgs = bot.getMessages(client.dmsID)      
                    try:
                        msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
                    except:
                        if client.webhook['enable']:
                            webhookping()
                        if client.sound():
                            threadcaptcha = threading.Thread(name="captchamusic", target=captchamusic)
                            threadcaptcha.start()
                        command(f"[INFO] There's An Issue With Rerunner",'')
                        endcommand()                 
                        if client.webhook['enable']:
                            webhookPing(f"=========================================================================================")
                        sleep(2)
                        return "captcha"  
                    print(f'{msgs}')
                    if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:		
                        solver.report(r2['captchaId'], True)
                        return "solved"
                    if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:
                        solver.report(r2['captchaId'], False) 
                        textjoin=[r2["code"],textand,textjoin,"ARE WRONG"]
                        texthint=' '.join(textjoin)
                        if client.webhook['enable']:
                            webhookPing(f"<@{client.webhook['pingid']}> [FAIL]I have solved the captcha fail in the 2nd chance. Wait me at the 3rd chance. Sorry . User: {client.username} <@{client.userid}>")
                            
                        code=texthint
                        r3 = getAnswer(encoded_string,countlen,code)
                        try:
                            if r=='captcha':
                                return 'captcha'
                        except:
                            pass
                        command(f"[INFO] Solving Captcha at 3rd chance: [Code: {r3['code']}]",'')
                        endcommand()  

                        bot.sendMessage(client.dmsID, r3['code'])  
                        captchabalance = solver.balance()
                        command(f"Balance 2CAPCHA : {captchabalance} $",'')
                        endcommand()                     
                        sleep(3)
                        
                        msgs = bot.getMessages(client.dmsID)      
                        try:
                            msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
                        except:
                            if client.webhook['enable']:
                                webhookping()
                            threadcaptcha.start()
                            command(f"[INFO] There's An Issue With Rerunne",'')
                            endcommand() 
                            if client.webhook['enable']:
                                webhookPing(f"=========================================================================================")
                            sleep(2)
                            return "captcha"    
                        print(f'{msgs}')
                        if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:		
                            solver.report(r3['captchaId'], True)
                            return "solved"
                        if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:	       
                            solver.report(r3['captchaId'], False) 
                            threadcaptcha.start()
                            if client.webhook['enable']:
                                webhookPing(f"<@{client.webhook['pingid']}> [FAIL]I have solved the captcha fail in the 3rd chance. Sorry very much. Please solve the captcha by yourself in the last chance. Carefully. Good Luck . User: {client.username} <@{client.userid}>")
                            return 'captcha'	
                        return 'captcha'	
                    return 'captcha'	
                return 'captcha'		
            
            if client.casino['cf']['enable'] or client.casino['cf']['enable']:
                if client.casino['channelcasinoid']=='nothing' or client.casino['channelcasinoid']=='':
                    client.casino['channelcasinoid']=client.channel
                    
                  
            if resp.event.message:		
                threadcaptcha= threading.Thread(name="captchamusic", target=captchamusic)
                m = resp.parsed.auto()     
                
                #if m['channel_id'] == client.channel or m['channel_id'] == client.casino['channelcasinoid'] or m['channel_id'] == client.dmsID and not client.stopped:
                if m['author']['id'] == client.OwOID or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456'  and not client.stopped:
                    
                    if client.username in m['content'] and 'banned' in m['content'].lower() and not client.stopped:
                        command(f'{at()} ','yellow')
                        command(' !! [CAPTCHA] !! ACTION REQUİRED','red')
                        endcommand()
                        client.stopped=True
                        return "captcha"
                    if client.username in m['content'] and  any(captcha in m['content'].lower() for captcha in ['(1/5)', '(2/5)', '(3/5)', '(4/5)', '(5/5)']) and not client.stopped:				
                        msgs=getMessages(channel=client.dmsID)
                        print(msgs)
                        if client.username in m['content'] and msgs[0]['author']['id'] == client.OwOID and '⚠'  in msgs[0]['content'] and msgs[0]['attachments'] and not client.stopped:
                            client.stopped=True
                            threadcaptcha.start()
                            command(f'{at()} ','yellow')
                            command(' !! [CAPTCHA] !! ACTION REQUİRED','red')
                            endcommand()      
                            
                            if checkvip and not client.stopped:
                                if client.webhook['enable']:
                                    webhookping()
                                return solvevip(msgs[0]['attachments'][0]['url'], msgs[0]['content'])
                            else:
                                if client.solve['enable'] and not client.stopped:
                                    return solve(msgs[0]['attachments'][0]['url'], msgs[0]['content'])
                            return "captcha"
                        elif msgs[0]['author']['id'] == client.OwOID and 'link' in msgs[0]['content'].lower() and not client.stopped:		
                            #if client.webhook['enable']:			
                                #webhookPing(f"<@{client.webhook['pingid']}> [WARNING]Captcha Link. Wait me. User: {client.username} <@{client.userid}>")
                            client.stopped=True	                           	
                            return solvelink()				
                    
                        msgs=getMessages(num=10)
                        for i in range(len(msgs)):
                            if client.username in m['content'] and  msgs[i]['author']['id'] == client.OwOID and 'solving the captcha' in msgs[i]['content'].lower() and not client.stopped:
                                threadcaptcha.start()
                                command(f'{at()} ','yellow')
                                command(' !! [CAPTCHA] !! ACTION REQUİRED','red')
                                endcommand()
                                if checkvip and not client.stopped:
                                    client.stopped=True

                                    return solvevip(msgs[0]['attachments'][0]['url'], msgs[0]['content'])
                                else:
                                    if not client.stopped:
                                        client.stopped=True
                                        if client.webhook['enable']:
                                            webhookping()
                                        return solve(msgs[0]['attachments'][0]['url'], msgs[0]['content'])
                                return "captcha"
                            else:
                                if i == len(msgs) - 1:
                                    client.stopped=True
                                    return "captcha"
                    if client.username in m['content'] and  '⚠' in m['content'].lower() and not client.stopped:

                        if  m['attachments'] and not client.stopped:
                            threadcaptcha.start()
                            command(f'{at()} ','yellow')
                            command(' !! [CAPTCHA] !! ACTION REQUİRED','red')
                            endcommand()
                
                            if  not client.stopped:
                                client.stopped=True
                                if client.webhook['enable']:
                                    webhookping()
                                return solvevip(m['attachments'][0]['url'], m['content'])
                            else:
                                if not client.stopped:
                                    client.stopped=True
                                    return solve(m['attachments'][0]['url'], m['content'])
                        threadcaptcha.start()
                        command(f'{at()} ','yellow')
                        command(' !! [CAPTCHA] !! ACTION REQUİRED','red')
                        endcommand()                        
                        return "captcha"                    

        @bot.gateway.command
        def security(resp: object)-> None:
            threadcaptchamusic = threading.Thread(name="captchamusic", target=captchamusic)
            threadsolvedmusic = threading.Thread(name="solvedmusic", target=solvedmusic)
            if issuechecker(resp) == "solved":	
                ImgElsa()
                if client.webhook['enable']:
                    if checkCasino():
                        webhookPing(f"[SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> or <#{client.casino['channelcasinoid']}> . User: {client.username} ")  			
                        #webhookPing(f"<@{client.webhook['pingid']}> [SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> or <#{client.casino['channelcasinoid']}> . User: {client.username} ")  			
                    
                    else:
                        webhookPing(f"[SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> . User: {client.username} ") 
                        #webhookPing(f"<@{client.webhook['pingid']}> [SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> . User: {client.username} ") 
                    if client.twocaptcha['enable']:
                        webhookPing(f'2Captcha Balance: {solver.balance()} $')
                    webhookPing("===========================================================================================")
                #threadsolvedmusic.start()
                sleep(3)
                command(f'[INFO] Captcha Solved. Started To Run Again','')
                endcommand()
                #subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')  
                client.stopped=False
                
                loopie()
                #execl(executable, executable, *argv)
            if issuechecker(resp) == "captcha":
                client.stopped = True
                if client.webhook['enable']:
                    webhookping()
                threadcaptchamusic.start()
                


        #Check balance Casino    
        @bot.gateway.command	
        def checkballance(resp): 
                      
            if checkCasino():
                if client.checknocash == False and client.stopped != True:
                    if resp.event.message:
                        m = resp.parsed.auto()
                        if m['channel_id'] == client.casino['channelcasinoid'] and client.stopped == False:
                            if m['author']['id'] == client.OwOID and client.username in m['content'] and 'you currently have' in m['content']:
                                client.cash = findall('[0-9]+', m['content'])
                                casino(f'{at()} ','#b452cd')
                                casino(f"You currently have {','.join(client.cash[1::])} Cowoncy !","")
                                endcasino()
                        if client.username in m['content'] and 'You don\'t have enough cowoncy!' in m['content']:
                            casino('[ERROR]','red')
                            casino('Not Enough Cowoncy To Continue!','')
                            endcasino()                            
                            client.checknocash = True

    # Gems
        @bot.gateway.command
        def checkgem(resp):
            if client.gem['mode']==1 and client.stopped != True :
                if resp.event.message:
                    m = resp.parsed.auto()
                    if m['channel_id'] == client.channel and client.stopped != True:
                        if m['author']['id'] == client.OwOID:
                            if client.username in m['content'] and "**🌱" in m['content']:
                                command(f'{at()} ','#b452cd')
                                command('!! [CHECK GEM HUNT] !!','')
                                endcommand()
                            
                            if client.username in m['content'] and  "and caught" in m['content'] and client.checknogem == False:
                                command(f'{at()} ','#b452cd')
                                command(f'!! [CHECK GEM] checknogem = {client.checknogem}','')
                                endcommand()                               
                                useGem()

        # Check Hunt
        @bot.gateway.command
        def checkhunt(resp):
            if client.stopped != True and client.webhook['enable'] :
                if resp.event.message:
                    m = resp.parsed.auto()
                    
                    if m['channel_id'] == client.channel and client.stopped != True:
                        if m['author']['id'] == client.OwOID:
                            if client.username in m['content'] and "**🌱" in m['content']:						
                                guildhuntid = bot.getChannel(m['channel_id']).json()['guild_id']
                                channels = bot.gateway.session.guild(guildhuntid).channels
                                guildname=bot.gateway.session.guild(guildhuntid).name
                                for i in channels:
                                    if channels[i]['type'] == "guild_text" and channels[i]['id']==m['channel_id']:
                                        channel4=channels[i]
                                channelname=channel4['name']
                                if "empowered" in m['content']:
                                    pet1=substring_after(m['content'],":blank: |")
                                    pethunt=substring_before(pet1, ':blank: |')
                                if "caught" in m['content']:
                                    pet1=substring_after(m['content'],"caught ")
                                    pethunt=substring_before(pet1, '!')

                                for i in range(len(client.listhidden)):
                                    if client.listhidden[i].lower() in pethunt.lower():   
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")       
                                        webhookPing(f"[INFO] I have found Hidden Pet at {channelname} . User:{client.username} <@{client.userid}> ") 
                                        webhookPing(f"https://discord.com/channels/{guildhuntid}/{m['channel_id']}/{m['id']}")
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        command(f"You found Hidden Pet by hunting at channel {channelname} in server {guildname} with message id is {m['id']}","")
                                        endcommand() 
                                        break
                                for i in range(len(client.listfabled)):
                                    if client.listfabled[i].lower() in pethunt.lower():  
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")     
                                        webhookPing(f"[INFO] I have found Fabled Pet at {channelname} . User:{client.username} <@{client.userid}> ") 
                                        webhookPing(f"https://discord.com/channels/{guildhuntid}/{m['channel_id']}/{m['id']}")	
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    		
                                        command(f"You found Fabled Pet by hunting at channel {channelname} in server {guildname} with message id is {m['id']}","")
                                        endcommand() 
                                        break
                                for i in range(len(client.listbotrank)):
                                    if client.listbotrank[i].lower() in pethunt.lower():  
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        webhookPing(f"[INFO] I have found Botrank Pet at {channelname} . User:{client.username} <@{client.userid}> ") 
                                        webhookPing(f"https://discord.com/channels/{guildhuntid}/{m['channel_id']}/{m['id']}")
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        command(f"You found Botrank Pet by hunting at channel {channelname} in server {guildname} with message id is {m['id']}","")
                                        endcommand()   
                                        break
                           
                                if "cpatreon" in pethunt.lower():
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        webhookPing(f"[INFO] I have found Custom Patreon Pet at {channelname} . User:{client.username} <@{client.userid}> ") 
                                        webhookPing(f"https://discord.com/channels/{guildhuntid}/{m['channel_id']}/{m['id']}")
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        command(f"You found Custom Patreon Pet by hunting at channel {channelname} in server {guildname} with message id is {m['id']}","")      
                                        endcommand()  
                                for i in range(len(client.listdistored)):
                                    if client.listdistored[i].lower() in pethunt.lower(): 
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        webhookPing(f"[INFO] I have found Distorted Pet at {channelname} . User:{client.username} <@{client.userid}> ") 
                                        webhookPing(f"https://discord.com/channels/{guildhuntid}/{m['channel_id']}/{m['id']}")
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        command(f"You found Distorted Pet by hunting at channel {channelname} in server {guildname} with message id is {m['id']}","")      
                                        endcommand()  
                                        break
                       
                                if "special" in pethunt.lower():
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        webhookPing(f"[INFO] I have found Special Pet at {channelname} . User:{client.username} <@{client.userid}> ") 
                                        webhookPing(f"https://discord.com/channels/{guildhuntid}/{m['channel_id']}/{m['id']}")
                                        webhookPing("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
                                        command(f"You found Special Pet by hunting at channel {channelname} in server {guildname} with message id is {m['id']}","")      
                                        endcommand()   
        
        
        
        # Get Direct Owo
        @bot.gateway.command
        def GetDMS(resp):        
                if resp.event.message:
                    m = resp.parsed.auto()
                    
                    if m['channel_id'] == client.dmsID :
                        if m['author']['id'] == client.OwOID:
                            dms(f'{at()} '"#b452cd")
                            dms('OWO [BOT]:\n',"#8b0a50")
                            dms(f'{m["content"]}\n\n',"")
                            if client.checkcaptchafail==True:
                                if ' I have verified' in m['content'] :
                                    client.stopped=True
                                    client.checkcaptchafail=False
                                    loopie()
                        if m['author']['id'] == client.userid:
                            dms(f'{at()} ',"#b452cd")
                            dms(f'{client.username}:\n',"#8b0a50")
                            dms(f'{m["content"]}\n\n',"")
                            
        
        def useGem():
            if client.gem['mode']!=3 and client.stopped != True:
                bot.typingAction(str(client.channel))
                sleep(1.5)
                bot.sendMessage(str(client.channel), "owo inv")
                command(f"{at()} ","#b452cd")
                command("User: ","")
                command(f"{client.username}","#8b0a50")
                command(f" [SENT] owo inv",'')
                endcommand() 
                client.totalcmd += 1
                sleep(4)
                msgs = bot.getMessages(str(client.channel), num=10)
                msgs = msgs.json()
                inv = ""
                for i in range(len(msgs)):
                    if msgs[i]['author']['id'] == client.OwOID and 'Inventory' in msgs[i]['content']:
                        inv = findall(r'`(.*?)`', msgs[i]['content'])
                if not inv:
                    sleep(2)
                    client.totalcmd -= 1
                    useGem()
                else:
                    if '050' in inv:
                        if client.gem['lbox'] and client.stopped != True:
                            bot.sendMessage(str(client.channel), "owo lb all")
                            command(f"{at()} ","#b452cd")
                            command("User:","")
                            command(f"{client.username}",'#8b0a50')
                            command(f" [SENT] owo lb all",'')      
                            endcommand() 
                            sleep(4)

                    if '100' in inv:
                        if client.gem['wcrate'] and client.stopped != True:
                            bot.sendMessage(str(client.channel), "owo crate all")
                            command(f"{at()} ","#b452cd")
                            command("User:","")
                            command(f"{client.username}",'#8b0a50')
                            command(f" [SENT] owo wc all",'')    
                            endcommand()
                            sleep(2)
                    for item in inv:
                        try:
                            if int(item) >= 100 or int(item) <= 50:
                                inv.pop(inv.index(item))  # weapons
                        except:  # backgounds etc
                            inv.pop(inv.index(item))
                    tier = [[], [], []]
                    countGem = [0, 0, 0, 0, 0, 0, 0]
                    command(f"{at()}","#b452cd")   
                    command(f"===============\n","")
                    command(f"{at()} ","#b452cd")                    
                    command(f"[INFO]  Found {len(inv)} Gems Inventory",'')    
                    endcommand()

                    available = []
                    for gem in inv:
                        gem = sub(r"[^a-zA-Z0-9]", "", gem)
                        gem = int(gem)
                        for i in range(0, 7, 1):
                            if gem == 51 + i or gem == 65 + i or gem == 72 + i:
                                countGem[i] += 1

                
                    command(f"{at()} ","#b452cd") 
                    command(f"[INFO] \n","")
                    command(f" 		     Gem C: {countGem[0]} loại\n","")
                    command(f" 		     Gem U: {countGem[1]} loại\n","")
                    command(f" 		     Gem R: {countGem[2]} loại\n","")
                    command(f"		     Gem E: {countGem[3]} loại\n","")
                    command(f" 		     Gem M: {countGem[4]} loại\n","")
                    command(f" 		     Gem L: {countGem[5]} loại\n","")
                    command(f" 		     Gem F: {countGem[6]} loại\n","")
                    command(f"{at()} ","#b452cd")
                    command("===============\n","")
                    sleep(1)
                    nogem = False
                    if client.gem['minmax']== 1:
                        for i in range(0, 5, 1):  # i=4 => Gem Mythic
                            if use3gem(i + 1, countGem[i]):
                                nogem = False
                                break
                            else:
                                nogem = True
                    if client.gem['minmax'] == 2:
                        for i in range(4, -1, -1):  # i=4 => Gem Mythic
                            if use3gem(i + 1, countGem[i]):
                                nogem = False
                                break
                            else:
                                nogem = True
                    if nogem:
                        client.checknogem = True
                        #print(f"{at()}{color.fail} [INFO] {color.reset} {client.checknogem}")
                        command(f"{at()} ","#b452cd")
                        command("[INFO] Ko có bộ 3 GEM giống nhau . Ko sử dụng GEM nhé","")
                        endcommand()

        def use3gem(level, count):
            if client.gem['mode']==1 and client.stopped != True:
                a = 50
                b = 64
                c = 71
                # 1 51 65 72 Common
                # 2 52 66 73 Uncommon
                # 3 53 67 74 Rare
                # 4 54 68 75 Epic
                # 5 55 69 76 Mythic
                # 6 56 70 77 Legend
                # 7 57 71 78 Fabled
                a = a + level
                b = b + level
                c = c + level
                typegem = ""
                turngem = 0
                if level == 1:
                    typegem = 'Common'.upper()
                    turngem = 25
                if level == 2:
                    typegem = 'UnCommon'.upper()
                    turngem = 25
                if level == 3:
                    typegem = 'Rare'.upper()
                    turngem = 50
                if level == 4:
                    typegem = 'Epic'.upper()
                    turngem = 75
                if level == 5:
                    typegem = 'Mythic'.upper()
                    turngem = 75
                if level == 6:
                    typegem = 'Legend'.upper()
                    turngem = 100
                if level == 7:
                    typegem = 'Fabled'.upper()
                    turngem = 100

                if count == 3:
                    sleep(2)
                    bot.sendMessage(str(client.channel), "owo use {} {} {}".format(str(a), str(b), str(c)))
                    command(f"{at()} ","#b452cd")
                    command("User:","")
                    command(f"{client.username}",'#8b0a50')
                    command(f" [SENT] owo use {a} {b} {c} [GEMS {typegem}][{str(turngem)} turn]","")
                    endcommand()
                    client.checkusegem += 1
                    command(f"{at()} ","#b452cd")
                    command(f"[INFO] !! [USE GEM lần {client.checkusegem}] !!","")
                    endcommand()
                    return True
                else:
                    return False

        @bot.gateway.command
        def checkcf(resp):
            if client.casino['enable'] and client.casino['cf']['enable'] and client.checknocash == False and client.stopped != True :
                if resp.event.message_updated:
                    m = resp.parsed.auto()
                    try:
                        if m['channel_id'] == client.casino['channelcasinoid']:
                            if m['author']['id'] == client.OwOID:
                                if client.username in m['content'] and 'and chose' in m['content']:
                                    if 'and you won' in m['content']:
                                        casino(f'[INFO WIN]{client.username} OCF Won: {client.currentcfbet} Cow/ Total Won: {client.totalwon+client.currentcfbet}/ Total Lost: {client.totallost}/ Last Benefit: {client.totalwon-client.totallost+client.currentcfbet}','#ff86e3')
                                        endcasino()
                                        client.countcfmaxlost =0
                                        client.totalwon += client.currentcfbet
                                        if client.currentcfbet == 150000:
                                            bot.typingAction(str(client.casino['channelcasinoid']))
                                            bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                        client.currentcfbet = client.casino['cf']['bet']
                                        sleep(1)
                                    if 'and you lost it all... :c' in m['content']:
                                        casino(f'[INFO LOSE]{client.username} OCF Lost: {client.currentcfbet} Cow/ Total Won: {client.totalwon}/ Total Lost: {client.totallost+client.currentcfbet}/ Last Benefit: {client.totalwon-client.totallost-client.currentcfbet}','#09316e')
                                        endcasino()
                                        client.totallost += client.currentcfbet
                                        if client.currentcfbet == 150000:
                                            client.countcfmaxlost += 1
                                            if client.sound():
                                                if client.countcfmaxlost==1:
                                                    threadkiepdoden = threading.Thread(name="kiepdoden", target=kiepdoden)
                                                    threadkiepdoden.start()									
                                            
                                            bot.sendMessage(str(client.casino['channelcasinoif']), "owo cash")
                                            if client.casino['maxbet'] == "All In to Die":
                                                client.currentcfbet = 150000
                                            if client.casino['maxbet'] == "Reset to First Bet":
                                                client.currentcfbet = client.casino['cf']['bet']
                                        client.currentcfbet *= client.casino['cf']['rate']
                                        if client.currentcfbet >= 150000:
                                            client.currentcfbet = 150000
                                        sleep(1)						
                    except KeyError:
                        pass

        @bot.gateway.command
        def checkos(resp):
        
            if client.casino['enable'] and client.casino['os']['enable'] and client.checknocash == False and client.stopped != True:
                if resp.event.message_updated:
                    m = resp.parsed.auto()
                    try:
                        if m['channel_id'] == client.casino['channelcasinoid']:
                            if m['author']['id'] == client.OwOID:
                                if client.username in m['content'] and 'bet' in m['content'] and '___SLOTS___' in m['content']:
                                    if 'and won <:cowoncy:416043450337853441>' in m['content']:
                                        if '<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' not in m['content'] and '<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>'not in m['content'] and '<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>'not in m['content'] and '<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>'not in m['content']:
                                            casino(f'[INFO WIN]{client.username} OS Won: {client.currentosbet} Cow/ Total Won: {client.totalwon+client.currentosbet}/ Total Lost: {client.totallost}/ Last Benefit: {client.totalwon-client.totallost+client.currentosbet}','#ff86e3')
                                            endcasino
                                            #client.countmaxlost =0
                                            client.totalwon += client.currentosbet
                                            if client.currentosbet == 150000:
                                                bot.typingAction(str(client.casino['channelcasinoid']))
                                                bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                            client.currentosbet = client.casino['os']['bet']
                                            sleep(1)       
                                    if ' and won nothing... :c' in m['content']:
                                        casino(f'[INFO LOSE]{client.username} OS Lost: {client.currentosbet} Cow/ Total Won: {client.totalwon}/ Total Lost: {client.totallost+client.currentosbet}/ Last Benefit: {client.totalwon-client.totallost-client.currentosbet}','#09316e')
                                        endcasino()
                                        client.totallost += client.currentosbet
                                        if client.currentosbet == 150000:
                                            client.countosmaxlost += 1
                                            if client.countosmaxlost==1:
                                                threadkiepdoden = threading.Thread(name="kiepdoden", target=kiepdoden)
                                                threadkiepdoden.start()									
                                            
                                            bot.sendMessage(str(client.channelocf), "owo cash")
                                            if client.casino['maxbet'] == "All In to Die":
                                                client.currentosbet = 150000
                                            if client.casino['maxbet'] == "Reset to First Bet":
                                                client.currentosbet = client.casino['os']['bet']
                                        client.currentosbet *= client.casino['os']['rate']
                                        if client.currentosbet >= 150000:
                                            client.currentosbet = 150000
                                    if'**`___SLOTS___  `**\n<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' in m['content']:
                                        casino(f'[INFO DRAW]{client.username} OS Draw: {client.currentosbet} Cow/ Total Won: {client.totalwon}/ Total Lost: {client.totallost}/ Last Benefit: {client.totalwon-client.totallost}','#b452cd')
                                        endcasino()
                        
                                    if'**`___SLOTS___  `**\n<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>' in m['content']:
                                            casino(f'[INFO WIN X3]{client.username} OS Won X3: {client.currentosbet} Cow/ Total Won: {client.totalwon+client.currentosbet*3}/ Total Lost: {client.totallost}/ Last Benefit: {client.totalwon-client.totallost+client.currentosbet*3}','#ff86e3')
                                            endcasino()
                                            client.countosmaxlost =0
                                            client.totalwon = client.currentosbet*3+client.totalwon
                                            if client.currentosbet >= 30000:
                                                bot.typingAction(str(client.casino['channelcasinoid']))
                                                bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                            client.currentosbet = client.casino['os']['bet']
                                            sleep(1)                  
                                    if'**`___SLOTS___  `**\n<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>' in m['content']:      
                                            casino(f'[INFO WIN X4]{client.username} OS Won X4: {client.currentosbet} Cow/ Total Won: {client.totalwon+client.currentosbet*4}/ Total Lost: {client.totallost}/ Last Benefit: {client.totalwon-client.totallost+client.currentosbet*4}','#ff86e3')
                                            endcasino()
                                            client.countosmaxlost =0
                                            client.totalwon = client.currentosbet*4 + client.totalwon
                                            if client.currentosbet >= 20000:
                                                bot.typingAction(str(client.casino['channelcasinoid']))
                                                bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                                sleep(1) 
                                                bot.typingAction(str(client.casino['channelcasinoid']))
                                                bot.sendMessage(str(client.casino['channelcasinoid']), "owo") 
                                            client.currentosbet = client.casino['os']['bet']
                                            sleep(1)             
                                    if'**`___SLOTS___  `**\n<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>' in m['content']:      
                                            casino(f'[INFO WIN X10]{client.username} OS Won X10: {client.currentosbet} Cow/ Total Won: {client.totalwon+client.currentosbet*10}/ Total Lost: {client.totallost}/ Last Benefit: {client.totalwon-client.totallost+client.currentosbet*10}','#ff86e3')
                                            endcasino()
                                            client.countosmaxlost =0
                                            client.totalwon = client.currentosbet*10 + client.totalwon
                                            if client.currentosbet >= 20000:
                                                bot.typingAction(str(client.casino['channelcasinoid']))
                                                bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                                sleep(1) 
                                                bot.typingAction(str(client.casino['channelcasinoid']))
                                                bot.sendMessage(str(client.casino['channelcasinoid']), "owo") 
                                            client.currentosbet = client.casino['os']['bet']							   
                    except KeyError:
                        pass

        # OCF
        def runnercf():
            if client.stopped != True:
                if client.casino['enable']:
                    if client.casino['cf']['enable']:
                        if not client.checknocash:
                            sleep(1)
                            bot.typingAction(str(client.casino['channelcasinoid']))
                            sleep(0.6)
                            bot.sendMessage(str(client.casino['channelcasinoid']), "owo cf {}  ".format(client.currentcfbet))
                            casino(f"{at()} ","#b452cd")
                            casino(f"User: ","")
                            casino(f'{client.username}','#8b0a50')
                            casino(f" [SENT] owo cf {client.currentcfbet}  ","")
                            endcasino()                        
                            sleep(2)
                            client.totalcmd += 1
                            sleep(random.randint(1, 2))
        
        
        # Owo Slot
        def runneros():
            if client.stopped != True:
                if client.casino['enable']:
                    if client.casino['cf']['enable']:
                        if not client.checknocash:
                            sleep(1)
                            bot.typingAction(str(client.casino['channelcasinoid']))
                            sleep(0.6)
                            bot.sendMessage(str(client.casino['channelcasinoid']), "owo s {}  ".format(client.currentosbet))
                            casino(f"{at()} ","#b452cd")
                            casino(f"User: ","")
                            casino(f'{client.username}','#8b0a50')
                            casino(f" [SENT] owo s {client.currentcfbet}  ","")
                            endcasino()                   
                            sleep(3)
                            client.totalcmd += 1
                            sleep(random.randint(1, 3))


        def runnerhunt():
            if client.stopped != True:
                bot.typingAction(str(client.channel))
                sleep(1.5)
                bot.sendMessage(str(client.channel), "owoh")
                command(f"{at()} ","#b452cd")
                command(f"User: ","")
                command(f'{client.username}','#8b0a50')
                command(f" [SENT] owo hunt","")
                endcommand()       
                sleep(2)
                client.totalcmd += 1
                sleep(random.randint(1, 2))


        def runnerbattle():
            bot.typingAction(str(client.channel))
            sleep(2)
            bot.sendMessage(str(client.channel), "owob")
            command(f"{at()} ","#b452cd")
            command(f"User: ","")
            command(f'{client.username}','#8b0a50')
            command(f" [SENT] owo battle","")
            endcommand()    
            sleep(1.2)
            sleep(random.randint(1, 2))


        def runnerowo():
            if client.stopped != True:
                bot.typingAction(str(client.channel))
                sleep(1.3)
                bot.sendMessage(str(client.channel), "owo")
                command(f"{at()} ","#b452cd")
                command(f"User: ","")
                command(f'{client.username}','#8b0a50')
                command(f" [SENT] owo","")
                endcommand()   
                sleep(1.6)
                sleep(random.randint(1, 2))
                client.totalcmd += 1


        def runnerbuy():
            if client.stopped != True:
                bot.typingAction(str(client.channel))
                sleep(1.1)
                bot.sendMessage(str(client.channel), "owo buy 1")
                command(f"{at()} ","#b452cd")
                command(f"User: ","")
                command(f'{client.username}','#8b0a50')
                command(f" [SENT] owo buy 1","")
                endcommand()      
                sleep(0.9)
                client.totalcmd += 1
                sleep(random.randint(1, 2))


        def owoexp():
            if client.exp['enable'] and client.stopped != True:
                try:
                    response = get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
                    if response.status_code == 200:
                        json_data = response.json()
                        data = json_data['data']
                        bot.sendMessage(str(client.exp['channelspamid']), data[0]['quoteText'])
                        command(f"{at()} ","#b452cd")
                        command(f"User: ","")
                        command(f'{client.username} ','#8b0a50')
                        command(f"[SPAM]","")
                        endcommand()           
                        client.totaltext += 1
                        sleep(random.randint(1, 6))
                except:
                    pass


        def owopray():
            if client.stopped != True:
                userpray = bot.getProfile(client.praycurse['prayother']['userid'], True).json()
                if client.praycurse['prayother']['enable']:
                    bot.sendMessage(str(client.channel), f"owo {client.praycurse['mode'].lower()} <@{client.praycurse['prayother']['userid']}> ")
                    command(f"{at()} ","#b452cd")
                    command(f"User: ","")
                    command(f'{client.username}','#8b0a50')
                    command(f" [SENT] owo {client.praycurse['mode'].lower()} {userpray['user']['username']}","")
                    endcommand()                  
                else:
                    bot.sendMessage(str(client.channel), "owo curse ")
                    command(f"{at()} ","#b452cd")
                    command(f"User: ","")
                    command(f'{client.username}','#8b0a50')
                    command(f" [SENT] owo {client.praycurse['mode'].lower()}","")
                    endcommand()  
                client.totalcmd += 1
                sleep(random.randint(13, 18))


        def runnerdaily():
            if  client.stopped != True:
                bot.typingAction(str(client.channel))
                sleep(3)
                bot.sendMessage(str(client.channel), "owo daily")
                command(f"{at()} ","#b452cd")
                command(f"User: ","")
                command(f'{client.username}','#8b0a50')
                command(f" [SENT] owo daily","")
                endcommand()  

                client.totalcmd += 1
                sleep(3)
                msgs = bot.getMessages(str(client.channel), num=5)
                msgs = msgs.json()
                daily_string = ""
                length = len(msgs)
                i = 0
                while i < length:
                    if msgs[i]['author']['id'] == client.OwOID and msgs[i]['content'] != "" and "Nu" or "daily" in msgs[i]['content']:
                        daily_string = msgs[i]['content']
                        i = length
                    else:
                        i += 1
                if not daily_string:
                    sleep(5)
                    client.totalcmd -= 1
                    runnerdaily()
                else:
                    if "Nu" in daily_string:
                        daily_string = findall('[0-9]+', daily_string)
                        client.wait_time_daily = str(
                            int(daily_string[0]) * 3600 + int(daily_string[1]) * 60 + int(daily_string[2]))
                        command(f"{at()} ","#b452cd")                
                        command(f"[INFO] Next Daily: {client.wait_time_daily}s","")
                        endcommand()                    
                    if "Your next daily" in daily_string:
                        command(f"{at()} ","#b452cd")                
                        command(f"[INFO] Claimed Daily","")
                        endcommand() 

        def changeChannel() -> str:
            channel2 = []
            guildspamID = bot.getChannel(client.channelspambackup).json()['guild_id']
            channels = bot.gateway.session.guild(guildspamID).channels
            for i in channels:
                if channels[i]['type'] == "guild_text":
                    channel2.append(i)
            channel2 = random.choice(channel2)
            return channel2, channels[channel2]['name']       
        

        def threadcasino():
            ocf=0
            os=0
            main = time()
        
            while True:
                if client.stopped == True:
                    break
                if client.stopped != True:
                    
                    if time() - ocf > random.randint(17, 28) and client.stopped != True:
        
                        if client.casino['cf']['enable'] and client.checknocash == False:
                    
                            runnercf()
                        ocf = time()
                    if time() - os > random.randint(17, 28) and client.stopped != True:
    
                        if client.casino['os']['enable'] and client.checknocash == False:
                            runneros()
                        os = time()
                    if time() - main > random.randint(1000, 2000):
                        sleep(random.randint(20, 30))
                        main = time()
                    sleep(1)      
                if not client.FlagRunAuto:
                    client.stopped=True
                    bot.gateway.close()
                    casino("\n\n=============================================",'')
                    casino("\n==================STOP AUTO==================\n",'')
                    casino("=============================================\n\n",'')
                    break


        def threadrunner():
            pray = 0
            sayowo = pray
            buyring = pray
            owo = pray
            ocf = pray
            hunt = pray
            battle = pray
            selltime = pray
            daily_time = pray
            main = time()
            stop = main
            change = main

            while True:
                if client.stopped == True:
                    break
                if client.stopped != True:
                    #Hunt Mode
                    if time() - hunt > random.randint(15, 25) and client.stopped != True:
                        if client.runner['hunt']:
                            runnerhunt()
                        hunt = time()
                    #Battle Mode			
                    if time() - battle > random.randint(15, 22) and client.stopped != True:
                        if client.runner['battle']:
                            runnerbattle()
                        battle = time()
            
                    #Say owo Mode
                    if time() - sayowo > random.randint(15, 25) and client.stopped != True:
                        if client.runner['sayowo']:
                            runnerowo()
                        sayowo = time()
                    #Buy Ring Mode
                    if time() - buyring > random.randint(8, 15) and client.stopped != True:
                        if client.runner['buyring']:   
                            runnerbuy()
                        buyring = time()
            
                    #Pray/Curse Mode
                    if time() - pray > random.randint(300, 400) and client.stopped != True:
                        if client.praycurse['enable']:
                            owopray()
                        pray = time()

                    #Spam Mode
                    if time() - owo > random.randint(20, 40) and client.stopped != True:
                        if client.exp['enable']:
                            owoexp()
                        owo = time()
            
                    #Sleep Mode
                    if client.sleep['enable']:
                        if time() - main > client.sleep['time']and client.stopped != True:
                            main = time()
                            command(f"{at()} ","#b452cd")    
                            command(f"[INFO] SLEEPING",'#8b0a50')
                            endcommand()  
                        
                            sleep(client.sleep['duration'])
                            #subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                            #os.system('python "mainvip.py"')
            
                    #Spam Mode
                    if client.runner['daily']:
                        if time() - daily_time > int(client.wait_time_daily) and client.stopped != True:
                            runnerdaily()
                            daily_time = time()           

            

            
                    #Change Channel Mode
                    if client.stopped != True:
                        if time() - change > random.randint(600, 1500) and not client.stopped:
                            change=time()
                            channel = changeChannel()
                            client.exp['channelspamid'] = channel[0]
                            command(f"{at()} ","#b452cd")    
                            command(f"[INFO] Changed Channel Spaming To :","")
                            command(f"{channel[1]}",'#8b0a50')
                            endcommand()                      
                    sleep(0.1)
                if not client.FlagRunAuto:
                    client.stopped=True
                    bot.gateway.close()
                    command("\n\n=============================================",'')
                    command("\n==================STOP AUTO==================\n",'')
                    command("=============================================\n\n",'')
                    break
        
        
        def getTimebot():
            if not client.FlagRunAuto:
                pass
            if client.FlagRunAuto:
                nowtime=time()
                duration = int(nowtime-client.starttime)
                mm, ss = divmod(duration, 60)
                hh, mm= divmod(mm, 60)
                text=f'{hh:02d}:{mm:02d}:{ss:02d}'
                vtime.set(text)
                tbTimeBot.after(1000,getTimebot)

       
            
    
            

        def threadTime():
            while True:
                if not client.FlagRunAuto:
                    break
                if client.FlagRunAuto :
                    getTimebot()
                    
                
                    
        def loopie():
            	
           
            comborunner = threading.Thread(name="threadrunner", target=threadrunner)
            combocasino = threading.Thread(name="threadcasino", target=threadcasino)
            combotime = threading.Thread(name="threadTime", target=threadTime)
            if checkCasino():
                print('start casino')
                combocasino.start()
            comborunner.start()      
            getTimebot()  
            #combotime.start()
                
                
                
        bot.gateway.run() 


def solvelink():
    if client.twocaptcha['enable']:	
        api=client.twocaptcha['api']
        token =client.token



        #Setting Chrom extension
        chrome_options = uc.ChromeOptions()
        chrome_options.add_extension('TwoCaptchaAutoSolve.crx')
        driver = uc.Chrome(options=chrome_options)

        #Setting key 2Captcha Solver
        driver.get('chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html')
        inputkey = driver.find_element(By.CSS_SELECTOR, value='body > div > div.content > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]')
        driver.execute_script("document.getElementsByName('apiKey')[0].value=arguments[0]",api)

        #click Login
        loginbutton=driver.find_element(By.CSS_SELECTOR, "#connect")
        driver.execute_script("arguments[0].click();", loginbutton)

        #Tắt Alert
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

        #OWO
        driver.get('https://owobot.com/captcha')

        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button')))
        driver.find_element(By.CSS_SELECTOR, value='#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button').click()

        driver.execute_script(js + f'login("{token}")')

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]')))
        driver.find_element(By.CSS_SELECTOR, value='button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]').click()

        while True:
            #Dợi extension solver hiện rồi f5 vì để ko bị lỗi sitekey
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))        
            solvebutton=driver.find_element(By.CLASS_NAME, "captcha-solver")
            sleep(3)
            driver.execute_script("arguments[0].click();", solvebutton)
            if WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "captcha-solver-info"), "Solving")):
                break
            #Wait 
        if WebDriverWait(driver, 200).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#app > div > main > div > div > div > div:nth-child(2) > div > div.v-card__actions.mb-3.welcome-text > div"), "I have verified that you're a human")):
            print('Solve Captcha Succesfully')		
            webhookPing(f"Solve Captcha link successfully")
            driver.quit()		
            return "solved"
        else:	
            return "captcha"
    else:
        return "captcha"				

def checkCasino():
    if client.casino['enable']:
        if client.casino['cf']['enable'] or client.casino['os']['enable']:
            return True
        else:
            return False
    else:
        return False


def captchamusic():
    if client.sound == 'yes':
        playsound('KhueMocLang.mp3')
    #playsound('Captcha.mp3')
    

def solvedmusic():
    if client.sound == 'yes':
        playsound('Solved.mp3')
        #playsound('KhueMocLang.mp3')

def kiepdoden():
    if client.sound=='yes':
        playsound("KiepDoDen.mp3")
    
def webhookPing(message):
        if client.webhook != 'None':
            webhook = DiscordWebhook(url=client.webhook['link'], content=message)
            webhook = webhook.execute()
def webhookping():
    if client.webhook['enable'] :
        
        if checkCasino():
            webhookPing(f"<@{client.webhook['pingid']}> I Found A Captcha In Channel: <#{client.channel}> or <#{client.casino['channelcasinoid']}> . User:{client.username} <@{client.userid}>")			
        else:
            webhookPing(f"<@{client.webhook['pingid']}> I Found A Captcha In Channel: <#{client.channel}>  . User:{client.username} <@{client.userid}>")

    else:
        if checkCasino() :
            webhookPing(f"<@{client.userid}>  I Found A Captcha In Channel: <#{client.channel}>  or <#{client.casino['channelcasinoid']}> . User:{client.username} <@{client.userid}>")
        else:
            webhookPing(f"<@{client.userid}> I Found A Captcha In Channel: <#{client.channel}>. User:{client.username} <@{client.userid}>")

def at():
    return f'{strftime("%d %b %Y %H:%M:%S", localtime())}'

def substring_after(s, substring):
    return s.partition(substring)[2]           
         
def substring_before(s,substring):
    return s.partition(substring)[0]

def on_exit():
    """When you click to exit, this function is called"""
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        Form.destroy()
        client.stopped=True
        if client.CheckRunningAuto:
            client.FlagRunAuto=False
        


if __name__ == '__main__':
    Form=Tk()
    Form.title("ELSA Selbot Owo")
 
    Form.geometry("1190x724")
    Form['bg']='#aad6ff'  #background 
    Form.attributes('-topmost',False) #Code cho cửa sổ luôn nằm trên top
    Form.iconbitmap('Elsaicon.ico')
    Form.resizable(height=False,width=False)
    Form.protocol("WM_DELETE_WINDOW", on_exit)
    cf=create_form(Form)

    Form.mainloop()
