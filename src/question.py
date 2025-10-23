class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer
    def check_answer(self, user_answer):
        return user_answer.strip().upper() == self.answer.upper()