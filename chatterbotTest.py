from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
chatbot = ChatBot("Ron Obvious")

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)


response = chatbot.get_response("Good morning!")
print(response)
