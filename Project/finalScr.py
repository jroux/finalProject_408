#Jessica Roux
#Student ID: 2317255
#Chapman Email: jroux@chapman.edu
#Course: 408-01
#Final Assignment


#Imports
import mysql.connector
from faker import Faker
import csv
import random as rand
import pandas as pd
from pandas import DataFrame


#Connection to database
db = mysql.connector.connect(
    host="34.94.182.22",
    user="jroux@chapman.edu",
    passwd="FooBar!@#$",
    database="jroux_db"
)

mycursor = db.cursor()


#Function that displays menu for user to pick from
def menu():
    while True:
        print("\n")
        print("Below are your options: ")
        print("-------------------------------------------------------------------------------------------")
        print("1) Display all tables in database")
        print("2) Create a new player")
        print("3) Delete from a table")
        print("4) Update data")
        print("5) Query for data")
        print("6) Generate reports")
        print("7) Exit program")
        print("\n")
        menuInput = input("Please select which option you would like to execute. Enter the corresponding digit: ")
        if menuInput == "1":
            print("\n")
            displayTables()
            continue
        elif menuInput == "2":
            print("\n")
            createNewRecord()
            continue
        elif menuInput == "3":
            print("\n")
            deleteRecord()
            continue
        elif menuInput == "4":
            print("\n")
            updateRecord()
            continue
        elif menuInput == "5":
            print("\n")
            queryData()
            continue
        elif menuInput == "6":
            print("\n")
            generateReports()
            continue
        elif menuInput == "7":
            print("\n")
            print("Quitting...Goodbye!")
            quit()
        else:
            print("\n")
            print("Please enter the single digit of your desired option")
            continue

#Function that prints and displays all the tables to the user
#Takes into account to not display data that has been soft deleted
def displayTables():
    print("\n")
    print("COACHES TABLE")
    print("-------------")
    mycursor.execute("SELECT CoachId, CoachName, AlmaMater, YearsCoached FROM Coach WHERE isDeleted = false;")
    Allrecords = mycursor.fetchall()
    #use pd.set_option to display full table with all attributes
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    #use DataFrame for cleaner display
    df = DataFrame(Allrecords, columns=['CoachId', 'CoachName', 'AlmaMater', 'YearsCoached'])
    print(df)
    print("\n")

    print("PLAYER TABLE")
    print("------------")
    mycursor.execute("SELECT PlayerId, TeamId, Name, JerseyNumber, Year, Position, Injured FROM Player WHERE isDeleted = false;")
    Allrecords = mycursor.fetchall()
    #use pd.set_option to display full table with all attributes
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    #use DataFrame for cleaner display
    df = DataFrame(Allrecords, columns=['PlayerId', 'TeamID', 'Name', 'JerseyNumber', 'Year', 'Position', 'Injured'])
    print(df)
    print("\n")

    print("TEAM TABLE")
    print("----------")
    mycursor.execute("SELECT TeamId, CoachId, UniversityName, Address, TeamSize, Wins, Losses, Ties FROM Team WHERE isDeleted = false;")
    Allrecords = mycursor.fetchall()
    #use pd.set_option to display full table with all attributes
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    #use DataFrame for cleaner display
    df = DataFrame(Allrecords, columns=['TeamId', 'CoachId', 'UniversityName', 'Address', 'TeamSize', 'Wins', 'Losses', 'Ties'])
    print(df)
    print("\n")

    print("ACADEMICS TABLE")
    print("---------------")
    mycursor.execute("SELECT AcademicID, PlayerId, Major, Gpa FROM Academics WHERE isDeleted = false;")
    Allrecords = mycursor.fetchall()
    #use pd.set_option to display full table with all attributes
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    #use DataFrame for cleaner display
    df = DataFrame(Allrecords, columns=['AcademicId', 'PlayerId', 'Major', 'Gpa'])
    print(df)
    print("\n")

    print("STATS TABLE")
    print("-----------")
    mycursor.execute("SELECT StatsId, PlayerId, Goals, Assists, MinutesPlayedTotal, GamesPlayedIn FROM Stats WHERE isDeleted = false;")
    Allrecords = mycursor.fetchall()
    #use pd.set_option to display full table with all attributes
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    #use DataFrame for cleaner display
    df = DataFrame(Allrecords, columns=['StatsId', 'PlayerId', 'Goals', 'Assists', 'MinutesPlayedTotal', 'GamesPlayedIn'])
    print(df)
    print("\n")


