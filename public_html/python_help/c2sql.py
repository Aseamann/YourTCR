# Name: Austin Seamann
# EMAIL: aseamann@unomaha.edu
# Class: BIOI 4870/CSCI 8876, Spring 2021
#
# Honor Pledge: On my honor as a student of the University of Neraska at
# Omaha, I have neither given nor received unauthorized help on
# this programming assignment.
#
# Partners: NONE
#
#Sources: NONE
import os
import sys


class C2Sql:
	def main():
		directory = os.getcwd()  # Current working directory
		total = {}  # Dictionary of all values in clusters [%][cluster#][pdb]
		for cluster in os.listdir(directory):
			if cluster.endswith('.clstr'):  # Only grabs cluster files
				identity = cluster.split('.')[0][-2:]  # Grabs percent identity
				with open(cluster, "r") as f:  # Opens cluster file
					cluster_dic = {}  # Dictionary of clusters [cluster#][pdbID]
					temp_cluster = -1
					for line in f:
                                                # Grabbing information from clusters
						if line[0] == ">":
							temp_cluster = int(line.split(' ')[1])
							cluster_dic[temp_cluster] = []
						else:
							pdb = line.split('>')[1][:4]
							cluster_dic[temp_cluster].append(pdb)
					total[identity] = cluster_dic
                # Opening file to be submitted to db
		with open("clusterPDBinsert.sql", "w") as f1:
			f1.write("USE aseamann;\n")
			for percent in total:
				for cluster in total[percent]:
					for pdb in total[percent][cluster]:
                                                insert_stm = 'INSERT INTO clustered(percentID, clust, pdbID) '
                                                insert_stm += f'VALUES({percent}, {cluster}, "{pdb}");'
                                                insert_stm += '\n'
                                                f1.write(insert_stm)
		os.system("mysql< clusterPDBinsert.sql")  # Submitting file to MySql

	if __name__ == '__main__':
		main()
