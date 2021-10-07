#A text-to-speech converter using gTTs
#gTTS is used to covert the text into speech while os is used to load the save file.

from gtts import gTTS 
import os

def speak(str):
	language = 'en'
	speech = gTTS(text = str, lang = language, slow = False)
	speech.save('text.mp3')
	os.system('start text.mp3')
	
if __name__ =='__main__':
	b=input("ENTER A STRING:")
	speak(b)