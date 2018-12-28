import numpy as np
from matplotlib import pyplot as plt
class player_average:
	def calc_avg(self,player_list,names):
		total_runs_scored=[]
		for indv_player in names:
			run_scored=[]
			print(indv_player)
			for a,b,c in player_list[1:]:
				if b==indv_player:
					p,q,r,s=map(int,c.strip().split(' ')[:4])
					run_scored.append(p)
				else:
					continue
			total_runs_scored.append(sum(run_scored))
		return total_runs_scored
	def plot_grph(self,player_names, totalrunscored):
		plt.figure(figsize=(20, 10))
		y_pos = np.arange(len(player_names)) 
		plt.bar(y_pos, totalrunscored, align='center', alpha=1)
		plt.xticks(y_pos, player_names)
		plt.ylabel('Scores')
		plt.xlabel('Player-wise')
		plt.title('Indian Cricket Score analysis')
		plt.show()

file_name=open("D:\Python\performance-of-cricket-players\Performance.txt",'r')
temp=''
player_list=[]
for i in file_name:
    player_list.append(i.replace('\n','').split('"'))
curr_player= (b for a,b,c in  player_list[1:])
player_names=sorted(set(curr_player))
obj_player=player_average()
out=obj_player.calc_avg(player_list,player_names)
obj_player.plot_grph(player_names,out)