#Function to allow user to create and add a new player to the database
#Error handling is enforced
def createNewRecord():
            #Gathering necessary user input for player information
            userPlayerName = input("Enter the name of the player: ")
            while True:
                try:
                    userJerseyNumber = int(input("Enter player's jersey number: "))
                    break
                except ValueError:
                    print("Please enter an integer: ")

            while True:
                try:
                    userYear= int(input("Enter player's grade level. Enter 1-4: "))
                    if userYear >= 1 and userYear <= 4:
                        break
                    else:
                        print("Please enter 1-4.")
                        continue
                #Enforce error handling
                except ValueError:
                    print("Please enter an integer 1-4 corresponding to grade level: ")

            userPosition = input("Enter the player's position: ")
            while True:
                userInjured = input("Is the player injured? Type yes or no: ")
                if userInjured == "yes":
                    userInjured = 1
                    break
                elif userInjured == "no":
                    userInjured = 0
                    break
                else:
                    print("Please type yes or no exactly as seen.")
                    continue


            #Gathering academic information of new player
            print("\n")
            print("Now please enter the academic information of the player.")
            userMajor = input("Enter the player's major: ")
            while True:
                try:
                    userGpa = float(input("Enter student's GPA: "))
                    if userGpa >= 1.0 and userGpa <= 4.0:
                        break
                    else:
                        continue
                except ValueError:
                    print("Please enter a decimal: ")


            #Gather stats of new player being added
            print("\n")
            print("Now please enter the stats for the player.")
            while True:
                try:
                    userGoals = int(input("Enter number of goals the player has scored: "))
                    break
                except ValueError:
                    print("Please enter an integer: ")

            while True:
                try:
                    userAssists = int(input("Enter number of assists the player has: "))
                    break
                except ValueError:
                    print("Please enter an integer: ")

            while True:
                try:
                    userMinutesPlayed = int(input("Enter number of minutes the player has played: "))
                    break
                except ValueError:
                    print("Please enter an integer: ")

            print("\n")
            #Display team id's and university names so the user knows what they can choose from
            mycursor.execute("SELECT TeamId, UniversityName FROM Team WHERE isDeleted = false;")
            Allrecords = mycursor.fetchall()
            # use pd.set_option to display full table with all attributes
            pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
            # use DataFrame for cleaner display
            df = DataFrame(Allrecords,
                           columns=['TeamId', 'UniversityName'])
            print(df)
            print("\n")

            test = True

            while True:
                try:
                    while test == True:
                        userPlayerUniversity = int(input(
                            "Enter the university id that the player plays for from the list above: "))
                        if userPlayerUniversity == 1 or userPlayerUniversity == 2 or userPlayerUniversity == 3 or userPlayerUniversity == 4 or userPlayerUniversity == 5 or userPlayerUniversity == 6 or userPlayerUniversity == 7 or userPlayerUniversity == 8 or userPlayerUniversity == 9:
                            test = False
                            break
                        else:
                            test = True
                            continue
                    break
                except ValueError:
                    print("\n")
                    print("Please enter an integer. ")



            while True:
                try:
                    userGamesPlayed = int(input("Enter number of games the player has played in: "))
                    break
                except ValueError:
                    print("Please enter an integer: ")

            #Using transaction and stored procedure created in console
            mycursor.callproc('createPlayer', args=(userPlayerName, userJerseyNumber, userYear, userPosition, userInjured, userMajor, userGpa, userGoals, userAssists, userMinutesPlayed, userGamesPlayed, userPlayerUniversity))
            for result in mycursor.stored_results():
                player = result.fetchall()
                print(player)
            print("\n")
            print("The player was successfully added!")
            db.commit()

