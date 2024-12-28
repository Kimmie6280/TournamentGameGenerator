from itertools import combinations
class myTournment:

    def getTeams(self):

        self.teams = 0
        while True:
            self.teams = int(input("Enter the number of teams "))
            if self.teams >=2:
                break
            else:
                print("You need to enter a number greater than 1. ")
        return self.teams

    def getNames(self):
        self.names = []
        while len(self.names) < self.teams:  # Keep asking until enough names are entered
            name = input("Please enter the team name: ")
            if len(name) < 2:
                print("Character name needs to have at least 2 characters.")
                continue  # Skip to the next iteration and don't append the name
            self.names.append(name)  # Add valid name to the list


    def getGames(self):
        self.games = 0
        while True:
            try:
                self.games = int(input("Enter the number of games played. "))
                if self.games >= self.teams:
                    print(f"The number of games each team will play is {self.games}.")
                    break  # Exit the loop
                else:
                    print(
                        "Invalid number of games. Each team plays each other at least once in the regular season, try again. ")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def getWins(self):

        self.wins = []

        for i in range(len(self.names)):

            while True:
                try:
                    wins = int(input(f"Enter the number of wins for {self.names[i]}: "))
                    if wins < 0:
                        print("The minimum number of wins is 0, try again.")
                    else:
                        self.wins.append(wins)  # Add the wins to the list
                        print(f"Team {self.names[i]} has {wins} wins.")
                        break  # Exit the inner loop once valid input is provided
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

    def generateTeams(self):

        self.pairs = []

        left = 0
        right = len(self.names)-1
        while left < right:
            self.pairs.append((self.names[left],self.names[right]))
            left+=1
            right-=1

        for pair in self.pairs:
            print(f"{pair[0]} vs {pair[1]}")


t = myTournment()
t.getTeams()
t.getNames()
t.getGames()
t.getWins()
t.generateTeams()