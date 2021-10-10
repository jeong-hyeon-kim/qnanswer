from selenium import webdriver
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start()
path = '/Users/kimjeonghyeon/Downloads/question_211008'
browser = webdriver.Chrome(path)

