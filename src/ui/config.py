from configparser import ConfigParser

class Config:
    def __init__(self, config_path="./src/ui/config.ini"):
        self.config = ConfigParser()
        self.config.read(config_path)

    def get_page_title(self):
        return self.config["DEFAULT"]["PAGE_TITLE"]

    def get_llm_models(self):
        return self.config["DEFAULT"]["LLM_MODELS"].split(",")

    def get_use_cases(self):
        return self.config["DEFAULT"]["USE_CASES"].split(",")

    def get_groq_models(self):
        return self.config["DEFAULT"]["GROQ_MODELS"].split(",")

    def get_gemini_models(self):
        return self.config["DEFAULT"]["GEMINI_MODELS"].split(",")

    def get_openai_models(self):
        return self.config["DEFAULT"]["OPENAI_MODELS"].split(",")