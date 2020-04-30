import paramiko
from selenium import webdriver
import time

def sshexecute ( hostname, username, password ):
    commands = [
    "pwd",
    "id",
    "uname -a",
    "df -h"
   ]
# initialize the SSH client
    client = paramiko.SSHClient()
# add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()
# execute the commands
    for command in commands:
        print("="*50, command, "="*50)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)

def openbrowser ( url ):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    driver.close()

sshexecute( hostname = '172.16.140.165', username = 'root', password = 'Combis123$')
openbrowser( url = "http://facebook.com")