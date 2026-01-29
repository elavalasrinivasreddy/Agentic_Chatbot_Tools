from src.workflow.llms.openai import OpenAI
from src.workflow.llms.groq import Groq
from src.workflow.llms.gemini import Gemini

class LLM_with_tools:
    def __init__(self, user_selections):
        self.user_selections = user_selections

    def get_model_with_tools(self, tools):
        try:
            if self.user_selections["llm"] == "openai":
                model = OpenAI(self.user_selections).get_model()
            elif self.user_selections["llm"] == "groq":
                model = Groq(self.user_selections).get_model()
            elif self.user_selections["llm"] == "gemini":
                model = Gemini(self.user_selections).get_model()
            
            # Bind the model with tools
            return model.bind_tools(tools)
        except Exception as e:
            raise ValueError(f"Error loading LLM with tools {e}")
