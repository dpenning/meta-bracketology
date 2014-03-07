import os


paths = ['cbs_sports','sports_illustrated','usa_today','espn']

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
					"Middle Tennessee",
					"Saint Mary's",
					"Oregon",
					"New Mexico State",
					"Valparaiso",
					"Albany",
					"Liberty",
					"North Carolina A&T"]
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
				"Boise State",
				"La Salle",
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
				"James Madison",
				"Long Island"]

teams = midwest_teams + west_teams + south_teams + east_teams
team_values = [[] for a in range(len(teams))]
team_average = [0 for a in range(len(teams))]
team_best = [0 for a in range(len(teams))]
team_worst = [0 for a in range(len(teams))]


for path in paths:
	path_ls = os.listdir(path)
	for fi in path_ls:
		f = open(path+'/'+fi,'r')
		for line in f.readlines():
			if len(line) > 1:
				if line.split('\t')[0] in teams:
					teams_index = teams.index(line.split('\t')[0])
					team_values[teams_index].append(int(line.split('(')[1].split(')')[0]))
		f.close()


for a in range(len(team_values)):
	team_average[a] = float(sum(team_values[a]))/len(team_values[a])
	team_worst[a] = max(team_values[a])
	team_best[a] = min(team_values[a])


f = open('averages.txt','w')

for a in range(len(team_values)):
	f.write(str(teams[a]) + "\t" + str(team_best[a]) + "\t" + str(team_worst[a]) + "\t" + str(team_average[a]) + '\n')
f.close()