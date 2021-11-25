#!/bin/bash

#                 COLORES ALTOS
negro="\e[1;30m"
azul="\e[1;34m"
verde="\e[1;32m"
cian="\e[1;36m"
rojo="\e[1;31m"
purpura="\e[1;35m"
amarillo="\e[1;33m"
blanco="\e[1;37m"
#                 COLORES BAJOS
black="\e[0;30m"
blue="\e[0;34m"
green="\e[0;32m"
cyan="\e[0;36m"
red="\e[0;31m"
purple="\e[0;35m"
yellow="\e[0;33m"
white="\e[0;37m"
#

if [ ! -e $PREFIX/bin/ShareFile ]; then
clear
echo -e "\n${rojo}Primero ejecute install.py!!!\n"
exit

fi

banner(){
clear
echo -e "${red}=========Developer o=[]=====> M01000========"
echo -e "${amarillo} ____  _                    _____ _ _       "
echo -e "/ ___|| |__   __ _ _ __ ___|  ___(_) | ___  "
echo -e "\___ \|  _ \ / _\\ | /__/ _ \ |_  | | |/ _ \\"
echo -e " ___) | | | | (_| | | |  __/  _| | | |  __/ "
echo -e "|____/|_| |_|\__/_|_|  \___|_|   |_|_|\___| "
echo ""
echo -e "${red}=========Developer o=[]=====> M01000========"
echo ""
}

instrucciones(){
clear
echo""
echo -e "${purple}===============INTRUCCIONES==============="
echo""
echo -e "[1] Abre otra seseion sin borrar esta"                   
echo -e "[2] Dirijete a donde esta la carpeta que vas a"
echo -e "    compartir"
echo ""
echo -e "[3] Ejecuta el Script en la carpeta > ShareFile"
echo ""
echo -e "[4] Preciona la opcion 2 "
echo -e -n "[~] Listo con el link pasalo a alguien y listo
    podra ver ese directorio que selecionastes"
echo -e "===============INSTRUCCIONES==============="
echo ""
echo -e "\e[33m       Presiona ctrl + c para salir"
echo ""
}

link(){
clear
echo ""
pkill -f -2 ngrok > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1
pkill -f -2 curl > /dev/null 2>&1
killall -2 curl > /dev/null 2>&1
pkill -f -2 python3 > /dev/null 2>&1
killall -2 python3  > /dev/null 2>&1
python3 -m http.server 8080 &> /dev/null &
sleep 8
ngrok http 8080 > /dev/null 2>&1 &
sleep 8
echo -e "${amarillo}Servidor 1 abierto"
echo ""
echo -e "${amarillo}Abriendo Sevidor 2..."
share=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9A-Za-z.-]*\.ngrok.io")
sleep 6
echo ""
echo -e "${amarillo}${amarillo}Servidor 2 abierto"
sleep 2
echo ""
echo -e "${amarillo}Obteniendo link..."
sleep 6
echo -e "${amarillo}Enlace >>>> ${blanco}" ${share}
}

finish(){
clear
pkill -f -2 ngrok > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1
pkill -f -2 curl > /dev/null 2>&1
killall -2 curl > /dev/null 2>&1
echo -e "\n${red} Conexiom Finalizada ✓\n"
sleep 5
ShareFile
}

link2(){
echo -e -n "${rojo}
[${blanco}1${rojo}] ${amarillo}Pc
${rojo}[${blanco}2${rojo}] ${amarillo}Mobile
${rojo}?>" ${blanco}
read -r op
if [[ ${op} == "01" || ${op} == "1" ]]; then
clear
echo -e "${rojo}------------------------"
echo -e "${amarillo}   Contact Developer    "
echo -e "${rojo}------------------------"
echo ""
echo -e "${rojo}[${blanco}https://t.me/HackForAll1${rojo}]"
echo ""
echo ""
elif [[ ${op} == "02" || ${op} == "2" ]]; then
clear
termux-open https://t.me/HackForAll1
bash ShareFile.sh
else
echo -e "${rojo}Option Incorrct!!"
sleep 1
bash ShareFile.sh
fi
}

adios(){
clear
echo -e -n "                Recuerda segirme en GitHub
                https://GitHub.com/UserM01000/
                porque estare subiendo mas scripts,
                ejecutables, etc echos en Python, Bash y
                C++!!!. Adios"
		echo ""
}


Menu(){

banner
echo -e "${rojo}[${white}1${rojo}] Compartir Archivo\e[0m"
echo -e "${rojo}[${white}2${rojo}] Optener Link Ngrok\e[0m"
echo -e "${rojo}[${white}3${rojo}] Finalizar La Conexion"
echo -e "${rojo}[${white}4${rojo}] [telegram]"
echo -e "${rojo}[${white}5${rojo}] exit"
echo ""
echo -e -n "${rojo}
╔────[${white}Selecciona una Opción${rojo}] ${rojo}
╚──➤" ${white}
read -r OPCION
if [[ ${OPCION} == "01" || ${OPCION} == "1" ]]; then
          instrucciones
elif [[ ${OPCION} == "02" || ${OPCION} == "2" ]]; then
	  link
elif [[ ${OPCION} == "03" || ${OPCION} == "3" ]]; then
	  finish
elif [[ ${OPCION} == "04" || ${OPCION} == "4" ]]; then
          link2
elif [[ ${OPCION} == "05" || ${OPCION} == "5" ]]; then
         adios
else 
echo -e "${rojo} OPCION INVALIDA "
sleep 1
banner
Menu

fi
}
Menu

