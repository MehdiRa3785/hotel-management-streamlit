import sqlite3

conn = sqlite3.connect("hotel.db")
cur = conn.cursor()

# Drop tables if they exist (for reruns)
cur.executescript("""
DROP TABLE IF EXISTS Chambre_Reservation;
DROP TABLE IF EXISTS Prestation_Reservation;
DROP TABLE IF EXISTS Evaluation;
DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Chambre;
DROP TABLE IF EXISTS Type_Chambre;
DROP TABLE IF EXISTS Prestation;
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS Hotel;
""")

# Create tables
cur.executescript("""
CREATE TABLE Hotel (
    Id_Hotel INTEGER PRIMARY KEY,
    Ville TEXT NOT NULL,
    Pays TEXT NOT NULL,
    Code_postal INTEGER NOT NULL
);

CREATE TABLE Client (
    Id_Client INTEGER PRIMARY KEY,
    Adresse TEXT NOT NULL,
    Ville TEXT NOT NULL,
    Code_postal INTEGER NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Telephone TEXT NOT NULL,
    Nom_complet TEXT NOT NULL
);

CREATE TABLE Type_Chambre (
    Id_Type INTEGER PRIMARY KEY,
    Type TEXT NOT NULL,
    Tarif REAL NOT NULL
);

CREATE TABLE Chambre (
    Id_Chambre INTEGER PRIMARY KEY,
    Numero INTEGER NOT NULL,
    Etage INTEGER NOT NULL,
    Fumeur BOOLEAN NOT NULL,
    Id_Hotel INTEGER NOT NULL,
    Id_Type INTEGER NOT NULL,
    FOREIGN KEY (Id_Hotel) REFERENCES Hotel(Id_Hotel),
    FOREIGN KEY (Id_Type) REFERENCES Type_Chambre(Id_Type)
);

CREATE TABLE Prestation (
    Id_Prestation INTEGER PRIMARY KEY,
    Prix REAL NOT NULL,
    Description TEXT NOT NULL
);

CREATE TABLE Reservation (
    Id_Reservation INTEGER PRIMARY KEY,
    Date_arrivee TEXT NOT NULL,
    Date_depart TEXT NOT NULL,
    Id_Client INTEGER NOT NULL,
    FOREIGN KEY (Id_Client) REFERENCES Client(Id_Client)
);

CREATE TABLE Evaluation (
    Id_Evaluation INTEGER PRIMARY KEY,
    Date_eval TEXT NOT NULL,
    Note INTEGER CHECK (Note BETWEEN 1 AND 5),
    Commentaire TEXT,
    Id_Client INTEGER NOT NULL,
    FOREIGN KEY (Id_Client) REFERENCES Client(Id_Client)
);

CREATE TABLE Chambre_Reservation (
    Id_Chambre INTEGER NOT NULL,
    Id_Reservation INTEGER NOT NULL,
    PRIMARY KEY (Id_Chambre, Id_Reservation),
    FOREIGN KEY (Id_Chambre) REFERENCES Chambre(Id_Chambre),
    FOREIGN KEY (Id_Reservation) REFERENCES Reservation(Id_Reservation)
);

CREATE TABLE Prestation_Reservation (
    Id_Prestation INTEGER NOT NULL,
    Id_Reservation INTEGER NOT NULL,
    PRIMARY KEY (Id_Prestation, Id_Reservation),
    FOREIGN KEY (Id_Prestation) REFERENCES Prestation(Id_Prestation),
    FOREIGN KEY (Id_Reservation) REFERENCES Reservation(Id_Reservation)
);
""")

# Insert data (abbreviated for brevity, but you'll paste all the rows here)
cur.executescript("""
INSERT INTO Hotel VALUES
(1, 'Paris', 'France', 75001),
(2, 'Lyon', 'France', 69002);

INSERT INTO Client VALUES
(1, '12 Rue de Paris', 'Paris', 75001, 'jean.dupont@email.fr', '0612345678', 'Jean Dupont'),
(2, '5 Avenue Victor Hugo', 'Lyon', 69002, 'marie.leroy@email.fr', '0623456789', 'Marie Leroy'),
(3, '8 Boulevard Saint-Michel', 'Marseille', 13005, 'paul.moreau@email.fr', '0634567890', 'Paul Moreau'),
(4, '27 Rue Nationale', 'Lille', 59800, 'lucie.martin@email.fr', '0645678901', 'Lucie Martin'),
(5, '3 Rue des Fleurs', 'Nice', 06000, 'emma.giraud@email.fr', '0656789012', 'Emma Giraud');

INSERT INTO Type_Chambre VALUES
(1, 'Simple', 80),
(2, 'Double', 120);

INSERT INTO Chambre VALUES
(1, 201, 2, 0, 1, 1),
(2, 502, 5, 1, 1, 2),
(3, 305, 3, 0, 2, 1),
(4, 410, 4, 0, 2, 2),
(5, 104, 1, 1, 2, 2),
(6, 202, 2, 0, 1, 1),
(7, 307, 3, 1, 1, 2),
(8, 101, 1, 0, 1, 1);

INSERT INTO Prestation VALUES
(1, 15, 'Petit-déjeuner'),
(2, 30, 'Navette aéroport'),
(3, 0, 'Wi-Fi gratuit'),
(4, 50, 'Spa et bien-être'),
(5, 20, 'Parking sécurisé');

INSERT INTO Reservation VALUES
(1, '2025-06-15', '2025-06-18', 1),
(2, '2025-07-01', '2025-07-05', 2),
(3, '2025-08-10', '2025-08-14', 3),
(4, '2025-09-05', '2025-09-07', 4),
(5, '2025-09-20', '2025-09-25', 5),
(7, '2025-11-12', '2025-11-14', 2),
(9, '2026-01-15', '2026-01-18', 4),
(10, '2026-02-01', '2026-02-05', 2);

INSERT INTO Evaluation VALUES
(1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 1),
(2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 2),
(3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 3),
(4, '2025-09-05', 5, 'Service impeccable, je recommande.', 4),
(5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 5);

INSERT INTO Chambre_Reservation VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (7, 7), (8, 9), (6, 10);

INSERT INTO Prestation_Reservation VALUES
(1, 1), (3, 1), (1, 2), (2, 2), (3, 3), (1, 4), (5, 4), (1, 5), (4, 5);
""")

conn.commit()
conn.close()
print("Database initialized.")
