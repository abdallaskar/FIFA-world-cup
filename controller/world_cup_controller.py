from controller.cup_controller import CupController
from controller.league_controller import LeagueController
from view.gui import Gui


class WorldCupController:

    def __init__(self, teams):
        self.teams = teams
        self.groups = []
        self.groups_result = []
        self.groups_result_st = ''
        self.groups_result_str = ''
        self.groups_str = ''

    def get_groups(self):
        hold = self.teams
        for i in range (len(hold)//4):
            group = [hold[i],hold[i+8],hold[i+16],hold[i+24]]
            self.groups.append(group)




        j = 1
        for i in self.groups:
            self.groups_str += 'group : {:2d}'.format(j) + '  ' + str(i)
            self.groups_str += '\n'
            j += 1

    def get_groupsRound_result(self, gui):
        for i in range(len(self.groups)):
            leagueController = LeagueController(self.groups[i])
            leagueController.get_lottery()
            leagueController.get_matches_result()
            self.groups_result_str += 'Group' + str(i + 1) + ' : result \n' + str(leagueController.get_league_result())
            self.groups_result_str += '\n'
            hold = list(leagueController.leagueResult.keys())
            self.groups_result.append(hold[0])
            self.groups_result_st += str(hold[0]) + '\t\t\t\t\t'
            self.groups_result_st += str(hold[1]) + '\t\t\n'
            self.groups_result.append(hold[1])

    def get_cupsRound_result(self, gui):
        cup = CupController(self.groups_result)
        cup.runCup(gui)
        pass

    def run_world_cup(self, gui):

        self.get_groups()
        # print(self.groups)
        gui.print_in_ouput_box('************************ World Cup group stage ***************************\n')
        gui.print_in_ouput_box(self.groups_str)
        gui.print_in_ouput_box('\n')
        self.get_groupsRound_result(gui)
        gui.print_in_ouput_box('************************ World Cup group stage result *********************\n')
        gui.print_in_ouput_box(self.groups_result_str)
        # print(self.groups_result)
        gui.print_in_ouput_box('\n')
        gui.print_in_ouput_box('************************  Qualified  teams *******************\n')
        gui.print_in_ouput_box(str(self.groups_result_st))
        gui.print_in_ouput_box('\n')
        self.get_cupsRound_result(gui)
        self.groups = []
        self.groups_result = []
        self.groups_result_st = ''
        self.groups_result_str = ''
        self.groups_str = ''
