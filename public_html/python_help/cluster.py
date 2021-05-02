import sys
import os
from PDB_Tools_V3 import PdbTools3
import subprocess


class ClusterSeq():
	def main():
		directory = os.getcwd()  # current dir
		pdb_dir = "/".join(directory.split('/')[:-1])  #grabs rawPDB dir
		pdb_dir += "/rawPDBs/"
		fasta_file = 'abTCR.fasta'
		cluster_ids = ['0.70', '0.80', '0.90', '0.99']
		for pdb in os.listdir(pdb_dir):
			if pdb.endswith('.pdb'):
				current_pdb = PdbTools3(pdb_dir + pdb)
				current_pdb.fasta_TCR(fasta_file)
		for cluster_id in cluster_ids:
			output_name = fasta_file.split('.')[0] + str(float(cluster_id) * 100)[:-2]
			subprocess.run(['cd-hit', '-i', fasta_file, '-o', output_name,
				'-c', cluster_id, '-n', '5', '-M', '8000', '-d', '0'])

	if __name__ == '__main__':
		main()

