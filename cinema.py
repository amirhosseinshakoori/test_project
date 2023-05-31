import json
from datetime import datetime
import logging


logging.basicConfig(filename='cinematicket.log', level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s')

class Cinema:
    def __init__(self):
        self.movies = []
        self.reservations = []

    def add_movie(self, movie_name: str, special_code: str, date_time: str, capacity: int, age_group: int, price: float,
                  genre: str = None, theater: str = None) -> None:
        """
        Add a movie to the list of movies.

        Args:
            movie_name (str): The name of the movie.
            special_code (str): The unique special code for the movie.
            date_time (str): The date and time of the movie in the format "YYYY-MM-DD HH:MM".
            capacity (int): The capacity of the movie.
            age_group (int): The minimum age requirement for the movie.
            price (float): The price of the movie.
            genre (str, optional): The genre of the movie. Defaults to None.
            theater (str, optional): The theater where the movie is screened. Defaults to None.

        Returns:
            None
        """
        movie = {
            "movie_name": movie_name,
            "special_code": special_code,
            "date_time": date_time,
            "capacity": capacity,
            "age_group": age_group,
            "price": price,
            "genre": genre,
            "theater": theater
        }
        self.movies.append(movie)
        self._update_movie_json()
        logging.info(f'add {movie_name} ' )
        return True

    def _update_movie_json(self) -> None:
        """
        Update the JSON file with the list of movies.

        Returns:
            None
        """
        with open("movies.json", "w") as file:
            json.dump(self.movies, file)

    def load_movies_from_json(self, json_file: str) -> None:
        """
        Load movies from a JSON file.

        Args:
            json_file (str): The path to the JSON file containing the movies.

        Returns:
            None
        """
        with open(json_file, "r") as file:
            self.movies = json.load(file)
        logging.info(f'load movies ' )

    def make_changes(self, special_code: str, changes: dict) -> bool:
        """
        Make changes to a movie and update the JSON file.

        Args:
            special_code (str): The special code of the movie to be changed.
            changes (dict): The dictionary containing the changes to be applied.

        Returns:
            bool: True if the movie was found and changes were applied, False otherwise.
        """
        for movie in self.movies:
            if movie["special_code"] == special_code:
                movie.update(changes)
                self._update_movie_json()
                logging.info(f'change movies {changes}' )
                return True
        return False

    def delete_movie(self, special_code: str) -> bool:
        """
        Delete a movie from the list of movies and update the JSON file.

        Args:
            special_code (str): The special code of the movie to be deleted.

        Returns:
            bool: True if the movie was found and deleted, False otherwise.
        """
        for movie in self.movies:
            if movie["special_code"] == special_code:
                self.movies.remove(movie)
                self._update_movie_json()
                logging.info(f'remove movies {movie}' )
                return True
        return False

    def reserve_movie(self, special_code: str, user_age: int) -> str:
        """
        Reserve a movie for the user.

        Args:
            special_code (str): The special code of the movie to be reserved.
            user_age (int): The age of the user.

        Returns:
            str: A message indicating the status of the reservation.
        """
        i = 0
        current_time = datetime.now()
        for movie in self.movies:
            if movie["special_code"] == special_code:
                i = 1
                movie_date_time = datetime.strptime(movie["date_time"], "%Y-%m-%d %H:%M")
                if current_time > movie_date_time:
                    print("Sorry, the movie has already started.")
                    logging.info(f'the movie has already starte')
                    return False
                elif movie["capacity"] <= 0:
                    print("Sorry, the movie is already sold out.")
                    logging.info(f'the movie is already sold out')
                    return False
                elif user_age < movie["age_group"]:
                    print("Sorry, this movie is not suitable for your age.")
                    logging.info(f' movie is not suitable for your age')
                    return False
                else:
                    movie["capacity"] -= 1
                    self._update_movie_json()
                    self._add_reservation(movie["movie_name"], special_code)
                    logging.info(f'reserve movies {movie}' )
                    return True
                    break
        if i ==0:
            print("film not find")  
            return False      
           


    def _add_reservation(self, movie_name: str, special_code: str) -> None:
        """
        Add a reservation to the list of reservations.

        Args:
            movie_name (str): The name of the reserved movie.
            special_code (str): The special code of the reserved movie.

        Returns:
            None
        """
        reservation = {
            "movie_name": movie_name,
            "special_code": special_code
        }
        self.reservations.append(reservation)
        self._update_reservation_json()

    def _update_reservation_json(self) -> None:
        """
        Update the JSON file with the list of reservations.

        Returns:
            None
        """
        with open("reservations.json", "w") as file:
            json.dump(self.reservations, file)

    def delete_reservation(self, special_code: str) -> bool:
        """
        Delete a reservation from the list of reservations.

        Args:
            special_code (str): The special code of the reservation to be deleted.

        Returns:
            bool: True if the reservation was found and deleted, False otherwise.
        """
        for reservation in self.reservations:
            if reservation["special_code"] == special_code:
                self.reservations.remove(reservation)
                self._update_reservation_json()
                self._return_capacity(special_code)
                logging.info(f' remove movie reserve {special_code}' )
                return True
        return False

    def _return_capacity(self, special_code: str) -> None:
        """
        Increase the capacity of a movie when a reservation is deleted.

        Args:
            special_code (str): The special code of the movie.

        Returns:
            None
        """
        for movie in self.movies:
            if movie["special_code"] == special_code:
                movie["capacity"] += 1
                logging.info(f'  movie capacity add {special_code}' )
                self._update_movie_json()
                break
    
    def return_price(self, special_code):

        for movie in self.movies:
            if movie["special_code"] == special_code:
               logging.info(f' price of movie reterned {special_code}' )
               return  movie["price"]
               break

    def show_movies(self) -> None:
        """
        Display all the movies with their features.

        Returns:
            None
        """
        with open("movies.json", "r") as file:
            self.movies = json.load(file)
            logging.info(f'load movies ' )
        for movie in self.movies:
            movie_name = movie.get("movie_name", "N/A")
            special_code = movie.get("special_code", "N/A")
            date_time = movie.get("date_time", "N/A")
            capacity = movie.get("capacity", "N/A")
            age_group = movie.get("age_group", "N/A")
            price = movie.get("price", "N/A")
            genre = movie.get("genre", "N/A")
            theater = movie.get("theater", "N/A")

            print(f"Movie Name: {movie_name}")
            print(f"Special Code: {special_code}")
            print(f"Date and Time: {date_time}")
            print(f"Capacity: {capacity}")
            print(f"Age Group: {age_group}")
            print(f"Price: {price}")
            print(f"Genre: {genre}")
            print(f"Theater: {theater}")
            print("------------------------------------")


