# team 10
# abdalla mahmoud ibrahim  70
# eslam mamdoauh mohamed  27
# mohamed eid rehab        111
# hossam fathi mahmoud    40
from controller.cup_controller import CupController
from controller.league_controller import LeagueController
from controller.world_cup_controller import WorldCupController
from view.gui import Gui

# Read names of teams and rate of every team  from file
# and sorted it depended on rate
teams_dic = [line.strip().split(',') for line in open('teams')]
teams_dic = [k for k in sorted(teams_dic, key=lambda item: (item[1]), reverse=True)]
teams_name = [i[0] for i in teams_dic]

# Create objects for league,cup,world cup and gui
league     = LeagueController(teams_name)
cup        = CupController(teams_name)
world_cup  = WorldCupController(teams_name)
gui = Gui()


# function run to league button
def league_function():
    data_output = league.runLeague()
    gui.delet_output_box()
    gui.print_in_ouput_box(data_output)
    gui.creat_league_lable()


# function run to cup button
def cup_function():

    gui.creat_cup_lable()
    gui.delet_output_box()
    cup.runCup(gui)


# function run to world cup button
def world_cup_function():
    gui.creat_world_cup_lable()
    gui.delet_output_box()
    world_cup.run_world_cup(gui)


# create gui
gui.create_start_main_window()
gui.create_league_button(league_function)
gui.create_cup_button(cup_function)
gui.create_world_cup_button(world_cup_function)
gui.create_output_box()
gui.create_main_window()
