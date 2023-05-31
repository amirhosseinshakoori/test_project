
import os
import json
from human import User 
import getpass
from datetime import datetime, timedelta
from cinema import Cinema
from bank import BankAccount 


def main():
        while True:
            print("Welcome to our comprehensive internet service system")
            print("\n")
            print("1. Cinema")
            print("2. bank")
            print("0. Exit")
            choices = input("Enter your choice: ")

            if choices == "1":
                print("Welcome to the Movie Booking System!")
                print("\nChoose an option:")
                print("1. Login")
                print("2. Register")
                print("0. Exit")

                choice = input("Enter your choice: ")
                if choice == "0":
                     break
                elif choice == "1":
                    os.system("clear")
                        #os.system("cls")
                    print("Please enter your username and password to enter the cinema  Booking system")
                    username = input("Enter your username: ")
                    password = getpass.getpass("Please enter your password: ")
                    user = User.login_user(username,password)
                    if user:
                        os.system("clear")
                        #os.system("cls")
                        while True:
                            choice1 = input(
                            "Enter your choice:\n"
                            "1. View profile\n"
                            "2. Edit personal information\n"
                            "3. Change password\n"
                            "4. View and booking sessions\n"
                            "5. Charge wallet \n"
                            "6. Subscription upgrade \n"
                            "0. Exit\n")
                            if choice1 == '1':
                                print(user)
                                break
                            elif choice1 == '2':
                                new_username = input("Enter new username (press enter to skip): ")
                                new_phone_number = input("Enter new phone number (pressenter to skip): ")
                                new_birthdate = input("Enter new birthdate (press enter to skip): ")

                                User.edit_personal_info(user,new_username,new_phone_number,new_birthdate)
                                break

                            elif choice1 == '3':
                                      os.system("clear")
                                     #os.system("cls")
                                      old_password = getpass.getpass("Enter your current password: ")
                                      new_password = getpass("Enter a new password: ")
                                      confirm_new_password = getpass("Confirm your new password: ")
                                      if new_password != confirm_new_password:
                                        print("New passwords do not match")
                                        break
                                      elif User.change_password(old_password,new_password):
                                           print("Password changed successfully")
                                           break
                                      else:
                                           print("Incorrect password")
                                           break
                            elif choice1 == '4':
                                  os.system("clear")
                                  #os.system("cls")
                                  print("\nAvailable sessions:")
                                  cinema = Cinema()
                                  Cinema.show_movies(cinema)
                                  special_code = input("Enter special_code: ")
                                  today = datetime.today()
                                  birth_date = datetime.strptime(user.birth_date, "%Y-%m-%d")
                                  age =today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                                  price = Cinema.return_price(cinema,special_code)*(1-User.apply_discount(user.birth_date,user.registration_date))
                                  if  price <= user.balance:
                                    print("Your account balance is insufficient")
                                    break
                                  elif   Cinema.reserve_movie(special_code,age):
                                       user.balenc -= price
                                       print("Booking successful!")
                                       
                                       if user.subscription == "Gold" and user.Expiration < datetime.today()  :
                                            print("Grab your energy drink")
                                            user.balenc += price*0.5
                                       elif user.subscription == "Silver" and user.Expiration > 0:
                                            user.balenc += price*0.2
                                            user.Expiration -=1
                                       break
                            elif choice1 == '5':
                                os.system("clear")
                                  #os.system("cls")
                                card_number = input("card_number: ")
                                cvv = input("cvv: ")
                                amount = float(input("Enter the desired amount: "))
                                password = getpass.getpass("Password: ")
                                try:
                                    user.balenc += BankAccount.charge_wallet(card_number,cvv,password,amount)
                                    break
                                except ValueError:
                                    print("The operation was not possible. Please check your account")
                                    break
                                
                            
                            elif choice1 == '6':
                                 while True:
                                    os.system("clear")
                                        #os.system("cls")
                                    choice = input(
                                    "Enter your subscription:\n"
                                    "1. Gold\n"
                                    "2. Silver\n"
                                    "0. Exit\n")
                                    if choice == 1:
                                        
                                        if user.balenc > 20.0:
                                            print("Your subscription has been changed to gold")
                                            user.subscription = "Gold"
                                            user.balenc -= 20.0
                                            user.Expiration = datetime.today() + timedelta(days=3*30)
                                            break
                                        else:
                                          print("Account upgrade was not successful")
                                          break
                                    elif choice == 2:
                                        if user.balenc > 10.0:
                                             user.subscription = "Silver"
                                             user.balenc -= 10.0
                                             user.Expiration =3
                                             break
                                              
                                        else:
                                            print("Account upgrade was not successful")
                                            break
                                    elif choice == '0':
                                        break
                                    else:
                                        print("Invalid choice, please enter a number between 0 and 2.")
                                              

                            elif choice1 == '0':
                                 break
                            else:
                                print("Invalid choice, please enter a number between 0 and 5.")
                         
                    else:
                         print("Check your account information, login failed")     
                         break
                elif choice == "2":
                    os.system("clear")
                    #os.system("cls")
                    while True:
                        print("Welcome to the Movie Booking System!")
                        print("\nPlease enter your details:")
                        name = input("Name: ")
                        dob = input("Date of birth (YYYY-MM-DD): ")
                        phone = input("Phone number: ")
                        password1 = getpass.getpass("Password: ")
                        user1 = User(name,phone,password1,dob)
                        if User.register_user(user1):
                         print("Registration successful!")
                         break
                        else:
                            print("Registration failed. Please try again.")
                            break

            elif choices == "2":  
                    
                     os.system("clear")
                     #os.system("cls")  
                     print("Welcome to the  Bank System!")
                     
                     name = input("Name: ")
                     balance = int(input("Enter the initial amount of your bank account: "))

                     password = getpass.getpass("Password: ")
                     password2 =getpass.getpass("Confirm your  password: ")
                     acuunt= BankAccount(name,balance,)
                     if BankAccount.set_password(acuunt):
                        print("Your account has been successfully opened\n"
                                "Your account information is as follows:"
                                )
                        print(f"card numberis {BankAccount.acuunt.card},cvv is {BankAccount.acuut.cvv}")
                        break
                     else:
                          print("try again")
                          break
            
            elif choices =="0":
                print("Exit")
                break

if __name__ == "__main__":
    main()
                  