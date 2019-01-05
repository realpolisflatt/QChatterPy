import QChatterChannel
import QChatterUser

import threading

import json

import time


def on_message(username, password, channel):
    while True:
        try:
            messages = QChatterUser.obtainUserMessageFromChannel(username, password, channel).split("\n")
            for message in messages:
                if(str(message) != "50000"):
                    json_decoded = json.loads(message)
                    
                    title = json_decoded["title"]
                    content = json_decoded["content"]

                    if (title == username):
                        continue

                    if (content.startswith("$")):
                        content_split = content.split(" ")

                        if (content_split[1] == "hi"):
                            QChatterChannel.sendMessage(channel, username, "Hello! I am TWE-QChatter Bot!", password)

                        elif (content_split[1] == "say"):
                            QChatterChannel.sendMessage(channel, username, "{author} told me to say: {stuff}".format(author = title, stuff = " ".join(content_split[2:])), password)
                        
                        else: 
                            QChatterChannel.sendMessage(channel, username, "Invalid command", password)
        except:
            pass
        
        finally:
            time.sleep(1.2)





username = "teamwebot"
password = "pathosandice"
channel = "teamwe"

if (not QChatterUser.userMatchCredentials(username, password)):
    print("CREDENTIALS WRONG")
    exit(1)


threading._start_new_thread(on_message, (username, password, channel,))
while True:
    text = input("cmd>")
    text_split = text.split(" ")

    if (text_split[0] == "join"):
        QChatterUser.joinChannel(username, password, channel)
    elif (text_split[0] == "say"):
        QChatterChannel.sendMessage(channel, username, " ".join(text_split[1:]), password)
