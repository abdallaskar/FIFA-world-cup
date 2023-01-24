import random
#from view.gui import Gui



def get_group_lottery(group):
    random.shuffle(group)
    lottery = []
    if len(group) % 2 == 0:
        for i in range(0, len(group), 2):
            lottery.append([group[i], group[i + 1]])
    else:
        for i in range(0, len(group) - 1, 2):
            lottery.append([group[i], group[i + 1]])
        lottery.append([group[len(group) - 1]])
    return lottery


def get_lottery_result(lottery):
    lottery_result = {}
    for i in range(len(lottery)):
        team1 = random.randint(0, 5)
        team2 = random.randint(0, 5)
        if team1 == team2:
            team1 += 1
        if len(lottery[i]) == 1:
            lottery_result[str(lottery[i])] = [lottery[i][0]]
            return lottery_result
        else:
            if team1 > team2:
                lottery_result[str(lottery[i])] = [team1, team2, lottery[i][1]]
            else:
                lottery_result[str(lottery[i])] = [team1, team2, lottery[i][0]]
    return lottery_result


class CupController:
    def __init__(self, cupTeams,):
        self.cupTeams = cupTeams
        self.group2 = []
        self.group1 = []
        self.lottery1 = []
        self.lottery2 = []
        self.lottery1_result = {}
        self.lottery2_result = {}

    def divide_teams(self):
        if len(self.cupTeams) % 2 == 0:
            for i in range(0, len(self.cupTeams), 2):
                self.group1.append(self.cupTeams[i])
                self.group2.append(self.cupTeams[i + 1])
        else:
            for i in range(0, len(self.cupTeams) - 1, 2):
                self.group1.append(self.cupTeams[i])
                self.group2.append(self.cupTeams[i + 1])
            self.group1.append(self.cupTeams[len(self.cupTeams) - 1])

    def get_round_result(self, groupNumber):
        if groupNumber == 1:
            self.lottery1 = get_group_lottery(self.group1)
            self.lottery1_result = get_lottery_result(self.lottery1)
            for i in range(len(self.lottery1_result)):
                if len(list(self.lottery1_result.values())[i]) == 3:
                    self.group1.remove(list(self.lottery1_result.values())[i][2])
        else:
            self.lottery2 = get_group_lottery(self.group2)
            self.lottery2_result = get_lottery_result(self.lottery2)
            for i in range(len(self.lottery2_result)):
                if len(list(self.lottery2_result.values())[i]) == 3:
                    self.group2.remove(list(self.lottery2_result.values())[i][2])

    def get_final_round(self):
        self.group1 += self.group2
        self.get_round_result(1)

    def format_result(self,lis_input):
        output_string=''
        output_string += '\n'
        for i in lis_input :
                output_string += str(i)
                output_string += '\t\t,\t\t'
        output_string +='\n'
        return output_string

    def format_result_dec(self,dic_input):
        output_string=''
        output_string += '\n'
        for i in dic_input.keys() :
                output_string += str(i).strip('()')
                output_string += '\t\t\t\t\t'+str(dic_input[i])
                output_string += '\n'
        return output_string


    def  runCup(self,gui):

        self.divide_teams()
        while len(self.group1) > 1 or len(self.group2) > 1:

            gui.print_in_ouput_box('*************************** Round '+str(len(self.group2)*2)+' ***************************\n')
            if len(self.group1) > 1:

                gui.print_in_ouput_box('------------------ Group 1 ----------------------------')
                gui.print_in_ouput_box(self.format_result(self.group1))
                self.get_round_result(1)
                #print(self.lottery1)
                gui.print_in_ouput_box('------------------ Matches -----------------------------')
                gui.print_in_ouput_box(self.format_result(self.lottery1))
                #print(self.lottery1_result)
                gui.print_in_ouput_box('------------------ Results    ----------------------------')
                gui.print_in_ouput_box(self.format_result_dec(self.lottery1_result))
            if len(self.group2) > 1:
                gui.print_in_ouput_box('------------------ Group 2  -----------------------------')
                gui.print_in_ouput_box(self.format_result(self.group2))
                self.get_round_result(2)
                gui.print_in_ouput_box('------------------ Matches -----------------------------')
                gui.print_in_ouput_box(self.format_result(self.lottery2))
                gui.print_in_ouput_box('------------------ Results    ----------------------------')
                gui.print_in_ouput_box(self.format_result_dec(self.lottery2_result))
        self.get_final_round()
        #print('The final : ', self.lottery1)
        gui.print_in_ouput_box('*************************** The final ***************************\n')
        gui.print_in_ouput_box(self.format_result(self.lottery1))
        gui.print_in_ouput_box('------------------ Results    ----------------------------\n')
        gui.print_in_ouput_box(self.format_result_dec(self.lottery1_result))
        gui.print_in_ouput_box('------------------ The Winner ----------------------------\n')
        gui.print_in_ouput_box(self.group1[0])
