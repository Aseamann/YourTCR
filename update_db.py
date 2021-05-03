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


def main():
    current_dir = os.getcwd()
    raw_dir = current_dir + '/public_html/rawPDBs/'
    update_file = 'updateDB.sql'
    os.system('mysql< updateDB.sql')

if __name__ == '__main__':
    main()
