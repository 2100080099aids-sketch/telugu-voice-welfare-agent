class ConversationMemory:
    def __init__(self):
        self.history = []
        self.profile = {}

    def add_user(self, text):
        self.history.append(("user", text))
        self._extract_profile(text)

    def add_agent(self, text):
        self.history.append(("agent", text))

    def _extract_profile(self, text):
        words = text.split()
        for w in words:
            if w.isdigit():
                self.profile["age"] = int(w)

    def get_profile(self):
        return self.profile