

def translate(string):
    if string in error_codes:
        return error_codes[string]
    else:
        return None

def printerror(translate_ret):
    if (translate_ret != None):
        print(translate_ret)

c_u_normal = "0"
c_u_master = "1"
c_u_bot = "2"

e_channel_has_password = "10201"
e_channel_does_not_have_password = "10200"

e_channel_password_denied = "102080"
e_channel_password_accepted = "102081"
e_channel_password_mismatch = "105200"

e_channel_does_exist = "1071"
e_channel_does_not_exist = "1070"

e_masterpassword_strcmp_failed = "25200"

e_user_password_denied = "302080"
e_user_password_confirmation_failure = "30200"

e_user_credentials_mismatch = "90000"
e_user_credentials_match = "90001"

e_user_is_in_channel = "40001"
e_user_is_not_in_channel = "40000"
e_user_channel_data_does_not_exist = "50000"

e_command_does_not_exist = "20102"
e_command_incorrect_number_of_arguments = "20103"

error_codes = {
    e_channel_has_password: "Channel does have password",
    e_channel_does_not_have_password: "Channel does not have password",
    e_channel_password_denied: "Channel password denied.",
    e_channel_password_accepted: "Channel password accepted.",
    e_channel_password_mismatch: "Channel masterpasswords do not match.",
    e_channel_does_exist: "Channel already exists.",
    e_channel_does_not_exist: "Channel doesn't exist, good/bad.",
    e_masterpassword_strcmp_failed: "Masterpassword incorrect.",
    e_user_password_denied: "User password was denied.",
    e_user_password_confirmation_failure: "User passwords don't match.",
    e_user_credentials_match: "User credentials match.",
    e_user_credentials_mismatch: "User credentials mismatched.",
    e_user_is_in_channel: "User is already in channel.",
    e_user_is_not_in_channel: "User is not in channel.",
    e_user_channel_data_does_not_exist: "",
    e_command_does_not_exist: "Server command does not exist",
    e_command_incorrect_number_of_arguments: "Server command: incorrect number of arguments passed."
}


def helpmenu():
    print("--- HELP ---")
    for key in help_commands:
        print("[{key}]        {description}".format(key = str(key), description = help_commands[key]))

    print("--- HELP ---")


help_commands = {
    "set_channel_description": "Sets the description of the channel. Requires masterpassword. e.g: set_channel_description <masterpassword>",
    "create_channel": "Creates a channel. e.g: create_channel <channel_name> <masterpassword> <masterpassword_again>",
    "join_channel": "Joins a channel. e.g: join_channel <channel>",
    "clear": "Clears the screen. e.g: clear <no_args>",
    "get_op": "Sets OP status on channel. e.g: get_op <masterpassword>",
    "help": "Prints me. Self explanatory.",
    "new_channel": "Changes the viewing channel"
}
