-- Name: Austin Seamann
-- EMAIL: aseamann@unomaha.edu
-- Class: BIOI 4870/CSCI 8876, Spring 2021
--
-- Honor Pledge: On my honor as a student of the University of Neraska at
-- Omaha, I have neither given nor received unauthorized help on
-- this programming assignment.
--
-- Partners: NONE
--
-- Sources: NONE

USE aseamann;

DROP TABLE IF EXISTS tcrs;
DROP TABLE IF EXISTS clustered;
DROP TABLE IF EXISTS tcr2mod;
DROP TABLE IF EXISTS modPDB;
DROP TABLE IF EXISTS tcr2raw;
DROP TABLE IF EXISTS rawPDB;


CREATE TABLE tcrs (
	pdbID VARCHAR(4) NOT NULL,
	percentID INT NOT NULL,
	modID INT NOT NULL
);

CREATE TABLE clustered (
	percentID INT NOT NULL,
	clust INT,
	pdbID VARCHAR(4)
);

CREATE TABLE tcr2raw {
	modID INT NOT NULL,
	pdbID_mod VARCHAR(8) NOT NULL,
	tempID int NOT NULL
};

CREATE TABLE modPDB (
	pdbID_mod VARCHAR(8) NOT NULL,
	tempID int NOT NULL,
	all_chains  BOOLEAN,
	trimmed  BOOLEAN,
	tcr_only BOOLEAN,
	p_only BOOLEAN,
	mhc_only BOOLEAN,
	renum BOOLEAN,
	PRIMARY KEY(pdbID_mod, tempID)
);

CREATE TABLE tcr2raw {
	pdbID VARCHAR(4) NOT NULL,
	pdbID_raw VARCHAR(4) NOT NULL
};

CREATE TABLE rawPDB (
	pdbID_raw VARCHAR(4) NOT NULL PRIMARY KEY,
	resolution FLOAT NOT NULL,
	tcr_alpha CHAR(1),
	tcr_beta CHAR(1),
	peptide CHAR(1),
	mhc CHAR(1)
);

