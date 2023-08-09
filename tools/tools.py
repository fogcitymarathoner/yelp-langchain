from langchain.utilities import SerpAPIWrapper
from utilities.yelpapi import YelpAPIWrapper

class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
            toret = res["answer_box"]["answer"]
        elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
            toret = res["answer_box"]["snippet"]
        elif (
            "answer_box" in res.keys()
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            toret = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res.keys()
            and "game_spotlight" in res["sports_results"].keys()
        ):
            toret = res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res.keys()
            and "description" in res["knowledge_graph"].keys()
        ):
            toret = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            toret = res["organic_results"][0]["link"].replace('?lang=en', '')

        else:
            toret = "No good search result found"
        return toret


def get_profile_url(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = CustomSerpAPIWrapper()
    res = search.run(f"{name}")
    return res


def get_yelp_business_id(name: str, address1: str, city:str, state: str, country:str):
    """Searches for id of a business."""
    search = YelpAPIWrapper()
    res = search.run(name=f"{name}", address1=f"{address1}", city=f"{city}", state=f"{state}", country=f"{country}")
    return res
