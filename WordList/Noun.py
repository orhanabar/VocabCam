from html.parser import HTMLParser
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.geeksforgeeks.org/part-speech-tagging-stop-words-using-nltk-python/")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup.prettify()

messages = soup.find_all('blockquote')


for tdTag in messages:
    content = tdTag.find("p").text
    # print(content)
# driver.close()
file = open("nltkTags.txt", "r")

print(file.read())
