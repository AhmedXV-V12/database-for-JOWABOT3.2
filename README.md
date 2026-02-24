# database-for-JOWABOT3.2
it's ```database``` for BOT named JOWABOT3.2 it's Open Source(```MIT```) database by json file

#1-#
# *why we need this database ?*
*to provide to have open source database for Ai or BOT*

##2-
example for the ```database```:
```json
{
    "Hi": "Hello What are you need ?",
    "whats your name ?": "My name is JOWABOT3.2 , Do you need any help?",
    "How are you ?": "I am fine , thanks for asking",
    "why the bnanna crying ?": "Because it was in peel",
    "what is the meaning of life ?": "The meaning of life is 42",
    "bye": "Goodbye , see you later"
}

```
##3-
BOT code with ```github *database* ``` for "./jowabot_internet_db.py" :
```python
# it's JOWABOT3.2
import os
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

```

BOT code with ```host *database* ``` "./jowabot_host_db.py" :
```python
# it's JOWABOT3.2

class Database:
    def __init__(self):
        self.data = {
            "Hi" : "Hello What are you need ?",                                       #_____________________________________
            "whats your name ?" : "My name is JOWABOT3.2 , are you need any help ?",  #       database for the bot          |
            "How are you ?" : "I am fine , thanks for asking",                        #_____________________________________|
            "why the bnanna crying ?" : "Because it was in peel",  # Bad joke :D
            "what is the meaning of life ?" : "The meaning of life is 42", # Another bad joke :D
            "bye" : "Goodbye , see you later"
        }
        
    def training(self, question, answer):
        self.data[question] = answer
        print("Training completed successfully")
        
    def get_answer(self, question):
        return self.data.get(question, "Sorry, I don't understand that question.")
    
    
    def answer_question(self, question):
        answer = self.get_answer(question)
        print("jowaBOT:",answer)
        
        
class JOWABOT:
    def __init__(self):
        self.database = Database()
        
    def ask_question(self, question):
        self.database.answer_question(question)
        
    def train_bot(self, question, answer):
        self.database.training(question, answer)
        
        
if __name__ == "__main__":
    bot = JOWABOT()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break
        elif user_input.lower().startswith("train:"):
            try:
                _, question, answer = user_input.split(":", 2)
                bot.train_bot(question.strip(), answer.strip())
            except ValueError:
                print("Invalid training format. Use: train: question : answer")
        else:
            bot.ask_question(user_input)

```
##4-
#Installation
#1.
_install raw file jowabot_internet_db.py_
#2.
_in Terminal write:_
```bash
pip install requests
```
_in Debian/Ubuntu:_
```bash
pip install --break-system-packages requests
```

```AXV have :*12*_years_old_ ```
__by:AXV( *AhmedWalid* )__
