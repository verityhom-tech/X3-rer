class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"I will help you {self.work}, Agferwards I will help you with {work}"

kl = Helper("homework")
print(kl("cleaning"))