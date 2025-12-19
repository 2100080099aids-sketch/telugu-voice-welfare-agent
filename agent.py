class WelfareAgent:
    def __init__(self, language, tools, memory):
        self.language = language
        self.tools = {tool.name: tool for tool in tools}
        self.memory = memory

    def run(self, user_text):
        self.memory.add_user(user_text)

        plan = self.plan(user_text)
        result = self.execute(plan)
        response = self.evaluate(result)

        self.memory.add_agent(response)
        return response
    def plan(self, text):
        if "వయస్సు" in text or "సంవత్సరాలు" in text:
            return "ELIGIBILITY"

        if "పథకం" in text or "అప్లై" in text:
            return "ELIGIBILITY"

        return "SCHEME"

    def execute(self, plan):
        if plan == "ELIGIBILITY":
            return self.tools["eligibility"].run(self.memory)

        return self.tools["scheme"].run(self.memory)

    def evaluate(self, result):
        if result is None:
            return "మీ వివరాలు పూర్తి కావాలి. దయచేసి మీ వయస్సు చెప్పండి."

        return result

