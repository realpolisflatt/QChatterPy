import requests
import os
import constants


class QChatterChannel:

    def __init__(self, _channel, _password = ""):
        self.channel = _channel
        self.password = ""
    

    def sendMessage(self, title, message, user_password):
        post_parameters = {"channel": self.channel, "title": title, "content": message, "user_password": user_password}
        return requests.post("{ip}{messages_dir}send.php".format(ip = constants.SERVER_IP_DNS, messages_dir = constants.MESSAGES_DIR), post_parameters).text

    def returnChannelDescription(self, password = ""):
        """ Optional password option. Use only if channel has password """
        post_parameters = {"channel": self.channel, "password": password, "mode": "get"}
        return requests.get("{ip}Channel/channel_get_description.php".format(ip = constants.SERVER_IP_DNS), post_parameters).text

    def setChannelDescription(self, description_text, masterpassword):
        post_parameters = {"channel": self.channel, "masterpassword": masterpassword, "description": description_text, "mode": "set"}
        return requests.post("{ip}Channel/channel_set_description.php".format(ip = constants.SERVER_IP_DNS), post_parameters).text


    def channelAddPassword(self, password, password_confirmation):
        post_parameters = {"channel": self.channel, "password": password, "password_confirm": password_confirmation}
        return requests.post("{ip}Channel/channel_create_password.php".format(ip = constants.SERVER_IP_DNS), post_parameters)

def createChannel(channel_name, masterpassword, masterpassword_confirmation):
        post_parameters = {"channel": channel_name, "masterpassword": masterpassword, "masterpassword_confirm": masterpassword_confirmation}
        return requests.post("{ip}Channel/channel_create.php".format(ip = constants.SERVER_IP_DNS), post_parameters).text


