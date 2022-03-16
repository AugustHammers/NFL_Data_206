#Program by August Hammers

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import math

def most_yards(season):
    #if/elif sequence to get right csv file (Pandas 1)
    if season == "2016":
        df = pd.read_csv("data/2016 Passing.csv")
        df.drop(columns=['Rk','4QC', 'GWD', 'EXP']) #Drop redundant columns
        df = df.dropna() #Drop empty cells

    elif season == "2017":
        df = pd.read_csv("data/2017 Passing.csv")
        df.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        df = df.dropna() 

    elif season == "2018":
        df = pd.read_csv("data/2018 Passing.csv")
        df.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        df = df.dropna() 

    elif season == "2019":
        df = pd.read_csv("data/2019 Passing.csv")
        df.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        df = df.dropna() 

    elif season == "2020":
        df = pd.read_csv("data/2020 Passing.csv")
        df = df.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        df = df.dropna() 

    df = df.sort_values(by=['Yds']) #Sorts the data frame by # of yards
 
    #Plotting stuff (Matplotlib 1)
    ax = df["Yds"].plot(kind="bar", xlabel="Teams", ylabel="Yards")
    ax.set_xticklabels(df["Tm"].tolist())
    plt.tight_layout()
    plt.show()

    team_name = df["Tm"].tail(1).item() #Gets team name for print
    num_yds = int(df["Yds"].tail(1).item())#Gets # of yards for print 

    print("The " + team_name + " had the most passing yards in " + season + " with a total of", num_yds, "yards!")

def top_five_ints(season):
    #if/elif sequence to get right csv file
    if season == "2016":
        df = pd.read_csv("data/2016 Passing.csv")
        df.drop(columns=['Rk','4QC', 'GWD', 'EXP']) #Drop redundant columns
        df = df.dropna() #Drop empty cells

    elif season == "2017":
        df = pd.read_csv("data/2017 Passing.csv")
        df.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        df = df.dropna() 

    elif season == "2018":
        df = pd.read_csv("data/2018 Passing.csv")
        df.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        df = df.dropna() 

    elif season == "2019":
        df = pd.read_csv("data/2019 Passing.csv")
        df.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        df = df.dropna() 

    elif season == "2020":
        df = pd.read_csv("data/2020 Passing.csv")
        df = df.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        df = df.dropna() 
    
    df = df.sort_values(by=["Int"], ascending=False)

    int_list = df["Int"].tolist()
    int_list.sort(reverse=True) #Data analysis using list/dicts 2
    
    team_list = df["Tm"].tolist()

    new_list = []
    temp_list = []

    for i, txt in enumerate(int_list):
        if i >= 5:
            break
        new_list.append(txt)
        temp_list.append(team_list[i])

    int_list = new_list
    team_list = temp_list

    ints = pd.Series(int_list)

    #Plotting stuff 
    ax = ints.plot(kind="bar", xlabel="Teams", ylabel="Interceptions")
    ax.set_xticklabels(team_list)
    plt.tight_layout()
    plt.show()
    
    for i, txt in enumerate(int_list):
        print(team_list[i] + ":", txt, "interceptions.")

    print("The average # of interceptions in", season, "was", math.ceil(df["Int"].mean()), "interceptions.") #(Pandas 2)

def yards_record_correlation(season):
    #if/elif sequence to get right csv file
    if season == "2016":
        standings = pd.read_csv("data/2016 Standings.csv")
        passing = pd.read_csv("data/2016 Passing.csv")
        passing = passing.drop(columns=['Rk', '4QC', 'GWD', 'EXP']) #Drop redundant columns
        standings = standings.dropna() #Drop empty cells
        passing = passing.dropna()

    elif season == "2017":
        standings = pd.read_csv("data/2017 Standings.csv")
        passing = pd.read_csv("data/2017 Passing.csv")
        passing = passing.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        standings = standings.dropna()
        passing = passing.dropna()

    elif season == "2018":
        standings = pd.read_csv("data/2018 Standings.csv")
        passing = pd.read_csv("data/2018 Passing.csv")
        passing = passing.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        standings = standings.dropna()
        passing = passing.dropna()

    elif season == "2019":
        standings = pd.read_csv("data/2019 Standings.csv")
        passing = pd.read_csv("data/2019 Passing.csv")
        passing = passing.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        standings = standings.dropna()
        passing = passing.dropna()

    elif season == "2020":
        standings = pd.read_csv("data/2020 Standings.csv")
        passing = pd.read_csv("data/2020 Passing.csv")
        passing = passing.drop(columns=['Rk', '4QC', 'GWD', 'EXP'])
        standings = standings.dropna()
        passing = passing.dropna()

    passing = passing.sort_values(by=["Tm"]) #Sorts the data frame by # of yards
    standings = standings.sort_values(by=["Tm"]) #Sorts the data frame by # of wins

    passing_list = passing["Yds"].tolist() #Puts these series into a list format
    standings_list = standings["W"].tolist()
    annotations = passing["Tm"].tolist()

    plt.scatter(passing_list, standings_list) #(Matplotlib 2)

    # for i, txt in enumerate(annotations): #This labeled each point to make sure it represented the right team
    #     plt.annotate(txt, (passing_list[i], standings_list[i]))

    #Line of best fit section, could be a separate function but i'm lazy | https://www.kite.com/python/answers/how-to-plot-a-line-of-best-fit-in-python

    x = np.array(passing_list)
    y = np.array(standings_list)

    m, b = np.polyfit(passing_list, standings_list, 1) #y = mx+b (Data analysis using lists/dicts 1)
    plt.plot(x, m*x + b)

    plt.tight_layout()
    plt.show()

    if m > 0:
        print ("The slope of the line of best fit is:", m, "and indicates a positive relationship between the # of passing yards a team has and the # of wins they have.")
    elif m < 0:
        print ("The slope of the line of best fit is:", m, "and indicates a negative relationship between the # of passing yards a team has and the # of wins they have.")
    elif m == 0:
        print ("The slope of the line of best fit is 0 and indicates no relationship between the # of passing yards a team has and the # of wins they have.")

def passing_questions():
    print("1 What team had the most passing yards in a season?")
    print("2 What 5 teams had the most interceptions in a season?")
    print("3 How does the number of passing yards a team has relate to a team's record in a season?")
    print("Select an inquiry with its corresponding number.")
    user_inquiry = input("Enter a number: ")

    if user_inquiry == "1":
        season_inquiry = input("Pick a season from 2016-2020: ")
        
        most_yards(season_inquiry)

    elif user_inquiry == "2":
        season_inquiry = input("Pick a season from 2016-2020: ")

        top_five_ints(season_inquiry)

    elif user_inquiry == "3":
        season_inquiry = input("Pick a season from 2016-2020: ")

        yards_record_correlation(season_inquiry)
    else:
      print("Error: Please choosea correct input")

passing_questions()