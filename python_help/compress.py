import os
import sys
import subprocess

def main():
    pdb_dir = 'rawPDBs'
    filename = 'rawPDBs.tar.gz'
    os.chdir('/home/aseamann/public_html')
    subprocess.run(['rm', '-r', filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['tar', '-czvf', filename, pdb_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('/~aseamann/' + filename)

if __name__=='__main__':
    main()

