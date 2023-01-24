from itertools import combinations
import random

class LeagueController:

    def __init__(self, leagueTeams):
        self.leagueTeams = leagueTeams
        self.lottery = []
        self.matchesResult = {}
        self.teamsResult = {i: [0, 0, 0, 0] for i in self.leagueTeams}
        self.leagueResult = {}
        self.num = 0

    def get_lottery(self):
        self.lottery += [list(c) for c in combinations(self.leagueTeams, 2)]
        random.shuffle(self.lottery)
        return self.lottery

    def updateTeamValue(self, match, team1, team2):
        team1_data = self.teamsResult.get(match[0])
        team1_goals_scored = team1_data[1] + team1
        team1_goals_received = team1_data[2] + team2
        team1_total_goals = team1_goals_scored - team1_goals_received
        team2_data = self.teamsResult.get(match[1])
        team2_goals_scored = team2_data[1] + team2
        team2_goals_received = team2_data[2] + team1
        team2_total_goals = team2_goals_scored - team2_goals_received

        if team1 > team2:
            self.teamsResult[match[0]] = [team1_data[0] + 3, team1_goals_scored, team1_goals_received,
                                          team1_total_goals]
            self.teamsResult[match[1]] = [team2_data[0], team2_goals_scored, team2_goals_received, team2_total_goals]
        elif team1 < team2:
            self.teamsResult[match[0]] = [team1_data[0], team1_goals_scored, team1_goals_received, team1_total_goals]
            self.teamsResult[match[1]] = [team2_data[0] + 3, team2_goals_scored, team2_goals_received,
                                          team2_total_goals]
        else:
            self.teamsResult[match[0]] = [team1_data[0] + 1, team1_goals_scored, team1_goals_received,
                                          team1_total_goals]
            self.teamsResult[match[1]] = [team2_data[0] + 1, team2_goals_scored, team2_goals_received,
                                          team2_total_goals]

    def get_matches_result(self):
        for i in range(0, len(self.lottery)):
            team1 = random.randint(0, 5)
            team2 = random.randint(0, 5)
            self.matchesResult[str(self.lottery[i])] = [team1, team2]
            self.updateTeamValue(self.lottery[i], team1, team2)
        return self.matchesResult

    def get_league_result(self):
        self.leagueResult = {key : value for key , value in sorted(self.teamsResult.items(), key=lambda item: (item[1][0], item[1][3]), reverse=True)}
        return self.leagueResult


    def format_result(self,dic_input):
        output_string=''
        j = 1
        for i in dic_input.keys() :
                output_string += 'number {:2d}'.format(j)+' : '+str(i) +'\t\t\t\t\t'+str(dic_input[i])
                output_string +='\n'
                j+=1
        return output_string


    def runLeague(self):
        self.get_lottery()
        self.get_lottery()
        self.get_matches_result()

        result1= self.format_result(self.get_league_result())
        return result1
