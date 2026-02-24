# database-for-JOWABOT3.2
it's ```database``` for BOT named JOWABOT3.2 it's Open Source(```MIT```) database by json file

*1-*
# *why we need this database ?*
*beacause to have open source database for Ai or BOT*

*2-*
example for the ```database```:
```json
{
    "Hi": "Hello What are you need ?",
    "whats your name ?": "My name is JOWABOT3.2 , are you need any help ?",
    "How are you ?": "I am fine , thanks for asking",
    "why the bnanna crying ?": "Because it was in peel",
    "what is the meaning of life ?": "The meaning of life is 42",
    "bye": "Goodbye , see you later"
}
```
BOT code with ```github *database* ``` :
```python


```

BOT code with ```host *database* ``` :
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


_by:AXV( *AhmedWalid* )_

