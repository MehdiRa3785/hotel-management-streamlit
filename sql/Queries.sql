-- hotel_queries.sql
USE hotel_management;

-- 3a. Reservations with client name and hotel city
SELECT r.Id_Reservation, c.Nom_complet, h.Ville
FROM Reservation r
JOIN Client c ON r.Id_Client = c.Id_Client
JOIN Chambre_Reservation cr ON r.Id_Reservation = cr.Id_Reservation
JOIN Chambre ch ON cr.Id_Chambre = ch.Id_Chambre
JOIN Hotel h ON ch.Id_Hotel = h.Id_Hotel;

-- 3b. Clients living in Paris
SELECT * FROM Client WHERE Ville = 'Paris';

-- 3c. Reservation count per client
SELECT c.Nom_complet, COUNT(r.Id_Reservation) AS Nombre_reservations
FROM Client c
LEFT JOIN Reservation r ON c.Id_Client = r.Id_Client
GROUP BY c.Id_Client;

-- 3d. Room count per room type
SELECT tc.Type, COUNT(c.Id_Chambre) AS Nombre_chambres
FROM Type_Chambre tc
LEFT JOIN Chambre c ON tc.Id_Type = c.Id_Type
GROUP BY tc.Id_Type;

-- 3e. Available rooms between dates (example: 2025-07-01 to 2025-07-10)
SELECT ch.* 
FROM Chambre ch
WHERE ch.Id_Chambre NOT IN (
    SELECT cr.Id_Chambre
    FROM Reservation r
    JOIN Chambre_Reservation cr ON r.Id_Reservation = cr.Id_Reservation
    WHERE (r.Date_arrivee <= '2025-07-10' AND r.Date_depart >= '2025-07-01')
);