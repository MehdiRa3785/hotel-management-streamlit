-- hotel_db_creation.sql
CREATE DATABASE IF NOT EXISTS hotel_management;
USE hotel_management;

-- Hotel table
CREATE TABLE Hotel (
    Id_Hotel INT AUTO_INCREMENT PRIMARY KEY,
    Ville VARCHAR(50) NOT NULL,
    Pays VARCHAR(50) NOT NULL,
    Code_postal INT NOT NULL
);

-- Client table
CREATE TABLE Client (
    Id_Client INT AUTO_INCREMENT PRIMARY KEY,
    Adresse VARCHAR(100) NOT NULL,
    Ville VARCHAR(50) NOT NULL,
    Code_postal INT NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Telephone VARCHAR(15) NOT NULL,
    Nom_complet VARCHAR(100) NOT NULL
);

-- Type_Chambre table
CREATE TABLE Type_Chambre (
    Id_Type INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(50) NOT NULL,
    Tarif DECIMAL(10,2) NOT NULL
);

-- Chambre table
CREATE TABLE Chambre (
    Id_Chambre INT AUTO_INCREMENT PRIMARY KEY,
    Numero INT NOT NULL,
    Etage INT NOT NULL,
    Fumeur BOOLEAN NOT NULL,
    Id_Hotel INT NOT NULL,
    Id_Type INT NOT NULL,
    FOREIGN KEY (Id_Hotel) REFERENCES Hotel(Id_Hotel),
    FOREIGN KEY (Id_Type) REFERENCES Type_Chambre(Id_Type)
);

-- Prestation table
CREATE TABLE Prestation (
    Id_Prestation INT AUTO_INCREMENT PRIMARY KEY,
    Prix DECIMAL(10,2) NOT NULL,
    Description VARCHAR(100) NOT NULL
);

-- Reservation table
CREATE TABLE Reservation (
    Id_Reservation INT AUTO_INCREMENT PRIMARY KEY,
    Date_arrivee DATE NOT NULL,
    Date_depart DATE NOT NULL,
    Id_Client INT NOT NULL,
    FOREIGN KEY (Id_Client) REFERENCES Client(Id_Client)
);

-- Evaluation table
CREATE TABLE Evaluation (
    Id_Evaluation INT AUTO_INCREMENT PRIMARY KEY,
    Date_eval DATE NOT NULL,
    Note INT CHECK (Note BETWEEN 1 AND 5),
    Commentaire TEXT,
    Id_Client INT NOT NULL,
    FOREIGN KEY (Id_Client) REFERENCES Client(Id_Client)
);

-- Chambre_Reservation junction table
CREATE TABLE Chambre_Reservation (
    Id_Chambre INT NOT NULL,
    Id_Reservation INT NOT NULL,
    PRIMARY KEY (Id_Chambre, Id_Reservation),
    FOREIGN KEY (Id_Chambre) REFERENCES Chambre(Id_Chambre),
    FOREIGN KEY (Id_Reservation) REFERENCES Reservation(Id_Reservation)
);

-- Prestation_Reservation junction table
CREATE TABLE Prestation_Reservation (
    Id_Prestation INT NOT NULL,
    Id_Reservation INT NOT NULL,
    PRIMARY KEY (Id_Prestation, Id_Reservation),
    FOREIGN KEY (Id_Prestation) REFERENCES Prestation(Id_Prestation),
    FOREIGN KEY (Id_Reservation) REFERENCES Reservation(Id_Reservation)
);