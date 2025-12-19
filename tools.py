class EligibilityTool:
    name = "eligibility"

    def run(self, memory):
        profile = memory.get_profile()

        if "age" not in profile:
            return None

        if profile["age"] < 18:
            return "మీరు ప్రభుత్వ పథకాలకు అర్హులు కాదు."

        return "మీరు ప్రభుత్వ పథకాలకు అర్హులు."


class SchemeTool:
    name = "scheme"

    def run(self, memory):
        return "మీకు రైతు భరోసా పథకం సరిపోతుంది. అప్లై చేయాలా?"
