import requests
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzI0OTY0YWUyZGIxYmVlMTNlNTdmOGQ3MWUyZjQ4MiIsIm5iZiI6MTc0MzY5NDEzOC43NTUsInN1YiI6IjY3ZWVhOTNhNDY4MGYyNmJmM2E3YmIyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.djSoWLofNeseWi-7z4ILwigetR0NyQf_FMPXPGStLtQ"
BASIC_URL = "https://api.themoviedb.org/3/movie/"
def call_tmdb_api(endpoint):
    full_url = f"{BASIC_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type="popular"):
    return call_tmdb_api(list_type)

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type="popular"):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    return call_tmdb_api(movie_id)

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"{1}/credits")