import requests
import sys


def checking_command():
    command = sys.argv[1::]
    command.split(' ')
    if '-u' in command:
        index = command.index('-u')
        uname_file = command[index + 1]
    if '-p' in command:
        index = command.index('-p')
        passwd_file = command[index + 1]
    uname = reading_files(uname_file)
    passwd = reading_files(passwd_file)


def reading_files():
    with 


def connecting_to_site(url, username, passwd):
    login_data = {
        'username': username,
        'password': passwd
    }
    response = requests.post(url, data=login_data)

    if response.status_code(200):
        print(f'{username} and {passwd} found')


checking_command()