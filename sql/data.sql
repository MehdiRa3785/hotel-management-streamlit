-- hotel_data_insertion.sql
USE hotel_management;

-- Insert Hotels
INSERT INTO Hotel (Id_Hotel, Ville, Pays, Code_postal) VALUES
(1, 'Paris', 'France', 75001),
(2, 'Lyon', 'France', 69002);

-- Insert Clients
INSERT INTO Client (Id_Client, Adresse, Ville, Code_postal, Email, Telephone, Nom_complet) VALUES
(1, '12 Rue de Paris', 'Paris', 75001, 'jean.dupont@email.fr', '0612345678', 'Jean Dupont'),
(2, '5 Avenue Victor Hugo', 'Lyon', 69002, 'marie.leroy@email.fr', '0623456789', 'Marie Leroy'),
(3, '8 Boulevard Saint-Michel', 'Marseille', 13005, 'paul.moreau@email.fr', '0634567890', 'Paul Moreau'),
(4, '27 Rue Nationale', 'Lille', 59800, 'Lucie.martin@email.fr', '0645678901', 'Lucie Martin'),
(5, '3 Rue des Fleurs', 'Nice', 06000, 'emma.giraud@email.fr', '0656789012', 'Emma Giraud');

-- Insert Type_Chambre
INSERT INTO Type_Chambre (Id_Type, Type, Tarif) VALUES
(1, 'Simple', 80),
(2, 'Double', 120);

-- Insert Chambres
INSERT INTO Chambre (Id_Chambre, Numero, Etage, Fumeur, Id_Hotel, Id_Type) VALUES
(1, 201, 2, 0, 1, 1),
(2, 502, 5, 1, 1, 2),
(3, 305, 3, 0, 2, 1),
(4, 410, 4, 0, 2, 2),
(5, 104, 1, 1, 2, 2),
(6, 202, 2, 0, 1, 1),
(7, 307, 3, 1, 1, 2),
(8, 101, 1, 0, 1, 1);

-- Insert Prestations
INSERT INTO Prestation (Id_Prestation, Prix, Description) VALUES
(1, 15, 'Petit-déjeuner'),
(2, 30, 'Navette aéroport'),
(3, 0, 'Wi-Fi gratuit'),
(4, 50, 'Spa et bien-être'),
(5, 20, 'Parking sécurisé');

-- Insert Reservations
INSERT INTO Reservation (Id_Reservation, Date_arrivee, Date_depart, Id_Client) VALUES
(1, '2025-06-15', '2025-06-18', 1),
(2, '2025-07-01', '2025-07-05', 2),
(3, '2025-08-10', '2025-08-14', 3),
(4, '2025-09-05', '2025-09-07', 4),
(5, '2025-09-20', '2025-09-25', 5),
(7, '2025-11-12', '2025-11-14', 2),
(9, '2026-01-15', '2026-01-18', 4),
(10, '2026-02-01', '2026-02-05', 2);

-- Insert Evaluations
INSERT INTO Evaluation (Id_Evaluation, Date_eval, Note, Commentaire, Id_Client) VALUES
(1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 1),
(2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 2),
(3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 3),
(4, '2025-09-05', 5, 'Service impeccable, je recommande.', 4),
(5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 5);

-- Insert Chambre_Reservation (assign rooms to reservations)
INSERT INTO Chambre_Reservation (Id_Chambre, Id_Reservation) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (7, 7), (8, 9), (6, 10);

-- Insert Prestation_Reservation (assign services to reservations)
INSERT INTO Prestation_Reservation (Id_Prestation, Id_Reservation) VALUES
(1, 1), (3, 1), (1, 2), (2, 2), (3, 3), (1, 4), (5, 4), (1, 5), (4, 5);