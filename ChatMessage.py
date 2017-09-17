from datetime import datetime

class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time= datetime.now()
        self.sent_by_me = sent_by_me