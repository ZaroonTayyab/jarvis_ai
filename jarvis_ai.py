import datetime
import webbrowser
import os
import wikipedia
import random
import requests
def get_news():
    print("Jarvis: Fetching latest news...")
    webbrowser.open("https://news.google.com")
def get_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "I told my wife she should embrace her mistakes. She gave me a hug!",
        "What do you call fake spaghetti? An impasta!",
        "I would tell you a joke about UDP... but you might not get it.",
        "Why do cows have hooves instead of feet? Because they lactose!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    return random.choice(jokes)
def get_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still perfectly edible!",
        "A single cloud can weigh more than a million pounds.",
        "Bananas are berries, but strawberries are not!"
    ]
    return random.choice(facts)
def jarvis():
    print("Hello, I am Jarvis. How can I assist you?")
    while True:
        command = input("You: ").lower()
        print("You said:", command)
        if "time" in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Jarvis: The time is {now}")
        elif "date" in command:
            today = datetime.datetime.today().strftime("%Y-%m-%d")
            print(f"Jarvis: Today's date is {today}")
        elif "datetime" in command or "date and time" in command:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Jarvis: The current date and time is {now}")
        elif "open google" in command:
            print("Jarvis: Opening Google")
            webbrowser.open("https://www.google.com")
        elif "open brave" in command:
            print("Jarvis: Opening Brave Browser")
            os.system("start brave")
        elif "search google for" in command:
            query = command.replace("search google for", "").strip()
            print(f"Jarvis: Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "search wikipedia for" in command:
            query = command.replace("search wikipedia for", "").strip()
            print(f"Jarvis: Searching Wikipedia for {query}")
            try:
                summary = wikipedia.summary(query, sentences=2)
                print(f"Jarvis: {summary}")
            except wikipedia.exceptions.DisambiguationError as e:
                print("Jarvis: Multiple results found. Please be more specific.")
            except wikipedia.exceptions.PageError:
                print("Jarvis: No results found.")
        elif "search youtube for" in command:
            query = command.replace("search youtube for", "").strip()
            print(f"Jarvis: Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif "open youtube" in command:
            print("Jarvis: Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "weather" in command:
            print("Jarvis: Checking weather on Google")
            webbrowser.open("https://www.google.com/search?q=weather")
        elif "news" in command:
            get_news()
        elif "joke" in command:
            print(f"Jarvis: {get_joke()}")
        elif "fact" in command:
            print(f"Jarvis: {get_fact()}")
        elif "open calculator" in command or "open cal" in command:
            print("Jarvis: Opening Calculator")
            os.system("calc")
        elif "open notepad" in command:
            print("Jarvis: Opening Notepad")
            os.system("notepad")
        elif "open command prompt" in command or "open cmd" in command:
            print("Jarvis: Opening Command Prompt")
            os.system("cmd")
        elif "shutdown" in command:
            print("Jarvis: Shutting down the system")
            os.system("shutdown /s /t 0")
        elif "restart" in command:
            print("Jarvis: Restarting the system")
            os.system("shutdown /r /t 0")
        elif "log off" in command:
            print("Jarvis: Logging off the system")
            os.system("shutdown /l")
        elif "exit" in command or "stop" in command:
            print("Jarvis: Goodbye!")
            break
        else:
            print("Jarvis: Sorry, I can't do that yet.")
if __name__ == "__main__":
    jarvis()
