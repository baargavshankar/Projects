import pyttsx3
import PyPDF3
path = open("essay.pdf",'rb')
pdfreader = PyPDF3.PdfFileReader(path)
from_page = pdfreader.getPage(7)
text = from_page.extractText()
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
