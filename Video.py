# video_library_management.py

from typing import List, Dict  # Import used for type annotations, which help with readability and type checking
from datetime import datetime  # Used to get the current year for validation

# Initial movie dataset
video_library: List[Dict] = [
    {"title": "The Godfather", "director": "Francis Ford Coppola", "genre": "Crime", "year": 1972, "quantity": 3, "rental_price": 3.99},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "genre": "Crime", "year": 1994, "quantity": 4, "rental_price": 2.99},
    {"title": "Inception", "director": "Christopher Nolan", "genre": "Sci-Fi", "year": 2010, "quantity": 5, "rental_price": 4.50},
    {"title": "Titanic", "director": "James Cameron", "genre": "Romance", "year": 1997, "quantity": 2, "rental_price": 3.50},
    {"title": "Parasite", "director": "Bong Joon-ho", "genre": "Thriller", "year": 2019, "quantity": 3, "rental_price": 4.25},
]

# Register a new movie
def register_movie(title: str, director: str, genre: str, year: int, quantity: int, rental_price: float):
    current_year = datetime.now().year  # Get current year
    if year > current_year or quantity < 0 or rental_price < 0:  # Validate inputs
        print("Invalid input. Year must not be in the future. Quantity and price must be positive.")
        return
    for movie in video_library:  # Check for duplicates
        if movie['title'].lower() == title.lower():
            print("Movie already exists.")
            return
    # Append new movie to the list
    video_library.append({"title": title, "director": director, "genre": genre, "year": year,
                          "quantity": quantity, "rental_price": rental_price})
    print("Movie registered successfully.")

# Search for a movie by title or director
def search_movie(query: str):
    # Filter results based on title or director match (case-insensitive)
    result = [movie for movie in video_library if query.lower() in movie['title'].lower() or query.lower() in movie['director'].lower()]
    return result if result else None

# Update movie info
def update_movie(title: str, quantity: int = None, rental_price: float = None):
    for movie in video_library:
        if movie['title'].lower() == title.lower():  # Find the movie
            if quantity is not None and quantity >= 0:  # Validate and update quantity
                movie['quantity'] = quantity
            if rental_price is not None and rental_price >= 0:  # Validate and update price
                movie['rental_price'] = rental_price
            print("Movie updated successfully.")
            return
    print("Movie not found.")

# Delete a movie by title
def delete_movie(title: str):
    confirm = input("Are you sure you want to delete this movie? (yes/no): ")  # Confirm deletion
    if confirm.lower() != "yes":
        print("Deletion cancelled.")
        return
    global video_library
    # Reassign the list excluding the movie
    video_library = [movie for movie in video_library if movie['title'].lower() != title.lower()]
    print("Movie deleted if it existed.")

# Generate reports
def generate_reports():
    # Calculate total inventory value
    total_value = sum(movie['quantity'] * movie['rental_price'] for movie in video_library)
    print(f"Total inventory value: ${total_value:.2f}")

    # Get distinct genres
    genres = set(movie['genre'] for movie in video_library)
    for genre in genres:
        # Filter movies by genre
        genre_movies = [m for m in video_library if m['genre'] == genre]
        # Find oldest and newest movies in that genre
        oldest = min(genre_movies, key=lambda x: x['year'])
        newest = max(genre_movies, key=lambda x: x['year'])
        print(f"\nGenre: {genre}")
        print(f"Oldest: {oldest['title']} ({oldest['year']})")
        print(f"Newest: {newest['title']} ({newest['year']})")

# Optional: Interactive Menu
def menu():
    while True:
        print("\nVideo Library Management")
        print("1. Register movie")
        print("2. Search movie")
        print("3. Update movie")
        print("4. Delete movie")
        print("5. Generate reports")
        print("6. Exit")

        option = input("Choose an option: ")

        if option == "1":
            # Get movie details from user
            t = input("Title: ")
            d = input("Director: ")
            g = input("Genre: ")
            y = int(input("Year: "))
            q = int(input("Quantity: "))
            p = float(input("Rental Price: "))
            register_movie(t, d, g, y, q, p)
        elif option == "2":
            # Search functionality
            q = input("Enter title or director: ")
            result = search_movie(q)
            if result:
                for m in result:
                    print(m)
            else:
                print("Movie not found. Would you like to register it?")
        elif option == "3":
            # Update movie
            t = input("Title to update: ")
            q = int(input("New quantity (-1 to skip): "))
            p = float(input("New rental price (-1 to skip): "))
            update_movie(t, q if q >= 0 else None, p if p >= 0 else None)
        elif option == "4":
            # Delete movie
            t = input("Title to delete: ")
            delete_movie(t)
        elif option == "5":
            # Report generation
            generate_reports()
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

# Run the menu if script is executed directly
if __name__ == "__main__":
    menu()
