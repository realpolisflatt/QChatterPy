import requests
import os
import constants


class QChatterUser(object):
    class QChatterCredentialsError(Exception):
        pass
        




    def __init__(self, _username, _password):
        self.username = _username
        self.password = _password

        if (not userMatchCredentials(self.username, self.password)):
            raise self.QChatterCredentialsError("Credentials do not match.")
        





    def obtainUserMessageFromChannel(self, channel):
        post_parameters = {"channel": channel, "username": self.username, "password": self.password}
        reponse = requests.get("{ip}/Profile/get_channel_message.php".format(ip = constants.SERVER_IP_DNS), post_parameters)
        return reponse.text

    def joinChannel(self, channel):
        post_parameters = {"channel": channel, "username": self.username, "password": self.password}
        return requests.post("{ip}/Profile/join_channel.php".format(ip = constants.SERVER_IP_DNS), post_parameters).text

    def getOp(self, channel, masterpassword):
        response = requests.post("{ip}/Profile/get_op_channel.php".format(ip = constants.SERVER_IP_DNS), {"username": self.username, "password": self.password, "channel": channel, "masterpassword": masterpassword}).text

        return response

    def leaveChannel(self, channel):
        post_parameters = {"username": self.username, "password": self.password, "channel": channel}
        response = requests.post("{ip}/Profile/leave_channel.php".format(ip = constants.SERVER_IP_DNS), post_parameters)

        return response.text

    
        

def registerUser(username, password, password_confirm):
    post_parameters = {"username": username, "password": password, "password_again": password_confirm}
    return requests.post("{ip}/Profile/register.php".format(ip = constants.SERVER_IP_DNS), post_parameters).text

def registerBot(bot_username, bot_password, bot_password_verify):
    post_parameters = {"bot_username": bot_username, "bot_password": bot_password, "bot_password_verify": bot_password_verify}
    return requests.post("{ip}/Bot/create_bot.php".format(ip = constants.SERVER_IP_DNS), post_parameters).text


def userMatchCredentials(user, password):
    post_parameters = {"username": user, "password": password}
    response = requests.get("{ip}/Profile/check_user_credentials.php".format(ip = constants.SERVER_IP_DNS), post_parameters).text

    if (str(response) == "90000"):
        return False
    elif (str(response) == "90001"):
        return True


