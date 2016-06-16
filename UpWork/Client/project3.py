################################### TASK 0 ##########################################
# Complete import of libraries and functions:
# Import tabulate function from tabulate.py
# Import sortTable function function from sorter.py
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sorter import sortTable
import tabulate
import numpy as np
################################### TASK 1 ##########################################
# Write the function that reads information of the groups from the file groupInfo.txt
# @Parameter: groupName
#   - Data type: String
#   - Possible values: 'groupA', 'groupB', 'groupC', 'groupD'
# @Returns a list of teams in groupName
#   - Format of the list: [str, str, str, str]
#   - E.g.: ['India', 'Netherlands', 'Brazil', 'Spain']
def readGroupInfo(groupName):
    file_open = open ('groupinfo.txt', 'r') # This is the line to read the file of the group
    datalines = file_open.readlines()
    readgrouplist = list()
    iteratorvalue = 0
    for line in datalines:
        if groupName == 'groupA':
            readgrouplist=[datalines[1], datalines[2], datalines[3], datalines[4]]
            return readgrouplist
        elif groupName == 'groupB':
            readgrouplist=[datalines[6], datalines[7], datalines[8], datalines[9]]
            return readgrouplist
        elif groupName == 'groupC':
            readgrouplist=[datalines[11], datalines[12], datalines[13], datalines[14]]
            return readgrouplist
        elif groupName =='groupD':
            readgrouplist=[datalines[11], datalines[17], datalines[18], datalines[19]]
            return readgrouplist
        else:
            print ('There is an error in the input group')
            exit(0)
################################### TASK 2 ###########################################
# Write the function that reads the results of round 0 from the file round0Results.txt
# @Parameter: teams
#   - List of the format [str, str, str, str] as specified above
# @Returns: List of strings containing results as specified above
def readResultsRound0(teams):
    file_open =open('round0Results.txt', 'r')
    data_file = file_open.readlines()
    read_result_list = list() # this is the match list which will return the list of the matches
    for line in data_file:
        for i in teams:
            if line.__contains__(i):
                if line in read_result_list:
                    continue
                else:
                    read_result_list.append(line)
            else:
                continue
    return read_result_list
################################### TASK 3 ##########################################
#  Write the function that builds the Points Table
# @Parameter: teams
#   - List of the format [str, str, str, str]
# @Parameter: results
#   - List of the format specified above
# @Returns: point table
#   - List of the format [[str, int], [str, int]... [str, int]]
def buildPointsTable(teams, results):
    d=dict()
    for i in range(len(teams)):
        d[teams[i]] = 0
    for i in range(len(teams)):
        x = results[i].split(', ')
        if (int(x[2])) > int(x[3]):
            d[x[0]] += 3   # if the first tem score greater than the 2nd team
        elif (int(x[2])) < int(x[3]):
            d[x[1]] += 3  # if the 2nd team score is lesser than the fiver1 team
        else:
            d[x[0]] += 1  # this is incrementing both of the team
            d[x[1]] += 1  # this is incrementing the both team
    result = []  # this is a list
    for i in range(len(teams)):
        result.append([teams[i], d[teams[i]]])
    return result
################################### TASK 4 ############################################
# Write the function that breaks ties in ranking values of the Rank Table
# @Parameter: rankTable
#   - List of the format [[str, int, int],...[str, int, int]]
# @Returns: rankTableTieBreaker
#   - List of the format [[str, int, int],...[str, int, int]]
def breakTies(rankTable):
    rank = len(rankTable)
    rankTableTieBreaker = sortTable(rankTable,0, 1, 2, 'ascending')
    for i in range(len(rankTable)):
        rankTable[i][2] = i + 1   # this is the sub list access of ith element
    return rankTableTieBreaker

################################### TASK 5 ######################################
# Write the function that adds ranks to the Points Table
# @Parameter: pointsTable
#   - List of the format [str, int],..., [[str, int]]
# @Returns: rankTable
#   - List of the format [[str, int, int],..., [[str, int, int]]
def addRankToPointsTable(pointsTable):
    Points = len(pointsTable)
    Add = sortTable(pointsTable, 0, 1, Points - 1, 'descending')  # this is sorting the table in the decending order
    for i in range(len(pointsTable)):
        Add[i].append(i + 1)  # Add list is being append with the values
    return breakTies(Add)
    
    
    
