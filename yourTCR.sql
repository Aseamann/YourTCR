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
	pdbID VARCHAR() NOT NULL PRIMARY KEY
);

CREATE TABLE clustered (
	pdbID VARCHAR() NOT NULL
);

CREATE TABLE nonredundant (
	pdbID VARCHAR() NOT NULL
);

CREATE TABLE modified (
	user VARCHAR() NOT NULL,
	mods VARCHAR() NOT NULL
);

CREATE TABLE modPDB (
	pdbID_mod VARCHAR() NOT NULL PRIMARY KEY,
	tempID VARCHAR() NOT NULL PRIMARY KEY,
	resolution FLOAT,
	tcr_alpha VARCHAR(),
	tcr_beta VARCHAR(),
	peptide VARCHAR(),
	mhc VARCHAR()
);

CREATE TABLE raw (
	pdbID_raw VARCHAR() NOT NULL PRIMARY KEY,
	resolution FLOAT NOT NULL,
        tcr_alpha VARCHAR(),
        tcr_beta VARCHAR(),
        peptide VARCHAR(),
        mhc VARCHAR()
);
