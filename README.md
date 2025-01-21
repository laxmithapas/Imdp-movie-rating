# Movie Rating Fetcher

This Python script allows you to search for movies and fetch detailed information about them using the OMDb API.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script to your local machine.
2. Install the `requests` library if you haven't already:

    ```sh
    pip install requests
    ```

## Usage

1. Replace `'your_api_key_here'` with your actual OMDb API key in the [main](http://_vscodecontentref_/0) function of [rating.py](http://_vscodecontentref_/1):

    ```python
    api_key = "your_api_key_here"  # Replace 'your_api_key_here' with your actual OMDb API key
    ```

2. Run the script:

    ```sh
    python rating.py
    ```

3. Follow the on-screen prompts to search for a movie or exit the program.

## Example

```sh
Menu:
1. Search for a movie
2. Exit
Enter your choice: 1
Enter the name of the movie: Inception

Search Results:
1. Inception (2010) - Movie

Enter the number of the movie to see details (or press Enter to skip): 1

Movie Details:
Title: Inception
Year: 2010
Rated: PG-13
Released: 16 Jul 2010
Runtime: 148 min
Genre: Action, Adventure, Sci-Fi
Director: Christopher Nolan
Writer: Christopher Nolan
Actors: Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page
Plot: A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.
Language: English, Japanese, French
Country: USA, UK
Awards: Won 4 Oscars. Another 152 wins & 204 nominations.
IMDB Rating: 8.8
IMDB Votes: 2,074,598
Type: movie
DVD: 07 Dec 2010
BoxOffice: $292,576,195
Production: Warner Bros. Pictures
Website: N/A
