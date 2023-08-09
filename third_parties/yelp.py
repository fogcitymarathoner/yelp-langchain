import os
from yelpapi import YelpAPI

from dotenv import load_dotenv

load_dotenv()


def scrape_yelp_profile(yelp_profile_id: int):
    """scrape information from yelp profiles,
    Manually scrape the information from the yelp profile
    """

    search = YelpAPI(os.environ.get("YELP_API_KEY")
)
    response = search.business_query(id=yelp_profile_id)
    return response