################################### TASK 6 ######################################
# Write the function that builds the Rank Table
# @Parameter: groupName
#   - Data type: String
# @Returns: rank table
#   - List of the format [[str, int, int],...,[[str, int, int]]
def buildRankTable(groupName):
    # 1. Read groupInfo, i.e., the teams belong to groupName.
    team_ranktable =readGroupInfo(groupName)
    result_ranktable = readResultsRound0(team_ranktable)
    # 2. Get the results for the teams of groupName
    # 3. Compute the points table for groupName
    ranktable_build = buildPointsTable(team_ranktable, result_ranktable)
    # 4. Add a column called rank to the points table, and get the rankTable
    RankTable = addRankToPointsTable(ranktable_build)
    return RankTable
    
    
    
################################### TASK 7 ######################################
# Write a function that builds a Crossed Table
# @Parameter: rankTableGroupX
#   - List of the format [[str, int, int],...[str, int, int]]
# @Parameter: rankTableGroupY
#   - List of the format [[str, int, int],...[str, int, int]] 
# @Returns: cross table
#   -List of the format [[str, str], [str, str]]
def buildCrossedTable(rankTableGroupX, rankTableGroupY):
    ct = [[rankTableGroupX[0][0], rankTableGroupY[1][0]], [rankTableGroupY[0][0], rankTableGroupX[1][0]]]
    return ct
    
    
    
################################### TASK 8 ######################################
# Write a function that determines the winner of a game
# This function determine the winner of match given the the
# @Parameter: teams (list of data types [str, str]) 
# @Return: winner (data type string)
def determineWinner(teams):
    team1 = teams[0]
    team2 = teams[1]
    f_open = open ('breaker.txt', 'r')
    data_in_lines = f_open.readlines()
    for line in data_in_lines:
        if line.__contains__(team1) and line.__contains__(team2):
            line = line.split(',')
            if int(line[2]) > int(line[3]):
                return team1
            elif int(line[2]) < int(line[3]):
                return team2
    
    
    
################################### TASK 9 ######################################
# Plot statistics of three best teams of the world cup
# @Parameter: teams
#   - Data type: List of the format [str, str, str]
#   - E.g.: ['Brazil', 'Germany', 'Italy']
# @Returns: None
def plotGoalsBarChar(teams):
    file_open = open ('round0Results.txt', 'r')
    data = file_open.readlines()
    file_open.close()
    team_list_goaldid = 0
    team_list_goalTaken = 0
    team1_list_goaldid = 0
    team1_list_goalTaken = 0
    team2_list_goaldid = 0
    team2_list_goalTaken = 0
    if teams[0] == str(teams[0]):
            for line in data:
                if line.__contains__(str(teams[0])):
                    line = line.split(',')
                    print (line)
                    print str(teams[0])
                    if str(line[0]) == str(teams[0]):
                        team_list_goaldid += int(line[2])
                        team_list_goalTaken += int(line[3])
                    elif str(line[1]) == str(teams[0]):
                        team_list_goaldid += int(line[3])
                        team_list_goalTaken += (line[2])
    if teams[1] == str(teams[1]):
            for line in data:
                if line.__contains__(str(teams[1])):
                    line = line.split(',')
                    if line[0] ==str(teams[1]):
                        team1_list_goaldid += int(line[2])
                        team1_list_goalTaken += int(line[3])
                    elif line[1] == str(teams[1]):
                        team1_list_goaldid += int(line[3])
                        team1_list_goalTaken += int(line[2])
    if teams[2] == str(teams[2]):
            for line in data:
                if line.__contains__(str(teams[2])):
                    line = line.split(',')
                    if line[0] == str(teams[2]):
                        team2_list_goaldid += int(line[2])
                        team2_list_goalTaken += int (line[3])
                    elif line[1] == str(teams[2]):
                        team2_list_goaldid += int(line[3])
                        team2_list_goalTaken += int(line[2])

    print ('Brazil goal did '+ str(team_list_goaldid)) # just for debuggin
    print ('Brazil goal taken '+str(team_list_goalTaken)) # just for debuggin
    print ('team1 goal did ' + str(team1_list_goaldid)) # just for debuggin
    print ('team1 goal taken ' + str(team1_list_goalTaken)) # just for debuggin
    print ('team2 goal did ' + str (team2_list_goalTaken)) # just for debugging
    print ('team2 goal taken ' + str(team2_list_goalTaken))



    plt.title('Round 0 Statistics of World Cup Best Teams')
    plt.xlabel('Teams')
    plt.ylabel('Number of Goals')
    plt.yscale = 35
    N = 4
    No = 35
    ind = np.arange(N)
    width = 0.35
    plt.xticks(ind + width, (teams[0], teams[1], teams[2]))
    plt.show()
    
