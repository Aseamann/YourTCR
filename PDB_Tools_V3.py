from math import sqrt
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist


class PdbTools3:
    # initialize PdbTools
    def __init__(self, file):
        self.file_name = file
        self.test_list = {}

    # method for changing PDB file
    def set_file_name(self, file_name_in):
        self.file_name = file_name_in

    # Returns file name currently in use
    def get_file_name(self):
        return self.file_name

    # Returns the pdbID of file
    def get_pdb_id(self):
        with open(self.file_name, 'r') as file:
            output = file.readline()
            return output[62:66].lower()

    # Returns a list of all chains in PDB file
    def get_chains(self):
        chains = []
        with open(self.file_name, 'r') as file:
            for line in file:
                if line[0:6] == 'ATOM  ':
                    if not chains.__contains__(line[21]):
                        chains.append(line[21])
        return chains

    # Returns a string of amino acids in a specific chain as a string in single letter notation
    def get_amino_acid_on_chain(self, chain):
        output = ''
        count = 0
        flag = True
        with open(self.file_name, 'r') as file:
            for line in file:
                if line[0:6] == 'ATOM  ':
                    if line[21] == chain:
                        if flag:
                            count = int(line[23:26])
                            flag = False
                        if count == int(line[23:26]):
                            if line[16] != 'B':
                                output += self.three_to_one(line[17:20])
                                count += 1
                        elif count < int(line[23:26]):
                            count = int(line[23:26])
        return output

    # Returns a dictionary for the first atom of a chain.
    def first_atom_on_chain(self, chain):
        with open(self.file_name, 'r') as file:
            for line in file:
                if line[0:6] == 'ATOM  ':
                    if line[21] == chain.upper() and len(line) >= 76:
                        atom = {'atom_num': int(line[6:11]), 'atom_id': line[13:16].strip(),
                                'atom_comp_id': line[17:20],
                                'chain_id': line[21], 'comp_num': int(line[22:26]), 'X': float(line[31:38]),
                                'Y': float(line[38:46]), 'Z': float(line[46:54]), 'occupancy': float(line[55:60]),
                                'B_iso_or_equiv': float(line[60:66]), 'atom_type': line[77]}
                        return atom
                    elif line[21] == chain.upper() and len(line) <= 76:
                        atom = {'atom_num': int(line[6:11]), 'atom_id': line[13:16].strip(),
                                'atom_comp_id': line[17:20],
                                'chain_id': line[21], 'comp_num': int(line[22:26]), 'X': float(line[31:38]),
                                'Y': float(line[38:46]), 'Z': float(line[46:54]), 'occupancy': float(line[55:60])}
                        return atom

    # Converts three letter AA to single letter abbreviation
    def three_to_one(self, three):
        translate = {
            'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'ASX': 'B', 'CYS': 'C', 'GLU': 'E',
            'GLN': 'Q', 'GLX': 'Z', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
            'MET': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y',
            'VAL': 'V'
        }
        for key in translate:
            if three.upper() == key:
                return translate[key]

    # Returns a dictionary with elements related to specific atom number entered
    def get_atom(self, atom_num):
        with open(self.file_name, 'r') as file:
            for line in file:
                if line[0:6] == 'ATOM  ':
                    if int(line[6:11]) == atom_num and len(line) >= 76:
                        atom = {'atom_num': int(line[6:11]), 'atom_id': line[13:16].strip(), 'atom_comp_id': line[17:20],
                                'chain_id': line[21], 'comp_num': int(line[22:26]), 'X': float(line[31:38]),
                                'Y': float(line[38:46]), 'Z': float(line[46:54]), 'occupancy': float(line[55:60]),
                                'B_iso_or_equiv': float(line[60:66]), 'atom_type': line[77]}
                        return atom
                    elif int(line[6:11]) == atom_num and len(line) <= 76:
                        atom = {'atom_num': int(line[6:11]), 'atom_id': line[13:16].strip(),
                                'atom_comp_id': line[17:20],
                                'chain_id': line[21], 'comp_num': int(line[22:26]), 'X': float(line[31:38]),
                                'Y': float(line[38:46]), 'Z': float(line[46:54]), 'occupancy': float(line[55:60])}
                        return atom

    # Returns the Euclidean distance between two atoms based with atom_id being sent in as the parameter
    def euclidean_of_atoms(self, atom_num_1, atom_num_2):
        atom_1 = self.get_atom(atom_num_1)
        atom_2 = self.get_atom(atom_num_2)
        euclidean_distance = sqrt((atom_2['X'] - atom_1['X'])**2 + (atom_2['Y'] - atom_1['Y'])**2
                                  + (atom_2['Z'] - atom_1['Z'])**2)
        return euclidean_distance

    def get_atoms_on_chain(self, chain):
        atoms = []
        with open(self.file_name, 'r') as file:
            for line in file:
                if line[0:6] == 'ATOM  ':
                    if line[21] == chain.upper() and len(line) >= 76:
                        atoms.append({'atom_num': int(line[6:11]), 'atom_id': line[13:16].strip(),
                                'atom_comp_id': line[17:20],
                                'chain_id': line[21], 'comp_num': int(line[22:26]), 'X': float(line[31:38]),
                                'Y': float(line[38:46]), 'Z': float(line[46:54]), 'occupancy': float(line[55:60]),
                                'B_iso_or_equiv': float(line[60:66]), 'atom_type': line[77]})
                    elif line[21] == chain.upper() and len(line) >= 76:
                        atoms.append({'atom_num': int(line[6:11]), 'atom_id': line[13:16].strip(),
                                'atom_comp_id': line[17:20],
                                'chain_id': line[21], 'comp_num': int(line[22:26]), 'X': float(line[31:38]),
                                'Y': float(line[38:46]), 'Z': float(line[46:54]), 'occupancy': float(line[55:60])})
        return atoms

    # Returns alpha and beta chain IDs based on seq. alignment to 1a07 PDB entry chains. Confirms that it is a
    # partnering TCR chain
    def get_tcr_chains(self):
        matrix = matlist.blosum62
        result = {}
        # Hard coded peptide chains for alpha and beta elements of the TCR_file
        alpha_chain = [
            'KEVEQNSGPLSVPEGAIASLNCTYSDRGSQSFFTYRQYSGKSPELIMSIYSNGDKEDGRFTAQLNKASQYVSLLIRDSQPSDSATYLCAVTTDSTGKLQFGAGTQVVVTPDIQNPDPAVYQLRDSKSSDKSVCLFTDFDSQTNVSQSKDSDVYITDKTVLDMRSMDFKSNSAVATSNKSDFACANAFNNSIIPEDTFFPSPESS',
            'QKVTQTQTSISVMEKTTVTMDCVYETQDSSYFLFTYKQTASGEIVFLIRQDSYKKENATVGHYSLNFQKPKSSIGLIITATQIEDSAVYFCAMRGDYGGSGNKLIFGTGTLLSVKP']
        beta_chain = [
            'NAGVTQTPKFQVLKTGQSMTLQCAQDMNHEYMSTYRQDPGMGLRLIHYSVGAGITDQGEVPNGYNVSRSTTEDFPLRLLSAAPSQTSVYFCASRPGLAGGRPEQYFGPGTRLTVTEDLKNVFPPEVAVFEPSEAEISHTQKATLVCLATGFYPDHVELSTTVNGKEVHSGVSTDPQPLKEQPALNDSRYALSSRLRVSATFTQNPRNHFRCQVQFYGLSENDETTQDRAKPVTQIVSAEATGRAD',
            'VTLLEQNPRTRLVPRGQAVNLRCILKNSQYPTMSTYQQDLQKQLQTLFTLRSPGDKEVKSLPGADYLATRVTDTELRLQVANMSQGRTLYCTCSADRVGNTLYFGEGSRLIV']
        chains = self.get_chains()
        tmp_alpha = []
        tmp_beta = []
        for chain in chains:
            score_alpha = pairwise2.align.globaldx(self.get_amino_acid_on_chain(chain), alpha_chain[0], matrix, score_only=True, penalize_end_gaps=(False, False))
            tmp_alpha.append([float(score_alpha), chain])
            score_beta = pairwise2.align.globaldx(self.get_amino_acid_on_chain(chain), beta_chain[0], matrix, score_only=True, penalize_end_gaps=(False, False))
            tmp_beta.append([float(score_beta), chain])
        alpha = sorted(tmp_alpha)
        beta = sorted(tmp_beta)
        result['ALPHA'] = alpha[-1][1]
        result['BETA'] = beta[-1][1]
        atom = self.first_atom_on_chain(result['ALPHA'])
        position = -1
        while True:
            atom2 = self.first_atom_on_chain(result['BETA'])
            distance1 = self.euclidean_of_atoms(atom['atom_num'], atom2['atom_num'])  # Distance between 1st atom in each chain
            distance2 = self.euclidean_of_atoms(atom['atom_num'], atom2['atom_num'] + 125)  # Distance between 1st and 125 atoms in each chain
            if distance1 <= 46 and abs(distance1 - distance2) <= 15:  # Determines if TCR chains are within typical distance.
                self.test_list[self.get_file_name()] = abs(distance1 - distance2)
                result['BETA'] = beta[position][1]
                break
            elif position == (len(beta) * -1):
                print(self.get_file_name() + ' : Possibly does not contain both TCR chains')
                result['BETA'] = beta[-1][1]
                break
            else:
                position -= 1
                result['BETA'] = beta[position][1]
        return result

    # Returns the amino acid sequence of either 'ALPHA' or 'BETA' chain as single letter AA abbreviation
    def get_tcr_amino_seq(self, tcr_type_in):
        tcr_dict = self.get_tcr_chains()
        for key in tcr_dict:
            if key == tcr_type_in:
                return self.get_amino_acid_on_chain(tcr_dict[key])

    # Returns the atoms on the peptide, peptide is determined by smallest chain
    def get_atoms_on_peptide(self):
        atoms = []
        self.set_record_type('ATOM')
        file_atoms = self.record_report().splitlines()
        chain = self.get_peptide_chain()
        for line in file_atoms:
            if line[15] == chain:
                atoms.append(self.get_atom(int(line[0:5])))
        atoms.pop(len(atoms) - 1)
        return atoms

    # Returns the AA chain that is the peptide of the pMHC complex, based on the smallest chain in file
    def get_peptide_chain(self):
        self.set_record_type('SEQRES')
        file_seqres = self.record_report().splitlines()
        lowest = 1000
        chain = ''
        for line in file_seqres:
            if int(line[7:10]) < lowest:
                lowest = int(line[7:10])
                chain = line[4]
        return chain

    # Returns the MHC chain - based on COMPND section labeling HISTOCOMPATIBILITY ANTIGEN
    # WILL LATER CONVERT THIS TO HOW I CHECK FOR TCR CHAINS
    # TODO Also write atoms on mhc
    def get_mhc_chain(self):
        self.set_record_type('COMPND')
        file = self.record_report().splitlines()
        chains = self.get_chains()
        flag = False
        for line in file:
            if flag and line[11] in chains:
                return line[11]
            elif line[4:12] == 'MOLECULE' and line.__contains__('HISTOCOMPATIBILITY ANTIGEN'):
                flag = True

    def renumber_docking(self, rename="****"):
        if rename != '****':  # Renames if given input, if not writes over file
            tcr = rename
        else:
            tcr = self.file_name
        tcr_list = self.get_tcr_chains()
        print(tcr_list)
        atom_count = 1
        res_count = 1
        previous_res_count = 0
        previous_chain = ""
        flag_start_res = False
        file_save = ""
        with open(self.file_name, "r") as f:  # Reads in PDB
            for line in f:
                file_save += line
        with open(tcr, "w") as f1:  # Writes renumbered PDB
            for line in file_save.split("\n"):
                if line[0:6] == 'HEADER':
                    f1.write(line + "\n")
                if line[0:6] == 'ATOM  ':  # Only writes over atoms
                    if line[16] != 'B' and line[26] == ' ':  # Don't allow secondary atoms
                        if line[21] != previous_chain and previous_chain != "":  # Writes TER at end of chain
                            f1.write("TER\n")
                        if not flag_start_res:
                            previous_res_count = int(line[22:26])
                            flag_start_res = True
                        if int(line[22:26]) != previous_res_count:
                            previous_res_count = int(line[22:26])
                            res_count += 1
                        line = line[:22] + str(res_count).rjust(4) + line[26:]  # Replaces res count
                        line = line[:6] + str(atom_count).rjust(5) + line[11:]  # Replaces atom count
                        if line[16] == 'A':
                            line = line[:16] + ' ' + line[17:]
                        previous_chain = line[21]  # Updates previous chain for adding TER
                        atom_count += 1
                        f1.write(line + '\n')
            f1.write("END\n")


if __name__ == '__main__':
    pdb = PdbTools3("Docking/franSession_trimmed.pdb")
    pdb.renumber_docking("Docking/test.pdb")


