import os
from human import User, Manager
import getpass
from datetime import datetime, timedelta
from cinema import Cinema


def main():
    while True:
        choes= input(
                "1. Login\n"
                "2. Register\n"
                "0. Exit\n"
                "Choose an option:"
        )
        
        
        if choes == "1": 
        
            print("Please enter your username and password to enter the cinema management system")

            username = input("Enter your username: ")
            password = getpass.getpass("Please enter your password: ")

            if Manager.login_admin(username, password):
                os.system("clear")
                # os.system("cls")
                print("Welcome, Manager!")
                while True:
                  print("\nChoose an option:")
                  print("1. Create a session")
                  print("2. Update session details")
                  print("3. Delete a session")
                  print("4. Delete a user")
                  print("0. Exit")

                  choice = input("Enter your choice: ")

                  if choice == "1":
                        os.system("clear")
                        # os.system("cls")
                        print("\nPlease enter session details:")
                        movie_name = input("Movie name: ")
                        special_code = input("special_code: ")
                        date_time = input("date_time (YYYY-MM-DD): ")
                        capacity = int(input("capacity: "))
                        age_group = int(input("age_group: "))
                        price = float(input("Price: "))
                        genre = input("genre: ")
                        theater = input("theater: ")
                        cinema =Cinema ()
                        if Cinema.add_movie(cinema,movie_name, special_code, date_time, capacity, age_group, price,genre, theater):
                            print("Session created.")
                        else:
                          print("Session creation failed. Please try again.")

                  elif choice == "2":
                        os.system("clear")
                        # os.system("cls")
                        cinema = Cinema()
                        Cinema.show_movies(cinema)
                        special_code = input("Enter special_code: ")
                        movie_name = input("New movie name: ")
                        date_time = input("New date_time (YYYY-MM-DD): ")
                        age_group = int(input("age_group: "))
                        capacity = int(input("New capacity: "))
                        price = float(input("New price: "))
                        genre = input("New genre: ")
                        theater = input("New theater: ")

                        changes = {
                        "movie_name": movie_name,
                        "special_code": special_code,
                        "date_time": date_time,
                        "capacity": capacity,
                        "age_group": age_group,
                        "price": price,
                        "genre": genre,
                        "theater": theater
                        }
                        cinema = Cinema()
                        if Cinema.make_changes(cinema,special_code, changes):
                         print("Changes applied successfully")
                        else:
                         print("Changes edeletion failed. Pleasecontinue to try again.")

                  elif choice == "3":
                         os.system("clear")
                         # os.system("cls")
                         special_code = input(" special_code: ")
                         cinema = Cinema()
                         if Cinema.delete_movie(cinema,special_code):
                             print("Session deleted.")
                         else:
                            print("Session deletion failed. Please try again.")

                  elif choice == "4":
                        os.system("clear")
                        # os.system("cls")
                        user_id = input("Enter user ID: ")
                        user = User(user_id)

                        if user.delete_user(user_id):
                          print("User deleted.")
                        else:
                             print("User deletion failed. Please try again.")

                  elif choice == "0":
                        print("Goodbye, Manager!")
                        break
                  else:
                        print("Invalid choice. Please try again.")
        if choes == "2":
            name = input("Enter your username: ")
            phone_number = input("Enter your phon: ")
            password1 = getpass.getpass("Please enter your password: ")

            admin1 = Manager(name,phone_number,password1)
            if Manager.register_admin(admin1):
                print("new admin is ready")
            else:
                print("eror")

if __name__ == "__main__":
    main()