import requests
import sys


def checking_command():
    command = sys.argv[1::]
    command.split(' ')

    uname = reading_files()
    passwd = reading_files()
    

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