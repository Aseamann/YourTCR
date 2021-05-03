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
import argparse

# Parses over arugments, details in help statements
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rawPDB', help="rawPDB_id", type=str)
    parser.add_argument('--modPDB', help="modPDB_Id", type=str)
    parser.add_argument("--renum", help="Updates numbering of TCR for docking", default=False, action="store_true")
    parser.add_argument("--all", help="All chains", default=False, action="store_true")
    parser.add_argument("--trim", help="Trim TCR chains to only contain variable region", default=False,
                        action="store_true")
    parser.add_argument("--mhc_split", help="Only provide MHC chains", default=False, action="store_true")
    parser.add_argument("--peptide_split", help="Only provide MHC chains", default=False, action="store_true")
    parser.add_argument("--tcr_split", help="Only provide TCR chains", default=False, action="store_true")
    return parser.parse_args()

def main():
    args = parser_args()
    # Moves over raw pdb to be editted
    os.copy('/home/aseamann/public_html/rawPDBs/' + args.rawPDB + ".pdb", '/home/aseamann/public_html/modPDBs/' + args.modPDB + ".pdb")
    # Submits pdb to PdbTools3
    pdb = PdbTools3('/home/aseamann/public_html/modPDBs/' +args.modPDB)
    all_chains = "FALSE"
    trimmed = "FALSE"
    tcr_only = "FALSE"
    p_only = "FALSE"
    mhc_only = "FALSE"
    renum = "FALSE"
    # Based on arguments passed, updated T/F for if the chain still remains in file
    if args.mhc_split:
        pdb.split_mhc()
        mhc_only = "TRUE"
    elif args.trim:
        pdb.clean_tcr_count_trim()
        trimmed = "TRUE"
        tcr_alpha = "TRUE"
        tcr_beta = "TRUE"
        renum = "TRUE"
    elif args.tcr_split:
        pdb.clean_tcr()
        tcr_alpha = "TRUE"
        tcr_beta = "TRUE"
    elif args.peptide_split:
        pdb.split_p()
        p_only = "TRUE"
    else:
        all_chains = "TRUE"
    if args.renum:
        pdb.clean_docking_count()
        renum = "TRUE"

    # Dictionary that hold values to be submitted
    pdb_data = {
            'pdbID_mod': args.rawPDB,
            'tempID': args.modPDB,
            'all_chains': all_chains,
            'trimmed': trimmed,
            'tcr_only': tcr_only,
            'peptide': p_only,
            'mhc': mhc_only,
            'renum': renum
    }

    # Writes to sql file that will be submitted to db
    with open('modPDBinsert.sql', 'w') as f:
        f.write('USE aseamann;\n')
        output = "INSERT INTO modPDB(pdbID_mod, tempID, all_chains, trimmed, tcr_only, peptide, mhc, renum) " \
                "VALUES('%(pdbID_mod)s', '%(tempID)s', '%(all_chains)s', '%(trimmed)s', '%(tcr_only)s', '%(peptide)s', '%(mhc)s', '%(renum)s');" % pdb_data
        f.write(output + '\n')
    os.system('mysql< modPDBinsert.sql')  # Submit to MySql
        


if __name__ == '__main__':
    main()
