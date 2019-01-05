import QChatterChannel
import QChatterUser
import QChatterServer 

import QChatterPyFunctions

from QChatterPyFunctions import error_codes
from QChatterPyFunctions import translate
from QChatterPyFunctions import printerror
from QChatterPyFunctions import helpmenu


import constants


import sys
import os
import json
import time
import threading

import pygame

import asyncio

from io import StringIO

import csv

from blessed import Terminal


import readline



term = Terminal()

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("notification.mp3")

exec(open("settings.py", "r").read()) # To read configuration file


getmessages_thread = True

def getmessages(qchannel, quser):
    print(qchannel.returnChannelDescription(qchannel.channel))
    while True:
        try:
            if (not getmessages_thread):
                break
            
            messages = json.loads(quser.obtainUserMessageFromChannel(qchannel.channel))
            #print(messages)
            for message in messages:
                if (str(message) != "50000"):
                    json_decode = message
                    human_time = time.ctime(int(json_decode["time"]))
                    title_status = json_decode["title_status"]
                    font_type = json_decode["font_type"]

                    

                    if (quser.username == json_decode["title"]):
                        continue

                    
                    title = ""

                    if (title_status == QChatterPyFunctions.c_u_master):
                        title = "@{title}".format(title = term.yellow(json_decode["title"]))
                    elif (title_status == QChatterPyFunctions.c_u_bot):
                        title = "[BOT] {title}".format(title = term.green(json_decode["title"]))
                    else:
                        #print(title_status)
                        title = json_decode["title"]
                    pygame.mixer.music.play()

                    if (font_type == "b"):
                        content = term.bold(content)
                    else:
                        content = json_decode["content"]
                    print("[{time}]  <{title}> {content}".format(time = human_time, title = title, content = content))
            time.sleep(1.2)
        except Exception as ecp:
            pass
            #print(ecp)
            
        
async def main():
    
    readline.parse_and_bind("tab: complete")

    if (len(sys.argv) > 1):
        if (sys.argv[1] == "--register"):
            print(QChatterUser.registerUser(sys.argv[2], sys.argv[3], sys.argv[4]))
            exit()
        elif (sys.argv[1] == "--join-channel"):
            print(QChatterUser.joinChannel(sys.argv[2], sys.argv[3], sys.argv[4]))
            exit()

        elif (sys.argv[1] == "--register-bot"):
            print(QChatterUser.registerBot(sys.argv[2], sys.argv[3], sys.argv[4]))
            exit()
        


    print("CONNECTED TO " + constants.SERVER_IP_DNS)
    print(QChatterServer.getMotd())
    username = ""
    password = ""


    if (auto_signin):
        username = auto_signin_username
        password = auto_signin_password



        try:
           quser = QChatterUser.QChatterUser(username, password)
        except QChatterUser.QChatterUser.QChatterCredentialsError:
            print("Authentication error.")
    else:
        while True:
            username = input("Username: ")
            password = input("Password: ")

            try:
                quser = QChatterUser.QChatterUser(username, password)
                break
            except QChatterUser.QChatterUser.QChatterCredentialsError as error:
                print("Authentication error.")


    #while True:
    #    print("Want to load a channel? Type the command loadchannel")
    #    command = input(">>>")
    #
    #    if (command == "loadchannel"):
    #        break

    _channel = input("Channel: ")
    qchannel = QChatterChannel.QChatterChannel(_channel)

    #print(QChatterUser.obtainUserMessageFromChannel(username, password, channel))
    #print(qchannel.returnChannelDescription())

    threading._start_new_thread(getmessages, (qchannel, quser,))

    while True:
        message = input("")
        sys.stdout.write("\033[F") #back to previous line
        sys.stdout.write("\033[K") #clear line
        message_no_slash = message.replace("/", "", 1)
        message_split = message_no_slash.split(" ")
        
        if (message_split[0] == "/"):
            print(term.red("--- DID YOU TYPE A COMMAND? MAKE SURE THE FIRST CHARACTER IS A SLASH! YOU MIGHT REVEAL THE PASSWORD ---"))
            continue


        if (message.startswith("/")):
            if (message_split[0] == "set_channel_description"):
                printerror(translate(qchannel.setChannelDescription(" ".join(message_split[2:]), message_split[1])))
            elif (message_split[0] == "create_channel"):
                printerror(translate(QChatterChannel.createChannel(message_split[1], message_split[2], message_split[3])))
            elif (message_split[0] == "join_channel"):
                printerror(translate(quser.joinChannel(message_split[1])))
            elif (message_split[0] == "clear"):
                os.system("clear")
            elif (message_split[0] == "get_op"):
                printerror(translate(quser.getOp(qchannel.channel, message_split[1])))
            elif (message_split[0] == "help"):
                helpmenu()
            elif (message_split[0] == "leave_channel"):
                printerror(translate(quser.leaveChannel(channel)))
            
            elif (message_split[0] == "new_channel"):
                getmessages_thread = False
                channel = message_split[1]
                getmessages_thread = True
                threading._start_new_thread(getmessages, (qchannel, quser,))

            elif (message_split[0] == "s"):
                print(QChatterServer.executeServerCommand(" ".join(message_split[1:])))

            else:
                print("Invalid command")


        else:
            print(qchannel.sendMessage(quser.username, message, quser.password))
            #printerror(translate(response))
            print("[{time}]  <{title}> {content}".format(time = time.ctime(time.time()), title = term.red(username), content = message))
            #sys.stdout.write("\033[F") #back to previous line
            #sys.stdout.write("\033[K") #clear line

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
