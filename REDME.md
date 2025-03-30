# Axio Assignment Setup Guide

This project consists of a **Django backend** and a **Vite + React frontend**.

## Cloning the Repository

```sh
git clone https://github.com/miyami-41820/axio-assigment.git
cd axio-assigment

git checkout develop
```

---

## Backend Setup

1. **Create and activate a virtual environment:**
   ```sh
   python3.11 -m venv axiovenv  
   source axiovenv/bin/activate    
   ```

2. **Navigate to the backend directory:**
   ```sh
   cd backend
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirement.txt
   ```

4. **Apply database migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Load dummy data into the database:**
   ```sh
   python manage.py shell
   >>> import flight_dummy_data
   >>> exit()
   ```

6. **Run the backend server:**
   ```sh
   python3 manage.py runserver
   ```

### Backend setup explanation:
- `migrate` will create tables in the SQLite database (in-memory DB).
- `runserver` will connect to that database and start the backend server on `localhost`.
- `flight_dummy_data` script inserts dummy data into the database for testing purposes.

---

## Frontend Setup

1. **Navigate to the frontend directory:**
   ```sh
   cd frontend
   ```

2. **Install dependencies:**
   ```sh
   npm i
   ```

3. **Start the frontend server:**
   ```sh
   npm run dev
   ```

### Frontend setup explanation:
- `npm i` installs the required packages.
- `npm run dev` starts the frontend server on `localhost`.

---

## Testing the Application

1. Ensure both the backend and frontend servers are running.
2. Open the **frontend dashboard** in your browser to check the application.

---

## Running Unit Tests

The backend unit tests are located inside the `airlineapp` app in the `tests.py` file. 

To run all test cases, execute the following command at the same location as `manage.py` (where the backend server runs):

```sh
python3 manage.py test
```

This will run all defined test cases and verify the application's correctness.

---

## Notes
- The backend runs on `http://127.0.0.1:8000/`
- The frontend runs on `http://localhost:5173/` (default Vite port)

# Airline Reservation System - API Documentation

## Overview
This document provides details about the RESTful APIs developed for the Airline Reservation System. The backend is implemented using Python with Django and Django Rest Framework.

## API Endpoints

### 1. Get All Available Flights
**Endpoint:** `GET /flights/`

**Request:**
```
GET http://127.0.0.1:8000/flights/
```

**Response:**
```json
{
    "code": 200,
    "data": [
        {
            "flight_id": 4,
            "airline": "SpiceJet",
            "departure_location": "Mumbai",
            "destination_location": "Kolkata",
            "destination_time": "2025-04-28T00:35:07.814197Z",
            "departure_time": "2025-04-27",
            "available_seats": 67
        }
    ],
    "errors": {},
    "message": "Success"
}
```

---

### 2. Get All Available Coupons
**Endpoint:** `GET /coupon/`

**Request:**
```
GET http://127.0.0.1:8000/coupon/
```

**Response:**
```json
{
    "code": 200,
    "data": [
        {
            "id": 1,
            "code": "COUPON872",
            "discount_percentage": 40,
            "valid_until": "2025-05-03"
        }
    ],
    "errors": {},
    "message": "Success"
}
```

---

### 3. Get Fare Details of a Flight
**Endpoint:** `GET /flights/{flight_id}/fare/`

**Request:**
```
GET http://127.0.0.1:8000/flights/3/fare/
```

**Response:**
```json
{
    "code": 200,
    "data": {
        "fare": 7183.94
    },
    "errors": {},
    "message": "Success"
}
```

---

### 4. Apply Coupon to Get Discounted Price
**Endpoint:** `GET /flights/{flight_id}/fare/?coupon={coupon_code}`

**Request:**
```
GET http://127.0.0.1:8000/flights/3/fare/?coupon=COUPON872
```

**Response:**
```json
{
    "code": 200,
    "data": {
        "fare": 4310.364,
        "coupon_validity": true
    },
    "errors": {},
    "message": "Success"
}
```

---

### 5. Create a Reservation
**Endpoint:** `POST /reservation/`

**Request (With Coupon):**
```
POST http://127.0.0.1:8000/reservation/
```

```
Content-Type: application/json

{
    "passenger_name": "Shyama Kumari",
    "paid_price": 4310.364,
    "flight_id": "3",
    "coupon": "COUPON872"
}

please make sure to enter correct coupon, flight id and price otherwise api will give error response
```

**Request (Without Coupon):**
```
POST http://127.0.0.1:8000/reservation/
```

```
Content-Type: application/json

{
    "passenger_name": "Shyama Kumari",
    "paid_price": 4310.364,
    "flight_id": "3"
}

please make sure to enter correct flight id and price other wise api will give error response
```

**Response:**
```json
{
    "code": 201,
    "data": {
        "status": "Booked Successfully"
    },
    "errors": {},
    "message": "Created Successfully"
}
```

---

### 6. View All Confirmed Bookings
**Endpoint:** `GET /confirmed-reservation/`

**Request:**
```
GET http://127.0.0.1:8000/confirmed-reservation/
```

**Response:**
```json
{
    "code": 200,
    "data": [
        {
            "id": 3,
            "flight": {
                "flight_id": 7,
                "airline": "Air India",
                "departure_location": "Bangalore",
                "destination_location": "Delhi",
                "destination_time": "2025-04-27T23:35:07.816995Z",
                "departure_time": "2025-04-27",
                "available_seats": 74
            },
            "passenger_name": "Bob Smith",
            "seat_number": "46",
            "confirmed": true,
            "paid_price": 8438.0
        }
    ],
    "errors": {},
    "message": "Success"
}
```


### 7. View All Reservation Bookings
**Endpoint:** `GET /reservation/`

**Request:**
```
GET http://127.0.0.1:8000/reservation/
```

**Response:**
```json
{
    "code": 200,
    "data": [
        {
            "id": 3,
            "flight": {
                "flight_id": 7,
                "airline": "Air India",
                "departure_location": "Bangalore",
                "destination_location": "Delhi",
                "destination_time": "2025-04-27T23:35:07.816995Z",
                "departure_time": "2025-04-27",
                "available_seats": 74
            },
            "passenger_name": "Bob Smith",
            "seat_number": "46",
            "confirmed": true,
            "paid_price": 8438.0
        }
    ],
    "errors": {},
    "message": "Success"
}
```