#Function that allows for a soft delete of a player - updates all tables on this soft delete where necessary
def deleteRecord():
    test = True
    while (test == True):
        #Shows user list of players they can delete
        mycursor.execute("SELECT PlayerId, Name FROM Player WHERE isDeleted = false;")
        Allrecords = mycursor.fetchall()
        pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
        df = DataFrame(Allrecords,
                       columns=['PlayerId', 'Name'])
        print(df)
        print("\n")
        deletePlayer = input("What player would you like to delete? Please enter the id of the player: ")
        mycursor.execute("SELECT PlayerId FROM Player WHERE PlayerId = %s", [deletePlayer])
        records = mycursor.fetchall()
        if records == []:
            #User must enter a valid player id
            print("Please enter a valid player id from the list below")
            mycursor.execute("SELECT PlayerId, Name FROM Player;")
            Allrecords = mycursor.fetchall()
            pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
            df = DataFrame(Allrecords,
                           columns=['PlayerId', 'Name'])
            print(df)
            continue
        else:
            test = False
            mycursor.execute("UPDATE Player SET isDeleted = true WHERE PlayerId = %s", (deletePlayer,))
            mycursor.execute("UPDATE Academics SET isDeleted = true WHERE PlayerId = %s", (deletePlayer,))
            mycursor.execute("UPDATE Stats SET isDeleted = true WHERE PlayerId = %s", (deletePlayer,))
            print("The player has been deleted from the database.")
            db.commit()



