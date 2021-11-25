import subprocess
import os
import time

os.system("clear")
print("Bienvenid@ y gracias por usar este script")
print("y gracias P3rs0N 7r5sh y https://github.com/AnibalGthub")
print("por las colaboraciones en este script:D\n")
time.sleep(5)

op = subprocess.run(['uname', '-o'], capture_output=True, text=True)
op = op.stdout[:-1]

if( op == 'GNU/Linux'):
    os.system("sudo apt-get update -y && sudo apt-get upgrade -y")
    os.system("clear")
    print("Terminal actializada correctamente :D")
    time.sleep(5)
    print("Calma esto no tomara mucho tiempo ;D\n")
    os.system("sudo apt-get install wget -y")
    os.system("sudo apt-get install unzip -y")
    time.sleep(3)
    print("\nInstalando el ultimo requisito")
    time.sleep(5)
    arch = subprocess.run(['uname', '-m'], capture_output=True, text=True)
    arch = arch.stdout[:-1]

    print(arch)

    if( arch == 'armv7l' or arch == 'arm' or arch == 'armhf' ):
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip', '-O', 'ngrok.zip'], shell=False) 
        os.system("unzip -o ngrok.zip > /dev/null 2>&1")
        os.system("sudo rm ngrok.zip > /dev/null 2>&1")
        os.system("clear")
        print("Disfruta de este maravillo script :D")
        time.sleep(3)
    elif( arch == 'armv8l' or arch == 'aarch64' or arch == 'arm64' ):
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip', '-O', 'ngrok.zip'], shell=False)
        os.system("unzip -o ngrok.zip > /dev/null 2>&1")
        os.system("sudo rm ngrok.zip > /dev/null 2>&1")
        os.system("clear")
        print("Disfruta de este maravillo script :D")
        time.sleep(3)
    elif( arch == 'x64' or arch == 'x86_64' or arch == 'amd64' ):
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip', '-O', 'ngrok.zip'], shell=False)
        os.system("unzip -o ngrok.zip > /dev/null 2>&1")
        os.system("sudo rm ngrok.zip > /dev/null 2>&1")
        os.system("clear")
        print("Disfruta de este maravillo script :D")
        time.sleep(3)
    elif( arch == 'x86' or arch == 'i386' or arch == 'i686' ):
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip', '-O', 'ngrok.zip'], shell=False)
        os.system("unzip -o ngrok.zip > /dev/null 2>&1")
        os.system("sudo rm ngrok.zip > /dev/null 2>&1")
        os.system("clear")
        print("Disfruta de este maravillo script :D")
        time.sleep(3)
    else:
        print("Arquitectura no encontrada :(")
        print("Problmeas? Contact Developer?")
        print("https://t.me/HackForAll1")

    os.system("clear")

    os.system("sudo cp -n ShareFile.sh ShareFile")
    os.system("chmod +x ShareFile")
    os.system("sudo mv -n ShareFile /usr/bin")
    os.system("sudo rm install.py")
    os.system("bash ShareFile.sh")

elif( op == 'Android' ):
    os.system("pkg update -y && pkg upgrade -y")
    print("\nCalma esto no toma tiempo ;D\n")
    time.sleep(5)    
    os.system("clear")
    print("Terminal Actualizadada correctamente :D\nInstalacion de los requisito")
    time.sleep(5)
    os.system("clear")
    os.system("pkg install wget -y && pkg install unzip -y")

    arch = subprocess.run(['uname', '-m'], capture_output=True, text=True)
    arch = arch.stdout[:-1]

    print(arch)

    if( arch == 'armv7l' or arch == 'arm' or arch == 'armhf' ):
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip', '-O', 'ngrok.zip'], shell=False) 
        os.system("unzip -o ngrok.zip > /dev/null 2>&1")
        os.system("rm ngrok.zip > /dev/null 2>&1")
        os.system("clear")
        print("Disfruta de este maravillo script :D")
        time.sleep(3)
    elif( arch == 'armv8l' or arch == 'aarch64' or arch == 'arm64' ):
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip', '-O', 'ngrok.zip'], shell=False)
        os.system("unzip -o ngrok.zip  > /dev/null 2>&1")
        os.system("rm ngrok.zip > /dev/null 2>&1")
        os.system("clear")
        print("Disfruta de este maravillo script :D")
        time.sleep(3)
    elif( arch == 'x64' or arch == 'x86_64' or arch == 'amd64' ):
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip', '-O', 'ngrok.zip'], shell=False)
        os.system("unzip -o ngrok.zip > /dev/null 2>&1")
        os.system("rm ngrok.zip > /dev/null 2>&1")
        os.system("clear")
        print("Disfruta de este maravillo script :D")
        time.sleep(3)
    elif( arch == 'x86' or arch == 'i386' or arch == 'i686' ):
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip', '-O', 'ngrok.zip'], shell=False)
        os.system("unzip -o ngrok.zip  > /dev/null 2>&1")
        os.system("rm ngrok.zip > /dev/null 2>&1")
        print("Disfruta de este maravillo script :D")
        time.sleep(3)
    else:
        print("Arquitectura no encontrada :(")
        print("Problmeas? Contact Developer?")
        print("https://t.me/HackForAll1")
  
    os.system("clear")
    
    os.system("cp -n ShareFile.sh ShareFile")
    os.system("chmod +x ShareFile")
    os.system("mv -n ShareFile $PREFIX/bin")
    os.system("rm install.py")
    os.system("bash ShareFile.sh")
    
