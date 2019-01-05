import requests
import os
from constants import *


def getMotd():
    return requests.post("{ip}/Server/motd.php".format(ip = SERVER_IP_DNS)).text


def executeServerCommand(command):
    return requests.post("{ip}/Command/issue_command.php".format(ip = SERVER_IP_DNS), {"command": command}).text