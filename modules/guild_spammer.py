import random
from .utils import send_message

class GuildSpammer:
    def __init__(self, tokens):
        self.tokens = tokens
    
    def spam(self, channel_id, message, amount=1):
        for i in range(amount):
            token = random.choice(self.tokens)
            send_message(token, channel_id, message, "Guild")