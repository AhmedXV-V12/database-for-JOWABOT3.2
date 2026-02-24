# it's JOWABOT3.2
import os

# if os.system("pip install requests") != 0:
#     os.system("pip install --break-system-packages requests")
    

import requests
import json

class Database:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_remote_data()
            
    def training(self, question, answer):
        self.data[question] = answer
        print("Training completed in memory.")
        
    def fetch_remote_data(self):
            try:
                response = requests.get(self.url)
                if response.status_code == 200:
                    raw_data = response.json()
                    return {k.lower(): v for k, v in raw_data.items()}
                return {}
            except:
                return {}

    def get_answer(self, question):
        query = question.strip().lower()
        return self.data.get(query, "Sorry, I don't understand.")
    def answer_question(self, question):
        answer = self.get_answer(question)
        print("jowaBOT:", answer)
            
class JOWABOT:
    def __init__(self, url): 
        self.database = Database(url)
    def ask_question(self, question):
        self.database.answer_question(question)
        
    def train_bot(self, question, answer):
        self.database.training(question, answer)
        
if __name__ == "__main__":
    bot = JOWABOT(url="https://raw.githubusercontent.com/AhmedXV-V12/database-for-JOWABOT3.2/main/database.json")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break
        elif user_input.lower().startswith("train:"):
            try:
                parts = user_input.split(":", 2)
                if len(parts) == 3:
                    _, question, answer = parts
                    bot.train_bot(question.strip(), answer.strip())
                else:
                    raise ValueError
            except ValueError:
                print("Invalid training format. Use: train: question : answer")
        else:
            bot.ask_question(user_input)
