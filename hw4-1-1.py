# Author: ALJ (AMDG) 10/6/20

wins = 3
ties = 1

team1_wins = int(input("How many wins did Team One have? "))
team1_ties = int(input("How many ties did Team One have? "))
team1_points = (team1_wins * wins + team1_ties * ties)

team2_wins = int(input("How many wins did Team Two have? "))
team2_ties = int(input("How many ties did Team Two have? "))
team2_points = (team2_wins * wins + team2_ties * ties)

if team1_points > team2_points:
    print("Team One beat Team Two!")
elif team2_points > team1_points:
    print("Team Two beat Team One!")
else:
    print("Team One tied Team Two!")