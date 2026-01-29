from langchain_tavily import TavilySearch

def get_tools():
    """
    Returns the list of tools for the chatbot.
    """
    tools = [TavilySearch(max_results=2)]
    return tools

    