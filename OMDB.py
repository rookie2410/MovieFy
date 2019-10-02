import os
import requests

def getRating(movieTitle):
    url = 'http://www.omdbapi.com'
    api_key = os.getenv('APIKEY')
    data = {'apikey':api_key,'t':movieTitle}
    response = requests.get(url,data)
    imdb_rating = response.json().get("imdbRating")
    return imdb_rating
    