import sqlite3
import streamlit as st
from datetime import date

# Connect to the SQLite database
conn = sqlite3.connect('hotel.db')
cur = conn.cursor()

st.set_page_config(page_title="Hotel Manager", layout="centered")
st.title("🏨 Hotel Management System")

# Sidebar for navigation
menu = st.sidebar.selectbox("📂 Menu", [
    "View Reservations",
    "View Clients",
    "Available Rooms",
    "Add Client",
    "Add Reservation"
])

# 1. View Reservations
if menu == "View Reservations":
    st.subheader("📋 Reservations")
    query = """
        SELECT r.Id_Reservation, c.Nom_complet AS Client, h.Ville AS Hotel, r.Date_arrivee, r.Date_depart
        FROM Reservation r
        JOIN Client c ON r.Id_Client = c.Id_Client
        JOIN Chambre_Reservation cr ON r.Id_Reservation = cr.Id_Reservation
        JOIN Chambre ch ON cr.Id_Chambre = ch.Id_Chambre
        JOIN Hotel h ON ch.Id_Hotel = h.Id_Hotel
    """
    rows = cur.execute(query).fetchall()
    st.table(rows)

# 2. View Clients
elif menu == "View Clients":
    st.subheader("👤 Clients")
    clients = cur.execute("SELECT Id_Client, Nom_complet, Email, Ville, Telephone FROM Client").fetchall()
    st.table(clients)

# 3. Available Rooms
elif menu == "Available Rooms":
    st.subheader("🛏️ Available Rooms")
    start_date = st.date_input("Start date", date(2025, 7, 1))
    end_date = st.date_input("End date", date(2025, 7, 10))

    if start_date <= end_date:
        query = """
            SELECT * FROM Chambre
            WHERE Id_Chambre NOT IN (
                SELECT cr.Id_Chambre
                FROM Reservation r
                JOIN Chambre_Reservation cr ON r.Id_Reservation = cr.Id_Reservation
                WHERE (r.Date_arrivee <= ? AND r.Date_depart >= ?)
            )
        """
        available_rooms = cur.execute(query, (end_date, start_date)).fetchall()
        st.write(f"Rooms available from {start_date} to {end_date}:")
        st.table(available_rooms)
    else:
        st.warning("End date must be after start date.")

# 4. Add Client
elif menu == "Add Client":
    st.subheader("➕ Add New Client")
    with st.form("add_client_form"):
        nom = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        address = st.text_input("Address")
        city = st.text_input("City")
        postal = st.number_input("Postal Code", step=1)
        submitted = st.form_submit_button("Add Client")

        if submitted:
            try:
                cur.execute("""
                    INSERT INTO Client (Adresse, Ville, Code_postal, Email, Telephone, Nom_complet)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (address, city, postal, email, phone, nom))
                conn.commit()
                st.success(f"Client '{nom}' added successfully.")
            except sqlite3.IntegrityError:
                st.error("This email is already in use.")

# 5. Add Reservation
elif menu == "Add Reservation":
    st.subheader("📝 Add Reservation")

    clients = cur.execute("SELECT Id_Client, Nom_complet FROM Client").fetchall()
    client_dict = {f"{c[1]} (ID: {c[0]})": c[0] for c in clients}

    chambres = cur.execute("SELECT Id_Chambre, Numero FROM Chambre").fetchall()
    chambre_dict = {f"Room {c[1]} (ID: {c[0]})": c[0] for c in chambres}

    with st.form("add_reservation_form"):
        client_name = st.selectbox("Select Client", list(client_dict.keys()))
        room_id = st.selectbox("Select Room", list(chambre_dict.keys()))
        start_date = st.date_input("Arrival Date")
        end_date = st.date_input("Departure Date")
        submitted = st.form_submit_button("Add Reservation")

        if submitted:
            if start_date >= end_date:
                st.error("Departure must be after arrival.")
            else:
                cur.execute("INSERT INTO Reservation (Date_arrivee, Date_depart, Id_Client) VALUES (?, ?, ?)",
                            (start_date, end_date, client_dict[client_name]))
                reservation_id = cur.lastrowid
                cur.execute("INSERT INTO Chambre_Reservation (Id_Chambre, Id_Reservation) VALUES (?, ?)",
                            (chambre_dict[room_id], reservation_id))
                conn.commit()
                st.success("Reservation successfully added.")
