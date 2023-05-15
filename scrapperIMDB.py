from bs4 import BeautifulSoup
import requests
import openpyxl

# Extract movie rating information from imdb
try:
    source = requests.get("https://www.imdb.com/chart/top/")
    #check if url is valid
    source.raise_for_status() 
    
    soup = BeautifulSoup(source.text, "html.parser")
    # Find all 'tr' tags within the 'tbody' tag and store it in a list
    movies = soup.find('tbody', class_="lister-list").find_all("tr")
    # print (len(movies))

    # Loop through all the movies in the movies array
    for movie in movies:
        # Find the movie title for every movie
        movie_name = movie.find("td", class_="titleColumn").find("a").text
        
        # Find rank of movie
        movie_rank = movie.find("td", class_="titleColumn").get_text(strip=True).split('.')[0]
        # Find movie year
        movie_year = movie.find("td", class_="titleColumn").find("span").text.strip("()")
        # Find movie rating
        movie_rating = movie.find("td", class_="ratingColumn").find("strong").text
        print(movie_rank, movie_name, movie_year, movie_rating)
except Exception as e:
    print(e)
