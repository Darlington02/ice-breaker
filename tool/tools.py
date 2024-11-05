from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """searches for LinkedIn or Twitter profile page"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res