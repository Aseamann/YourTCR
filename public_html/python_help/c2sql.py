import os
import sys


class C2Sql:
	def main():
		directory = os.getcwd()
		total = {}  # Dictionary of all values in clusters [%][cluster#][pdb]
		for cluster in os.listdir(directory):
			if cluster.endswith('.clstr'):
				identity = cluster.split('.')[0][-2:]
				with open(cluster, "r") as f:
					cluster_dic = {}  # Dictionary of clusters [cluster#][pdbID]
					temp_cluster = -1
					for line in f:
						if line[0] == ">":
							temp_cluster = int(line.split(' ')[1])
							cluster_dic[temp_cluster] = []
						else:
							pdb = line.split('>')[1][:4]
							cluster_dic[temp_cluster].append(pdb)
					total[identity] = cluster_dic
		with open("clusterPDBinsert.sql", "w") as f1:
			f1.write("USE aseamann;\n")
			for percent in total:
				for cluster in total[percent]:
					for pdb in total[percent][cluster]:
						insert_stm = f'INSERT INTO clustered({percent}, {cluster}, "{pdb}");\n'
						f1.write(insert_stm)
		os.system("mysql< clusterPDBinsert.sql")

	if __name__ == '__main__':
		main()
