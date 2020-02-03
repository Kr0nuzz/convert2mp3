#!/usr/bin/env python3

from pytube import YouTube as yt
from time import sleep
from halo import Halo
import sys, pytube, os, halo


def banner():
	print ("""  ______                                 ______             ________
 / _____)                           _   (_____ \           (_______/
| /      ___  ____ _   _ ____  ____| |_   ____) )____  ____   ____  
| |     / _ \|  _ \ | | / _  )/ ___)  _) /_____/|    \|  _ \ (___ \ 
| \____| |_| | | | \ V ( (/ /| |   | |__ _______| | | | | | |____) )
 \______)___/|_| |_|\_/ \____)_|    \___|_______)_|_|_| ||_(______/ 
                                                      |_|           """)
	sleep(0.5)
	print ("Author		:Kr0nuzz")
	sleep(0.5)
	print ("Purpose		:Convert Youtube Video To mp3")
	sleep(0.5)

def inti():
	link = input('Masukkan Link>> ')
	name = input('Masukkan Nama File>> ')
	pip = name+'.mp4'
	kontol = name+'.mp3'
	spinner = Halo(text='Sedang Mengkonversi', spinner='dots')
	spinner.start()
	if os.name == 'posix':
		lokasi = os.getcwd()+ '/'
	else:
		print ("maaf platform anda tidak support")
	suk = yt(link)
	print (suk.title)
	suk.streams.filter(only_audio=True).first().download(filename=name)
	spinner.stop()
	os.system("mv {} {}". format(pip, kontol))

if __name__=='__main__':
	banner()
	inti()
