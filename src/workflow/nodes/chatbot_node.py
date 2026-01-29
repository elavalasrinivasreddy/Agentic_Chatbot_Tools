from src.workflow.states.chatbot_state import Chatbot_state

class Chatbot_node:
    def __init__(self, model):
        self.model = model

    def process(self, state: Chatbot_state):
        """
        This function processes the state of the chatbot.
        """
        return {"messages": self.model.invoke(state['messages'])} 