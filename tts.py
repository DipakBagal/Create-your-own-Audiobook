#importing Google text to speech library and PDF conversion library
from gtts import gTTS

import PyPDF2

#text stores the String that should be converted to sound
text= " "

#creating a pdf file object
pdfFileObj = open('Ashlee Vance - Elon Musk; Tesla, SpaceX, and the Quest for a Fantastic Future.pdf', 'rb')

#creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#printing number of pages in pdf file
print(pdfReader.numPages)

total_pages= pdfReader.numPages

for i in range(0, int(total_pages)):
     pageObj = pdfReader.getPage(i)
     # extracting text from page
     text+= pageObj.extractText()

tts= gTTS(text=text) # Optional parameter is lang="" which is by default English

# Saving tts as sound.mp3
tts.save("sound.mp3")

# closing the pdf file object
pdfFileObj.close()