#Funcion allows user to update data
def updateRecord():
    while True:
        print("What would you like to update? :")
        print("1) Coach Information")
        print("2) Basic and Academic Player Information")
        print("3) Player Statistics")
        print("4) Team Information")
        print("\n")
        userChoice = input("Please enter which option you would like to execute: ")
        if (userChoice == "1"):
        #update coach information
            test = True
            while (test == True):
                mycursor.execute("SELECT CoachId, CoachName FROM Coach WHERE isDeleted = false;")
                Allrecords = mycursor.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(Allrecords,
                               columns=['CoachId', 'CoachName'])
                print("\n")
                print(df)
                print("\n")
                userUpdate = input("Please enter the ID of the coach you would like to update: ")
                mycursor.execute("SELECT DISTINCT CoachId FROM Coach WHERE CoachId = %s and isDeleted = false", [userUpdate])
                records = mycursor.fetchall()
                if records == []:
                    print("\n")
                    print("Please enter a valid coach ID. That ID is not in the database.")
                    continue
                else:
                    option = True
                    while (option == True):
                        print("\n")
                        print("What would you like to update? : ")
                        print("1) Name")
                        print("2) Alma Mater")
                        print("3) Years Coached")
                        userChoice = input(
                            "Please type in the corresponding number: ")
                        if userChoice == "1":
                            nameUpdate = input("Please enter the new updated name: ")
                            mycursor.execute("UPDATE Coach SET CoachName = %s WHERE CoachId = %s", (nameUpdate, userUpdate,))
                            print("\n")
                            print("Successfully updated!")
                            test = False
                            option = False
                        elif userChoice == "2":
                            almaMaterUpdate = input("Please enter the updated alma mater: ")
                            mycursor.execute("UPDATE Coach SET AlmaMater = %s WHERE CoachId = %s",
                                             (almaMaterUpdate, userUpdate,))
                            print("\n")
                            print("Successfully updated!")
                            test = False
                            option = False
                        elif userChoice == "3":
                            while True:
                                try:
                                    YearsCoachedUpdate = int(input("Please enter the new updated number of years coached: "))
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter all digits. Try again: ")
                            mycursor.execute("UPDATE Coach SET YearsCoached = %s WHERE CoachId = %s",
                                             (YearsCoachedUpdate, userUpdate,))
                            print("\n")
                            print("Successfully updated!")
                            test = False
                            option = False
                        else:
                            print("\n")
                            print("Please enter a valid option.")
                            continue
            db.commit()
            break
        elif (userChoice == "2"):
        #update player information
            test = True
            while (test == True):
                # Check to make sure the enter student id is in the Students table
                mycursor.execute("SELECT PlayerId, Name FROM Player WHERE isDeleted = false;")
                Allrecords = mycursor.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(Allrecords,
                               columns=['PlayerId', 'Name'])
                print("\n")
                print(df)
                print("\n")
                userUpdate = input("Please enter the ID of the player you would like to update: ")
                mycursor.execute("SELECT DISTINCT PlayerId FROM Player WHERE PlayerId = %s and isDeleted = false", [userUpdate])
                records = mycursor.fetchall()
                if records == []:
                    print("\n")
                    print("Please enter a valid player ID. That ID is not in the database.")
                    continue
                else:
                    option = True
                    while (option == True):
                        print("\n")
                        print("What would you like to update? :")
                        print("1) Name")
                        print("2) Jersey Number")
                        print("3) Year")
                        print("4) Position")
                        print("5) Injured Status")
                        print("6) Major")
                        print("7) GPA")
                        userChoice = input(
                            "Please type in the corresponding number: ")
                        if userChoice == "1":
                            nameUpdate = input("Please enter the new updated name: ")
                            mycursor.execute("UPDATE Player SET Name = %s WHERE PlayerId = %s", (nameUpdate, userUpdate,))
                            print("\n")
                            print("Successfully updated!")
                            test = False
                            option = False
                        elif userChoice == "2":
                            while True:
                                try:
                                    JerseyNumberUpdate = int(input("Please enter the updated jersey number: "))
                                    mycursor.execute("UPDATE Player SET JerseyNumber = %s WHERE PlayerId = %s",
                                                     (JerseyNumberUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")

                        elif userChoice == "3":
                            while True:
                                try:
                                    YearsUpdate = int(input("Please enter the new updated grade level. Enter 1-4: "))
                                    if YearsUpdate >= 1 and YearsUpdate <= 4:
                                        break
                                    else:
                                        print("\n")
                                        print("Please enter 1-4.")
                                        continue
                                except ValueError:
                                    print("\n")
                                    print("Please enter single integer 1-4 corresponding to grade level. Try again: ")
                            mycursor.execute("UPDATE Player SET Year = %s WHERE PlayerId = %s",
                                             (YearsUpdate, userUpdate,))
                            print("\n")
                            print("Successfully updated!")
                            test = False
                            option = False



                        elif userChoice == "4":
                            positionUpdate = input("Please enter the new updated position: ")
                            mycursor.execute("UPDATE Player SET Position = %s WHERE PlayerId = %s", (positionUpdate, userUpdate,))
                            print("\n")
                            print("Successfully updated!")
                            test = False
                            option = False
                        elif userChoice == "5":
                            while True:
                                userInjured = input("Is the player injured? Type yes or no: ")
                                if userInjured == "yes":
                                    mycursor.execute("UPDATE Player SET Injured = 1 WHERE PlayerId = %s",
                                                     (userUpdate,))
                                    test = False
                                    option = False
                                    break
                                elif userInjured == "no":
                                    mycursor.execute("UPDATE Player SET Injured = 0 WHERE PlayerId = %s",
                                                     (userUpdate,))
                                    test = False
                                    option = False
                                    break
                                else:
                                    print("\n")
                                    print("Please type yes or no exactly as seen.")
                                    continue
                        elif userChoice == "6":
                            majorUpdate = input("Please enter the new updated major: ")
                            mycursor.execute("UPDATE Academics SET Major = %s WHERE PlayerId = %s", (majorUpdate, userUpdate,))
                            print("\n")
                            print("Successfully updated!")
                            test = False
                            option = False
                        elif userChoice == "7":
                            while True:
                                try:
                                    userGpa = float(input("Enter student's GPA: "))
                                    if userGpa >= 1.0 and userGpa <= 4.0:
                                        mycursor.execute("UPDATE Academics SET Gpa = %s WHERE PlayerId = %s",
                                                         (userGpa, userUpdate,))
                                        test = False
                                        option = False
                                        break
                                    else:
                                        print("\n")
                                        print("Please enter a gpa between 1.0 and 4.0")
                                        continue
                                except ValueError:
                                    print("\n")
                                    print("Please enter a decimal: ")
                        else:
                            print("\n")
                            print("Please enter a valid option.")
                            continue
            db.commit()
            break
        elif (userChoice == "3"):
            #update player stats
            test = True
            while (test == True):
                # Check to make sure the enter student id is in the Students table
                mycursor.execute("SELECT PlayerId, Name FROM Player WHERE isDeleted = false;")
                Allrecords = mycursor.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(Allrecords,
                               columns=['PlayerId', 'Name'])
                print("\n")
                print(df)
                print("\n")
                userUpdate = input("Please enter the ID of the player you would like to update: ")
                mycursor.execute("SELECT DISTINCT PlayerId FROM Player WHERE PlayerId = %s and isDeleted = false", [userUpdate])
                records = mycursor.fetchall()
                if records == []:
                    print("\n")
                    print("Please enter a valid player ID. That ID is not in the database.")
                    continue
                else:
                    option = True
                    while (option == True):
                        print("\n")
                        print("What would you like to update? :")
                        print("1) Goals")
                        print("2) Assists")
                        print("3) Minutes Played")
                        print("4) Games Played In")
                        userChoice = input(
                            "Please type in the corresponding number: ")
                        if userChoice == "1":
                            while True:
                                try:
                                    goalUpdate = int(input("Please enter the new goal count: "))
                                    mycursor.execute("UPDATE Stats SET Goals = %s WHERE PlayerId = %s", (goalUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")

                        elif userChoice == "2":
                            while True:
                                try:
                                    assistUpdate = int(input("Please enter the new assist count: "))
                                    mycursor.execute("UPDATE Stats SET Assists = %s WHERE PlayerId = %s", (assistUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")
                        elif userChoice == "3":
                            while True:
                                try:
                                    minutesUpdate = int(input("Please enter the new minutes played count: "))
                                    mycursor.execute("UPDATE Stats SET MinutesPlayedTotal = %s WHERE PlayerId = %s", (minutesUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")
                        elif userChoice == "4":
                            while True:
                                try:
                                    playedUpdate = int(input("Please enter the new amounts of games the player has played in: "))
                                    mycursor.execute("UPDATE Stats SET GamesPlayedIn = %s WHERE PlayerId = %s", (playedUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")
                        else:
                            print("\n")
                            print("Please enter a valid option.")
                            continue
            db.commit()
            break

        elif (userChoice == "4"):
            print("\n")
            #update team information
            test = True
            while (test == True):
                # Check to make sure the enter student id is in the Students table
                mycursor.execute("SELECT TeamId, UniversityName FROM Team WHERE isDeleted = false;")
                Allrecords = mycursor.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(Allrecords,
                               columns=['TeamId', 'UniversityName'])
                print("\n")
                print(df)
                print("\n")
                userUpdate = input("Please enter the ID of the team you would like to update: ")
                mycursor.execute("SELECT DISTINCT TeamId FROM Team WHERE TeamId = %s and isDeleted = false", [userUpdate])
                records = mycursor.fetchall()
                if records == []:
                    print("\n")
                    print("Please enter a valid team ID. That ID is not in the database.")
                    continue
                else:
                    option = True
                    while (option == True):
                        print("\n")
                        print("What would you like to update? :")
                        print("1) TeamSize")
                        print("2) Wins")
                        print("3) Losses")
                        print("4) Ties")
                        userChoice = input(
                            "Please type in the corresponding number: ")
                        if userChoice == "1":
                            while True:
                                try:
                                    sizeUpdate = int(input("Please enter the new team size: "))
                                    mycursor.execute("UPDATE Team SET TeamSize = %s WHERE TeamId = %s", (sizeUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")

                        elif userChoice == "2":
                            while True:
                                try:
                                    winUpdate = int(input("Please enter the new number of wins: "))
                                    mycursor.execute("UPDATE Team SET Wins = %s WHERE TeamId = %s", (winUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")
                        elif userChoice == "3":
                            while True:
                                try:
                                    lossUpdate = int(input("Please enter the new number of losses: "))
                                    mycursor.execute("UPDATE Team SET Losses = %s WHERE TeamId = %s", (lossUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")
                        elif userChoice == "4":
                            while True:
                                try:
                                    tieUpdate = int(input("Please enter the new number of ties: "))
                                    mycursor.execute("UPDATE Team SET Ties = %s WHERE TeamId = %s", (tieUpdate, userUpdate,))
                                    print("\n")
                                    print("Successfully updated!")
                                    test = False
                                    option = False
                                    break
                                except ValueError:
                                    print("\n")
                                    print("Please enter integers. Try again: ")
                        else:
                            print("\n")
                            print("Please enter a valid option.")
                            continue
            db.commit()
            break
        else:
            print("\n")
            print("Please enter a valid integer option.")
            continue

#Function allows for user to query data from specific given options
def queryData():
    print("What would you like to specifically look for in the database? : ")
    print("1) Which players are eligible to play")
    print("2) Which players are currently injured")
    print("3) Most experienced coaches in the league")
    print("4) See a specific group of players based on their year")
    print("5) See which top players are on a specific team")
    print("6) See all players and their stats")
    print("7) See team records ")

    checkWhile = True
    while (checkWhile == True):
        print("\n")
        fieldInput = input("Please enter the corresponding number: ")
        if fieldInput == "1":
            mycursor.callproc('getEligibilePlayers')
            for result in mycursor.stored_results():
                eligibile = result.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(eligibile, columns=['Name', 'Gpa', 'UniversityName'])
                print(df)
            break
        elif fieldInput == "2":
            mycursor.callproc('getInjuredPlayers')
            for result in mycursor.stored_results():
                injured = result.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(injured, columns=['Name', 'JerseyNumber', 'UniversityName'])
                print(df)
            break
        elif fieldInput == "3":
            mycursor.callproc('getMostExperiencedCoaches')
            for result in mycursor.stored_results():
                experience = result.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(experience, columns=['CoachName', 'YearsCoached', 'UniversityName'])
                print(df)
            break
        elif fieldInput == "4":
            userYearInput = input("What year would you like to query by?: ")
            mycursor.callproc('getPlayersByYear', args = [userYearInput])
            for result in mycursor.stored_results():
                byYear = result.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(byYear, columns=['Name', 'Year', 'JerseyNumber', 'UniversityName'])
                print(df)
            break
        elif fieldInput == "5":
            while True:
                try:
                    print("\n")
                    mycursor.execute("SELECT TeamId, UniversityName FROM Team WHERE isDeleted = false;")
                    Allrecords = mycursor.fetchall()
                    # use pd.set_option to display full table with all attributes
                    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                    # use DataFrame for cleaner display
                    df = DataFrame(Allrecords,
                                   columns=['TeamId', 'UniversityName'])
                    print(df)
                    print("\n")

                    userTeamName = int(input("What school would you like to query by? Please enter the corrosponding team ID from list above: "))
                    mycursor.callproc('playersFromSchool', args = [userTeamName])
                    for result in mycursor.stored_results():
                        school = result.fetchall()
                        pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                        df = DataFrame(school, columns=['Name', 'JerseyNumber', 'Year', 'Position', 'UniversityName'])
                        print(df)
                    break
                except ValueError:
                    print("\n")
                    print("Please enter integers. Try again: ")
            break


        elif fieldInput == "6":
            mycursor.callproc('playerStats')
            for result in mycursor.stored_results():
                stats = result.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(stats, columns=['Name', 'JerseyNumber', 'UniversityName', 'MinutesPlayedTotal', 'GamesPlayedIn', 'goals', 'assists'])
                print(df)
            break
        elif fieldInput == "7":
            mycursor.callproc('teamRecords')
            for result in mycursor.stored_results():
                records = result.fetchall()
                pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                df = DataFrame(records, columns=['UniversityName', 'Wins', 'Losses', 'Ties'])
                print(df)
            break
        else:
            print("Please enter a digit provided.")
            continue



#Function generates 4 reports for user that may be a common necessity
def generateReports():

    #Report 1 - Average Stats
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM avgStats")
    avg = mycursor.fetchall()
    df = pd.DataFrame(avg, columns=['UniversityName', 'Avg Goals', 'Avg Assists', 'AvgMinutesPlayedTotal', 'AvgGamesPlayedIn'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv("AverageStats.csv")

    #Report 2 - Top Goal Scorers
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM topTenGoalScorers")
    avg = mycursor.fetchall()
    df = pd.DataFrame(avg, columns=['Name', 'JerseyNumber', 'Position', 'MaxGoals', 'UniversityName'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv("topGoalScorers.csv")


    #Report 3 - Most Minutes Played
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM topTenMinutePlayers")
    avg = mycursor.fetchall()
    df = pd.DataFrame(avg, columns=['Name', 'JerseyNumber', 'Position', 'MinutesPlayed', 'UniversityName'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv("topMinutePlayers.csv")

    #Report 4 - Injuries on Each Team
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM injuryTeamCount")
    avg = mycursor.fetchall()
    df = pd.DataFrame(avg, columns=['Count', 'UniversityName'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv("injuryTeamCount.csv")

    print("\n")
    print("Reports have successfully been created!")
    print("\n")
    print("Created reports include:")
    print("Report #1: Average Stats")
    print("Report #2: Top Ten Goal Scorers")
    print("Report #3: Players with Max Minutes")
    print("Report #4: Injuries on each Team")