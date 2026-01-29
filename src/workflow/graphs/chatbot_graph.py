from langgraph.graph import StateGraph, START, END
from src.workflow.states.chatbot_state import Chatbot_state
from src.workflow.nodes.chatbot_node import Chatbot_node


class Chatbot_graph:
    """
    This class is used to build the chatbot graph.
    """
    def __init__(self, model):
        self.model = model
        self.graph = StateGraph(Chatbot_state)

    def build_graph(self):
        """
        This function builds the chatbot graph.
        """
        self.chatbot_node = Chatbot_node(self.model)
        self.graph.add_node("chatbot", self.chatbot_node.process)
        self.graph.add_edge(START, "chatbot")
        self.graph.add_edge("chatbot", END)
        return self.graph.compile()