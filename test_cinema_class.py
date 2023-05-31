import unittest
from datetime import datetime
from cinema import Cinema


class CinemaTest(unittest.TestCase):
    def setUp(self):
        self.cinema = Cinema()

    def test_add_movie(self):
        self.cinema.add_movie("Movie 1", "1234", "2023-06-01 10:00", 100, 12, 10.99)
        self.assertEqual(len(self.cinema.movies), 1)
        self.assertEqual(self.cinema.movies[0]["movie_name"], "Movie 1")
        self.assertEqual(self.cinema.movies[0]["special_code"], "1234")

    def test_load_movies_from_json(self):
        self.cinema.load_movies_from_json("movies.json")
        self.assertEqual(len(self.cinema.movies), 2)
        self.assertEqual(self.cinema.movies[0]["movie_name"], "Movie 1")
        self.assertEqual(self.cinema.movies[1]["movie_name"], "Movie 2")

    def test_make_changes(self):
        self.cinema.add_movie("Movie 1", "1234", "2023-06-01 10:00", 100, 12, 10.99)
        changes = {"price": 12.99, "theater": "Theater 1"}
        self.cinema.make_changes("1234", changes)
        self.assertEqual(self.cinema.movies[0]["price"], 12.99)
        self.assertEqual(self.cinema.movies[0]["theater"], "Theater 1")

    def test_delete_movie(self):
        self.cinema.load_movies_from_json("movies.json")
        self.cinema.delete_movie("5678")
        self.assertEqual(len(self.cinema.movies), 1)
        self.assertEqual(self.cinema.movies[0]["movie_name"], "Movie 1")

    def test_reserve_movie(self):
        self.cinema.add_movie("Movie 1", "1234", "2023-06-01 10:00", 100, 12, 10.99)
        reservation_status = self.cinema.reserve_movie("1234", 15)
        self.assertTrue(reservation_status)
        self.assertEqual(self.cinema.movies[0]["capacity"], 99)
        self.assertEqual(len(self.cinema.reservations), 1)
        self.assertEqual(self.cinema.reservations[0]["movie_name"], "Movie 1")

    def test_delete_reservation(self):
        self.cinema.add_movie("Movie 1", "1234", "2023-06-01 10:00", 100, 12, 10.99)
        self.cinema.reserve_movie("1234", 15)
        self.cinema.delete_reservation("1234")
        self.assertEqual(len(self.cinema.reservations), 0)
        self.assertEqual(self.cinema.movies[0]["capacity"], 100)

    def test_return_price(self):
        self.cinema.load_movies_from_json("movies.json")
        price = self.cinema.return_price("5678")
        self.assertEqual(price, 8.99)

    def test_show_movies(self):
        self.cinema.load_movies_from_json("movies.json")


if __name__ == "__main__":
    unittest.main()
