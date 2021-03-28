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
DROP TABLE IF EXISTS nonredundant;
DROP TABLE IF EXISTS modified;
DROP TABLE IF EXISTS modPDB;
DROP TABLE IF EXISTS raw;
DROP TABLE IF EXISTS rawPDB;


CREATE TABLE tcrs (
	pdbID VARCHAR(4) NOT NULL PRIMARY KEY
);

CREATE TABLE clustered (
	pdbID VARCHAR(4) NOT NULL
);

CREATE TABLE nonredundant (
	pdbID VARCHAR(4) NOT NULL
);

CREATE TABLE modified (
	user VARCHAR(100) NOT NULL,
	mods VARCHAR(1000) NOT NULL
);

CREATE TABLE modPDB (
	pdbID_mod VARCHAR(4) NOT NULL,
	tempID VARCHAR(100) NOT NULL,
	resolution FLOAT,
	tcr_alpha CHAR(1),
	tcr_beta CHAR(1),
	peptide CHAR(1),
	mhc CHAR(1),
	PRIMARY KEY(pdbID_mod, tempID)
);

CREATE TABLE raw (
	pdbID_raw VARCHAR(4) NOT NULL PRIMARY KEY,
	resolution FLOAT NOT NULL,
        tcr_alpha CHAR(1),
        tcr_beta CHAR(1),
        peptide CHAR(1),
        mhc CHAR(1)
);
