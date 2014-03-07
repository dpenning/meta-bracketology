import sys

f = open('averages.txt','r')
teams_list = {}
for a in f.readlines():
	c = a.split('\t')
	teams_list[str(c[0])] = (int(c[1]),int(c[2]),float(c[4].replace('\n','')))

#build the bracket
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
					["Middle Tennessee",
					"Saint Mary's"],
					"Oregon",
					"New Mexico State",
					"Valparaiso",
					"Albany",
					["Liberty",
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
				["Boise State",
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

confs = [midwest_teams,west_teams,south_teams,east_teams]

bad_teams = []

bracket_history = []


bracket_history_new = []
for a in confs:
	for b in a:
		if 'list' in str(type(b)):
			for c in b:
				bracket_history_new.append(c)
		else:
			bracket_history_new.append(b)
bracket_history.append(bracket_history_new)




bracket_history_new = []
#EZ matchups
for c in range(len(confs)):
	for d in range(len(confs[c])):
		if 'list' in str(type(confs[c][d])):
			team1,team2 = confs[c][d][0],confs[c][d][1]
			bad_teams.append(team1)
			bad_teams.append(team2)
			if teams_list[team1][2] > teams_list[team2][2]:
				winning_team = team2
			else:
				winning_team = team1
			confs[c][d] = winning_team
			bracket_history_new.append(winning_team)

save_confs = confs[:]

bracket_history.append(midwest_teams+west_teams+south_teams+east_teams)

bracket_history_new = []
#round 1
for c in range(len(confs)):
	new_conference = []
	starting_matchups = [(1,16),(8,9),(5,12),(4,13),(6,11),(3,14),(7,10),(2,15)]
	for a in starting_matchups:
		team1 = confs[c][a[0]-1]
		team2 = confs[c][a[1]-1]
		if teams_list[team1][2] > teams_list[team2][2]:
			winning_team = team2
		else:
			winning_team = team1
		new_conference.append(winning_team)
		bracket_history_new.append(winning_team)
	confs[c] = new_conference
bracket_history.append(bracket_history_new)

bracket_history_new = []
#round 2
for c in range(len(confs)):
	new_conference = []
	starting_matchups = [(1,2),(3,4),(5,6),(7,8)]
	for a in starting_matchups:
		team1 = confs[c][a[0]-1]
		team2 = confs[c][a[1]-1]
		if teams_list[team1][2] > teams_list[team2][2]:
			winning_team = team2
		else:
			winning_team = team1
		new_conference.append(winning_team)
		bracket_history_new.append(winning_team)
	confs[c] = new_conference
bracket_history.append(bracket_history_new)

bracket_history_new = []
#round 3
for c in range(len(confs)):
	new_conference = []
	starting_matchups = [(1,2),(3,4)]
	for a in starting_matchups:
		team1 = confs[c][a[0]-1]
		team2 = confs[c][a[1]-1]
		if teams_list[team1][2] > teams_list[team2][2]:
			winning_team = team2
		else:
			winning_team = team1
		new_conference.append(winning_team)
		bracket_history_new.append(winning_team)
	confs[c] = new_conference
bracket_history.append(bracket_history_new)

bracket_history_new = []
#round 4
for c in range(len(confs)):
	new_conference = []
	starting_matchups = [(1,2)]
	for a in starting_matchups:
		team1 = confs[c][a[0]-1]
		team2 = confs[c][a[1]-1]
		if teams_list[team1][2] > teams_list[team2][2]:
			winning_team = team2
		else:
			winning_team = team1
		new_conference.append(winning_team)
		bracket_history_new.append(winning_team)
	confs[c] = new_conference
bracket_history.append(bracket_history_new)

bracket_history_new = []
#final 4
bracket_history_new = []
final_conference = []
team1 = confs[0][0]
team2 = confs[1][0]
if teams_list[team1][2] > teams_list[team2][2]:
	winning_team = team2
else:
	winning_team = team1
bracket_history_new.append(winning_team)
final_conference.append(winning_team)
team1 = confs[2][0]
team2 = confs[3][0]
if teams_list[team1][2] > teams_list[team2][2]:
	winning_team = team2
else:
	winning_team = team1
bracket_history_new.append(winning_team)
final_conference.append(winning_team)
bracket_history.append(bracket_history_new)

#final Game
bracket_history_new = []
team1 = final_conference[0]
team2 = final_conference[1]
if teams_list[team1][2] > teams_list[team2][2]:
	winning_team = team2
else:
	winning_team = team1
bracket_history_new.append(winning_team)
bracket_history.append(bracket_history_new)


#count = 0
#for a in bracket_history:
#	print("-------- Round "+ str(count) +"---------")
#	for b in a:
#		print ('\t'+str(b))
#	print("------------"+ str( len(a) ) +"--------------")
#	count += 1



def m(s,i=50):
	if len(s)>i:
		return s[:i]
	return s

def print_bracket(offset=48):
	r1 = [""] + bracket_history[1][offset:offset+16]
	r2 = [""] + bracket_history[2][(offset)//2:((offset+16)//2)]
	r3 = [""] + bracket_history[3][(offset)//4:((offset+16)//4)]
	r4 = [""] + bracket_history[4][(offset)//8:((offset+16)//8)]
	r5 = [""] + bracket_history[5][(offset)//16:((offset+16)//16)]


	starting_matchups = [(1,16),(8,9),(5,12),(4,13),(6,11),(3,14),(7,10),(2,15)]

	space = "\t\t"

	print(m(r1[1]))
	print(space+m(r2[1]))
	print(m(r1[16]))
	print(space+space+m(r3[1]))
	print(m(r1[8]))
	print(space+m(r2[2]))
	print(m(r1[9]))
	print(space+space+space+m(r4[1]))
	print(m(r1[5]))
	print(space+m(r2[3]))
	print(m(r1[12]))
	print(space+space+m(r3[2]))
	print(m(r1[4]))
	print(space+m(r2[4]))
	print(m(r1[13]))
	print(space+space+space+space+m(r5[1]))
	print(m(r1[6]))
	print(space+m(r2[5]))
	print(m(r1[11]))
	print(space+space+m(r3[3]))
	print(m(r1[3]))
	print(space+m(r2[6]))
	print(m(r1[14]))
	print(space+space+space+m(r4[2]))
	print(m(r1[7]))
	print(space+m(r2[7]))
	print(m(r1[10]))
	print(space+space+m(r3[4]))
	print(m(r1[2]))
	print(space+m(r2[8]))
	print(m(r1[15]))








print_bracket()





