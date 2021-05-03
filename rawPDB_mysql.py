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
# Sources: NONE
import sys
import os
from PDB_Tools_V3 import PdbTools3 as tool


def main():
    # Preparing SQL query for inserting raw PDB info
    pdb_data = {
        'pdbID_raw': "NULL", 
        'resolution': 3.0, 
        'tcr_alpha': 'D', 
        'tcr_beta': 'E', 
        'peptide': 'C', 
        'mhc': 'A'
    }
    
    # Gather directories
    current_dir = os.path.dirname(os.path.realpath(__file__))
    raw_dir = current_dir + '/public_html/rawPDBs/'

    # Creates sql file that will be submitted to MySql
    with open('rawPDBinsert.sql', 'w') as f:
        f.write('USE aseamann;\n')
        for pdb in sorted(os.listdir(raw_dir)):
                if pdb.endswith(".pdb"):
                    pdb1 = tool(raw_dir + pdb)
                    resolution = pdb1.get_resolution()
                    tcr_chains = pdb1.get_tcr_chains()
                    mhc = pdb1.get_mhc_chain()
                    peptide = pdb1.get_peptide_chain()

                    pdb_data['pdbID_raw'] = pdb[:4]
                    pdb_data['resolution'] = resolution
                    pdb_data['tcr_alpha'] = tcr_chains['ALPHA']
                    pdb_data['tcr_beta'] = tcr_chains['BETA']
                    pdb_data['peptide'] = peptide
                    pdb_data['mhc'] = mhc
                    
                    # writing line
                    output = "INSERT INTO rawPDB(pdbID_raw, resolution, tcr_alpha, tcr_beta, peptide, mhc) " \
                        "VALUES('%(pdbID_raw)s', %(resolution)s, '%(tcr_alpha)s', '%(tcr_beta)s', '%(peptide)s', '%(mhc)s');" % pdb_data
                    f.write(output + '\n')
    os.system('mysql< rawPDBinsert.sql')  # Submit to MySql


if __name__ == '__main__':
    main()


