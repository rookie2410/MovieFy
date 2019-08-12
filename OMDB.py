import requests
import json

def getRating(movieTitle):
    url = 'http://www.omdbapi.com'
    data = {'apikey':'34af84e4','t':movieTitle}
    response = requests.get(url,data)
    return str(response.json().get("imdbRating"))
    

if __name__=='__main__':
    print()