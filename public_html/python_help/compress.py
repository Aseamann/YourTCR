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
import os
import sys
import subprocess

def main():
    pdb_dir = 'rawPDBs'
    filename = 'rawPDBs.tar.gz'
    os.chdir('/home/aseamann/public_html')  # Setting directory
    subprocess.run(['rm', '-r', filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # Removes previous compressed file
    subprocess.run(['tar', '-czvf', filename, pdb_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # Compress
    print('/~aseamann/' + filename)  # Return result

if __name__=='__main__':
    main()

