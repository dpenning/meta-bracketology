# goes
# Midwest -> West -> South -> East
import os
def clear():
	#clear
	os.system("clear")
def print_all():
	for i in range(len(conferences)):
		for j in range(len(conferences[i])):
				print (j,":",str(conferences[i][j]))
	input("Continue")
def get_team_placement(team):
	clear()
	round_names = ['Prelim(68)','Round 1(64)','Round 2(32)','Sweet 16(16)','Elite 8(8)','Final Four(4)','Championship(2)','Winner(1)']
	print(str(team))
	print("-----------")
	for a in range(len(round_names)):
		print (a,":",round_names[a])
	return int(input("Which Round Did The Lose?: "))
def tiebreaker():
	clear()
	print("TieBreaker")
	print("----------")
	i = str(input("Score (1 comma): "))
	return [int(x) for x in i.split(',')]

website_list = ["cbs_sports",
				"usa_today",
				"sports_illustrated",
				"espn",
				"_test_"]
midwest_teams = [	"Louisville",
					"Duke",
					"Michigan State",
					"Saint Louis",
					"Oklahoma State",
					"Memphis",
					"Creighton",
					"Colorado State",
					"Missouri",
					"Cincinnati",
					[ "Middle Tennessee",
					  "Saint Mary's"],
					"Oregon",
					"New Mexico State",
					"Valparaiso",
					"Albany",
					[ "Liberty",
					  "North Carolina A&T"]]
west_teams = [	"Gonzaga",
				"Ohio State",
				"New Mexico",
				"Kansas State",
				"Wisconsin",
				"Arizona",
				"Notre Dame",
				"Pittsburgh",
				"Wichita State",
				"Iowa State",
				"Belmont",
				"Mississippi",
				[ "Boise State",
				  "La Salle"],
				"Harvard",
				"Iona",
				"Southern"]
south_teams = [	"Kansas",
				"Georgetown",
				"Florida",
				"Michigan",
				"VCU",
				"UCLA",
				"San Diego State",
				"North Carolina",
				"Villanova",
				"Oklahoma",
				"Minnesota",
				"Akron",
				"South Dakota State",
				"Northwestern State",
				"Florida Gulf Coast",
				"Western Kentucky"]
east_teams = [	"Indiana",
				"Miami",
				"Marquette",
				"Syracuse",
				"UNLV",
				"Butler",
				"Illinois",
				"NC State",
				"Temple",
				"Colorado",
				"Bucknell",
				"California",
				"Montana",
				"Davidson",
				"Pacific",
				["James Madison",
				 "Long Island"]]
conferences = [midwest_teams,west_teams,south_teams,east_teams]
round_names = ['Prelim(68)','Round 1(64)','Round 2(32)','Sweet 16(16)','Elite 8(8)','Final Four(4)','Championship(2)','Winner(1)']
for a in range(len(website_list)):
	print(a,":",website_list[a])
which_website = int(input("Which Website: "))
file_path = str(website_list[which_website])
bracket_file_loc = ""
if os.path.isdir(file_path):
	path_ls = os.listdir(file_path)
	count = 0
	while "bracket_" + str(count) + ".txt" in path_ls:
		count += 1
	bracket_file_loc = file_path + '/' + "bracket_" + str(count) + ".txt"
else:
	os.mkdir(file_path)
	bracket_file_loc = file_path + '/' + "bracket_" + str(0) + ".txt"
file_str = ""
for i in range(len(conferences)):
	for j in [11,13,16]:
		j = j - 1
		if 'list' in str(type(conferences[i][j])):
			val = get_team_placement(conferences[i][j][0])
			file_str += conferences[i][j][0] + "\t" + round_names[val] + "\n"
			val = get_team_placement(conferences[i][j][1])
			file_str += conferences[i][j][1] + "\t" + round_names[val] + "\n"
for i in range(len(conferences)):
	for j in [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]:
		j = j - 1
		if 'list' in str(type(conferences[i][j])):
			continue
		val = get_team_placement(conferences[i][j])
		file_str += conferences[i][j] + "\t" + round_names[val] + "\n"
f = open(bracket_file_loc,'w')
f.write(file_str)
f.close()
clear()
print (bracket_file_loc)
