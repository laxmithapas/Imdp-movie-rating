import requests

def fetch_movie_data(api_key, **params):
    base_url = "http://www.omdbapi.com/"
    params["apikey"] = api_key
    response = requests.get(base_url, params=params)
    return response.json()

def display_movie_details(movie_data):
    print("\nMovie Details:")
    print(f"Title: {movie_data.get('Title')}")
    print(f"Year: {movie_data.get('Year')}")
    print(f"Rated: {movie_data.get('Rated')}")
    print(f"Released: {movie_data.get('Released')}")
    print(f"Runtime: {movie_data.get('Runtime')}")
    print(f"Genre: {movie_data.get('Genre')}")
    print(f"Director: {movie_data.get('Director')}")
    print(f"Writer: {movie_data.get('Writer')}")
    print(f"Actors: {movie_data.get('Actors')}")
    print(f"Plot: {movie_data.get('Plot')}")
    print(f"Language: {movie_data.get('Language')}")
    print(f"Country: {movie_data.get('Country')}")
    print(f"Awards: {movie_data.get('Awards')}")
    print(f"IMDB Rating: {movie_data.get('imdbRating')}")
    print(f"IMDB Votes: {movie_data.get('imdbVotes')}")
    print(f"Type: {movie_data.get('Type')}")
    print(f"DVD: {movie_data.get('DVD')}")
    print(f"BoxOffice: {movie_data.get('BoxOffice')}")
    print(f"Production: {movie_data.get('Production')}")
    print(f"Website: {movie_data.get('Website')}")

def main():
    api_key = "923f9792"  # Replace 'your_api_key_here' with your actual OMDb API key

    while True:
        print("\nMenu:")
        print("1. Search for a movie")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            movie_name = input("Enter the name of the movie: ").strip()
            movie_data = fetch_movie_data(api_key, s=movie_name)

            if "Error" in movie_data:
                print(f"Error: {movie_data.get('Error', 'No movies found.')}")
            else:
                print("\nSearch Results:")
                for i, movie in enumerate(movie_data.get("Search", []), start=1):
                    print(f"{i}. {movie.get('Title')} ({movie.get('Year')}) - {movie.get('Type').capitalize()}")

                # Allow user to pick a movie for more details
                choice = input("\nEnter the number of the movie to see details (or press Enter to skip): ").strip()
                if choice.isdigit() and 1 <= int(choice) <= len(movie_data["Search"]):
                    selected_movie = movie_data["Search"][int(choice) - 1]
                    detailed_data = fetch_movie_data(api_key, i=selected_movie.get("imdbID"))

                    if "Error" in detailed_data:
                        print(f"Error: {detailed_data['Error']}")
                    else:
                        display_movie_details(detailed_data)

        elif choice == "2":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()