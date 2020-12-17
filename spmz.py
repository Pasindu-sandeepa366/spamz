#!/usr/share/python3

from time import sleep
#from pynput.keyboard import Key, Listener
#from threading import Thread
import pyautogui
from colorama import Fore, Style
import os,platform,clipboard


global green,blue,red,end
green = Fore.GREEN
blue = Fore.BLUE
red = Fore.RED
end = Style.RESET_ALL
if platform.system()=='Linux':
	cle = 'clear'
elif  platform.system()=='Windows':
	cle = 'cls'


def main():
	banner()
	print(f'''
	{blue}
	[1] Spam msg
	[2] Crash msg
	{end}
	''')
	choice=input(' >> ')
	if choice == '1':
		msg,num,delay=data()
		spaming(msg,num,delay)
	elif choice == '2':
		crash()




def banner():
	print(f'''{blue}
	:'######::'########:::::'###::::'##::::'##::::::::::'########:
	'##... ##: ##.... ##:::'## ##::: ###::'###::::::::::..... ##::
	##:::..:: ##:::: ##::'##:. ##:: ####'####:::::::::::::: ##:::
	. ######:: ########::'##:::. ##: ## ### ##::::::::::::: ##::::
	:..... ##: ##.....::: #########: ##. #: ##:::::::::::: ##:::::
	'##::: ##: ##:::::::: ##.... ##: ##:.:: ##::::::::::: ##::::::
	. ######:: ##:::::::: ##:::: ##: ##:::: ##:'#######: ########:
	:......:::..:::::::::..:::::..::..:::::..::.......::........::

	{red}
	\t[+]Coded_by_Pasindu_Sandeepa
	\t[@]bombtiktiktik54321@gmail.com
	\t[+]Special_Tnkz_Maneesha
	{end}
	''')

def data():
	msg=input(f'{green}Spam msg > {blue}')
	try:
		delay=0
		delay=float(input(f'{green}Delay >{blue} '))
	except ValueError:
		print(f'{red}ValueError{end}')
		print(f'{blue}Delay seted = 0{end}')
	try:
		num=int(input(f'{green}Number of Msg you wan to send > {blue} '))
	except ValueError:
		print('{red}ValueError{end}')
		quit()
	return msg,num,delay;


def spaming(msg,num,delay):
	os.system(cle)
	count=0
	input(f'{blue}\n\tPress enter to start attack..!{end}')
	while True:
		banner()
		print(f'{blue}\n\tCountdown for starting attack {red}[{5-count}]{end}')
		sleep(0.9)
		os.system(cle)
		count+=1
		if count==5:
			break;
		else:
			pass
	count=0
	while count < num:
		count+=1
		pyautogui.typewrite(msg)
		pyautogui.press('enter')
		sleep(delay)
		os.system(cle)
		banner()
		print(f'Status : {red}{count}/{blue}{num}')
		print(f'Completed : {blue}{round(count/num*100)}%')
		print(f'\t','='*(round(count/num*50)),'>>')
		print('[Running..!]')
	os.system(cle)
	banner()
	print(f'''{green}
	Status : {red}{count}/{blue}{num}
	Completed : {blue}{round(count/num*100)}%
		================================================== >>
	[Compleated..!]{end}
	
	
	''')

#######################################################################################################
def crash():
	num,delay = cdata()
	os.system(cle)
	f=open('msg.txt','r')
	msg=f.read()

	clipboard.copy(msg)
	f.close()
	count=0
	input(f'{blue}\n\tPress enter to start attack..!{end}')
	while True:
		banner()
		print(f'{blue}\n\tCountdown for starting attack {red}[{5-count}]{end}')
		sleep(0.9)
		os.system(cle)
		count+=1
		if count==5:
			break;
		else:
			pass
	count=0
	while count < num:
		count+=1
		#pyautogui.typewrite(msg)
		pyautogui.keyDown('ctrl')
		pyautogui.press('v')
		pyautogui.keyUp('ctrl')
		pyautogui.press('enter')
		sleep(delay)
		os.system(cle)
		banner()
		print(f'Status : {red}{count}/{blue}{num}')
		print(f'Completed : {blue}{round(count/num*100)}%')
		print(f'\t','='*(round(count/num*50)),'>>')
		print('[Running..!]')
	os.system(cle)
	banner()
	print(f'''{green}
	Status : {red}{count}/{blue}{num}
	Completed : {blue}{round(count/num*100)}%
		================================================== >>
	[Compleated..!]{end}
	
	
	''')


def cdata():
	try:
		delay=0.2
		delay=float(input(f'{green}Delay >{blue} '))
	except ValueError:
		print(f'{red}ValueError{end}')
		print(f'{blue}Delay seted = 0.2{end}')
	try:
		num=int(input(f'{green}Number of Msg you wan to send > {blue} '))
	except ValueError:
		print('{red}ValueError{end}')
		quit()
	return num,delay;

if '__main__' == __name__:
	main()