#################################### Main #######################################
# Main() is in the charge to execute the actions related to different rounds of
# this tournament. It is also in change to display the results of the games
# of different rounds, display 'match tables', and call the function that
# plot statistics of the best three teams of the World Cup.
# PLEASE DO NOT CHANGE THIS FUNCTION AT ALL.

def main():

    
    # 1. Initialize nRounds to 4
    nRounds = 4

    # rankTableA = buildRankTable('groupA')
    # for r in rankTableA:
    #     print (r)

    # 2. Loop for each round
    for r in range(nRounds):
        
        # 2.1 Actions for round 0
        if r == 0:
            
            # Build rank tables of the 4 groups
            rankTableA = buildRankTable('groupA')
            rankTableB = buildRankTable('groupB')
            rankTableC = buildRankTable('groupC')
            rankTableD = buildRankTable('groupD')


            # print rank tables of the 4 groups
            print('***************************************************************')
            print('*              Rank Tables after ROUND 0                      *')
            print('***************************************************************')

            print('\n\nRank table for groupA')
            print(tabulate(rankTableA, headers = ['Team', 'Point', 'Rank']))
            print('\n\nRank table for groupB')
            print(tabulate(rankTableB, headers = ['Team', 'Point', 'Rank']))
            print('\n\nRank table for groupC')
            print(tabulate(rankTableC, headers = ['Team', 'Point', 'Rank']))
            print('\n\nRank table for groupD')
            print(tabulate(rankTableD, headers = ['Team', 'Point', 'Rank']))

            # Groups A and B are corss out to play in round 1
            crossedTableAB = buildCrossedTable(rankTableA, rankTableB)

            # Groups C and D are corss out to play in round 1
            crossedTableCD = buildCrossedTable(rankTableC, rankTableD)

            # Print match tables of next round
            print('\n\nMatches for next round resulting of crossing group A and B')
            print(tabulate(crossedTableAB, headers = ['Team1', 'Team2']))

            print('\n\nMatches for next round resulting of crossing group C and D')
            print(tabulate(crossedTableAB, headers = ['Team1', 'Team2']))
                

        # 2.2 Actions for round 1
        if r == 1:

            # Determine the two winners of group AB, which will play in round 2
            winnerListAB = []
            for i in range(len(crossedTableAB)):
                winnerListAB.append(determineWinner(crossedTableAB[i]))

            # Determine the two winners of group CD, which will play in round 2
            winnerListCD = []
            for i in range(len(crossedTableCD)):
                winnerListCD.append(determineWinner(crossedTableCD[i]))

            # Preparte cross table AB to show results
            if winnerListAB[0] == crossedTableAB[0][0] or winnerListAB[0] == crossedTableAB[0][1]:
                crossedTableAB[0].append(winnerListAB[0])
                crossedTableAB[1].append(winnerListAB[1])
            else:
                crossedTableAB[0].append(winnerListAB[1])
                crossedTableAB[1].append(winnerListAB[0])

            # Preparte cross table CD to show results
            if winnerListCD[0] == crossedTableCD[0][0] or winnerListCD[0] == crossedTableCD[0][1]:
                crossedTableCD[0].append(winnerListCD[0])
                crossedTableCD[1].append(winnerListCD[1])
            else:
                crossedTableCD[0].append(winnerListCD[1])
                crossedTableCD[1].append(winnerListCD[0])

            # Prepare winner list of group AB to show match of next round
            toPrintWinnerListAB = []
            toPrintWinnerListAB.append(winnerListAB)
            

            # Prepare winner list of group CD to show match of next round
            toPrintWinnerListCD = []
            toPrintWinnerListCD.append(winnerListCD)
                   
            # Print winners of crossed table AB
            print('\n\n')
            print('***************************************************************')
            print('*                          ROUND 1                            *')
            print('***************************************************************')
            print('\n\nResults of the matches of the crossed groups A and B')
            print(tabulate(crossedTableAB, headers = ['Team1', 'Team2', 'Winner']))
            
            # Print winners of crossed table CD
            print('\n\nResults of the matches of the crossed groups C and D')
            print(tabulate(crossedTableCD, headers = ['Team1', 'Team2', 'Winner']))

            #Print match table of group AB for next round
            print('\n\nMatch tables of groups A and B for semi-finals')
            print(tabulate(toPrintWinnerListAB, headers = ['Team1', 'Team2']))

            #Print match table of group CD for next round
            print('\n\nMatch tables of groups C and D for semi-finals')
            print(tabulate(toPrintWinnerListCD, headers = ['Team1', 'Team2']))

            
        # 2.3 Actions for round 2 (semi final)
        if r == 2:

            # Detemine the winner and the looser of the two classified teams of group AB
            winnerAB = determineWinner(winnerListAB)
            if winnerAB != winnerListAB[0]:
                loserAB = winnerListAB[0]
            else:
                loserAB = winnerListAB[1]

            # Detemine the winner and the looser of the two classified teams of group CD
            winnerCD = determineWinner(winnerListCD)
            if winnerCD != winnerListCD[0]:
                loserCD = winnerListCD[0]
            else:
                loserCD = winnerListCD[1]

            #Preparte winner list AB to show results
            winnerListAB.append(winnerAB)
            toPrintWinnerListAB = []
            toPrintWinnerListAB.append(winnerListAB)

            #Preparte winner list AB to show results
            winnerListCD.append(winnerCD)
            toPrintWinnerListCD = []
            toPrintWinnerListCD.append(winnerListCD)

            # Prepare match table for final
            toPrintChampionsip = []
            toChampionship = []
            toChampionship.append(winnerAB)
            toChampionship.append(winnerCD)
            toPrintChampionsip.append(toChampionship)

            # Prepare match table for third place
            toPrintThirdPlace = []
            toThirdPlace = []
            toThirdPlace.append(loserAB)
            toThirdPlace.append(loserCD)
            toPrintThirdPlace.append(toThirdPlace)

            # Print winners of winner list AB
            print('\n\n')
            print('***************************************************************')
            print('*                         SEMI FINALS                         *')
            print('***************************************************************')
            print('\n\nResults of the matches of groups A and B in semi-finals')
            print(tabulate(toPrintWinnerListAB, headers = ['Team1', 'Team2', 'Winner']))

            # Print winners of winner list CD
            print('\n\nResults of the matches of groups C and D in semi-finals')
            print(tabulate(toPrintWinnerListCD, headers = ['Team1', 'Team2', 'Winner']))

            #Print match table for championship
            print('\n\nMatch table for championship')
            print(tabulate(toPrintChampionsip, headers = ['Team1', 'Team2']))

            #Print match table for third place
            print('\n\nMatch table for third place')
            print(tabulate(toPrintThirdPlace, headers = ['Team1', 'Team2']))
                       

        # 2.4 Actions for round 3 (final)
        if r ==3:

            # Get champion and sub-champion
            champion = determineWinner([winnerAB, winnerCD])
            if champion != winnerAB:
                subChampion = winnerAB
            else:
                subChampion = winnerCD

            # Get third place
            competitors = []
            competitors.append(loserAB)
            competitors.append(loserCD)
            thirdPlace = determineWinner(competitors)

            # Prepare table to show results of championship match
            toPrintChampionsip = []
            toChampionship.append(champion)
            toPrintChampionsip.append(toChampionship)

            # Prepare table to show results of third place match
            toPrintThirdPlace = []
            toThirdPlace.append(thirdPlace)
            toPrintThirdPlace.append(toThirdPlace)

            # Prepare table for final results
            toPrintFinalResults = []
            finalResults = []
            finalResults.append(champion)
            finalResults.append(subChampion)
            finalResults.append(thirdPlace)
            toPrintFinalResults.append(finalResults)

            #Print results of championship match
            print('\n\n')
            print('***************************************************************')
            print('*                          FINALS                             *')
            print('***************************************************************')
            print('\n\nResults of the championship match')
            print(tabulate(toPrintChampionsip, headers = ['Team1', 'Team2', 'Winner']))

            # Print results of third place match
            print('\n\nesults of the third place match')
            print(tabulate(toPrintThirdPlace, headers = ['Team1', 'Team2', 'Winner']))
            
            # Print final results:
            print('\n\nFinals results:')
            print(tabulate(toPrintFinalResults, headers = ['Champion', 'Sub-Champion', 'Third Place']))

    # 3. Plot statistics of champion, subChampion and thirdPlace
    print('\n\n')
    print('***************************************************************')
    print('*                       Statistics                            *')
    print('***************************************************************')
    print('\n\nDo the results of round 0 coincide with the forecast?')
    print('Let\'s compare the scores of the champion, sub-champion and')
    print('third-place')
    plotGoalsBarChar(finalResults)



    

    
