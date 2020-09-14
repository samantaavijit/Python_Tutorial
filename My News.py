from win32com.client import Dispatch
import requests
import json


def speak(msg):
    sp = Dispatch("SAPI.SpVoice")
    sp.Speak(msg)


if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b139f36e0d8844b8a77347a536ac3588"
    news = requests.get(url).text
    newsDict = json.loads(news)
    arts = newsDict["articles"]
    for article in arts:
        speak(article['title'])
        speak("...")
        speak(article['content'])
        speak("Next..")
    speak("Thanks for listening..")
