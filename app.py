from agent import WelfareAgent
from tools import EligibilityTool, SchemeTool
from memory import ConversationMemory
from voice import stt_whisper, tts_telugu

print("Telugu Welfare Agent Started...")

memory = ConversationMemory()

agent = WelfareAgent(
    language="te",
    tools=[EligibilityTool(), SchemeTool()],
    memory=memory
)

# Use recorded audio file
audio_file = "input.wav"

user_text = stt_whisper(audio_file)
print("USER SAID:", user_text)

agent_reply = agent.run(user_text)
print("AGENT REPLY:", agent_reply)

output_audio = tts_telugu(agent_reply)
print("SPOKEN OUTPUT SAVED AS:", output_audio)