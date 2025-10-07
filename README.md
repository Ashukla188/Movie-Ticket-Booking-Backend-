# 🎬 Movie Booking System (Backend)

# A Django REST Framework–based backend for a Movie Ticket Booking System,
# implementing authentication, movie/show management, and seat booking with 
# complete business rule validation.

# ------------------------------------------------------------
# 🚀 FEATURES
# ------------------------------------------------------------
# - User Registration & JWT Authentication
# - Movie & Show Listing
# - Seat Booking and Cancellation
# - Double Booking Protection
# - Show Capacity Enforcement
# - User-specific Booking Access Control
# - Integrated Swagger API Documentation

# ------------------------------------------------------------
# 🛠️ TECH STACK
# ------------------------------------------------------------
# Python 3.10+
# Django 5.0
# Django REST Framework
# SimpleJWT (JSON Web Tokens)
# SQLite (default)
# Swagger (drf-yasg) for API testing

# ------------------------------------------------------------
# 🧩 PROJECT SETUP
# ------------------------------------------------------------

# 1️⃣ Clone the Repository
git clone <your_repo_url>
cd movie_booking

# 2️⃣ Create & Activate Virtual Environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

# 5️⃣ Create Superuser (for Django Admin)
python manage.py createsuperuser

# 6️⃣ Run Server
python manage.py runserver

# Server will start at:
# http://127.0.0.1:8000/

# ------------------------------------------------------------
# 🧠 API DOCUMENTATION (SWAGGER)
# ------------------------------------------------------------
# Once the server is running, open:
# http://127.0.0.1:8000/swagger/
# Use this UI to test all APIs interactively.
# You can also use Postman with the same endpoints.

# ------------------------------------------------------------
# 🔐 AUTHENTICATION FLOW
# ------------------------------------------------------------
# Step | Endpoint | Description
# 1 | /api/signup/ | Register new user
# 2 | /api/login/ | Login to get JWT tokens
# 3 | /api/token/refresh/ | (Optional) Refresh expired token

# JWT Header Format:
# Authorization: Bearer <access_token>

# ------------------------------------------------------------
# 🎬 MOVIE & SHOW MANAGEMENT
# ------------------------------------------------------------
# Visit the Django Admin:
# http://127.0.0.1:8000/admin/
# Use superuser credentials to:
# - Add Movies
# - Add Shows

# Each show has:
# movie
# screen_name
# date_time
# total_seats

# ------------------------------------------------------------
# 📡 API ENDPOINTS
# ------------------------------------------------------------

# 1️⃣ Register User → /api/signup/
# POST
# {
#   "username": "john",
#   "email": "john@gmail.com",
#   "password": "test1234"
# }

# 2️⃣ Login → /api/login/
# POST
# {
#   "username": "john",
#   "password": "test1234"
# }
# Response:
# {
#   "refresh": "<refresh_token>",
#   "access": "<access_token>"
# }

# 3️⃣ Get All Movies → /api/movies/
# GET
# [
#   {
#     "id": 1,
#     "title": "Inception",
#     "duration_minutes": 148
#   }
# ]

# 4️⃣ Get Shows for a Movie → /api/movies/<movie_id>/shows/
# GET
# [
#   {
#     "id": 1,
#     "screen_name": "Screen 1",
#     "date_time": "2025-10-07T20:00:00Z",
#     "total_seats": 10
#   }
# ]

# 5️⃣ Book a Seat → /api/shows/<show_id>/book/
# POST
# {
#   "seat_number": 5
# }
# Response:
# {
#   "id": 1,
#   "show": 1,
#   "seat_number": 5,
#   "status": "booked"
# }

# 6️⃣ View My Bookings → /api/my-bookings/
# GET
# [
#   {
#     "id": 1,
#     "seat_number": 5,
#     "status": "booked"
#   }
# ]

# 7️⃣ Cancel a Booking → /api/bookings/<booking_id>/cancel/
# POST
# Response:
# {
#   "message": "Booking 1 cancelled successfully",
#   "status": "cancelled"
# }

# ------------------------------------------------------------
# ⚙️ BUSINESS RULES IMPLEMENTED
# ------------------------------------------------------------
# ✅ A seat cannot be booked twice (only one active booking per seat).
# ✅ Total bookings cannot exceed show capacity.
# ✅ Cancelling a booking frees up the seat for rebooking.
# ✅ A user cannot cancel another user's booking.
# ✅ Double booking & invalid seat numbers return descriptive errors.

# ------------------------------------------------------------
# 🧪 TEST FLOW (RECOMMENDED ORDER)
# ------------------------------------------------------------
# 1️⃣ /api/signup/ → Register user
# 2️⃣ /api/login/ → Get JWT token
# 3️⃣ /api/movies/ → List all movies
# 4️⃣ /api/movies/<id>/shows/ → List shows
# 5️⃣ /api/shows/<id>/book/ → Book a seat
# 6️⃣ /api/my-bookings/ → Verify booking
# 7️⃣ /api/bookings/<id>/cancel/ → Cancel
# 8️⃣ /api/shows/<id>/book/ → Rebook same seat ✅

# ------------------------------------------------------------
# 🧾 EXAMPLE BUSINESS RULE VALIDATION
# ------------------------------------------------------------
# | Action | Expected Behavior |
# |--------|--------------------|
# | Book same seat twice | ❌ "Seat already booked" |
# | Cancel booking | ✅ "Booking cancelled successfully" |
# | Rebook cancelled seat | ✅ "booked" |
# | Cancel another user’s booking | ❌ "Booking not found or not yours" |

# ------------------------------------------------------------
# 🧰 ADMIN CREDENTIALS (for local dev)
# ------------------------------------------------------------
# URL: http://127.0.0.1:8000/admin/
# Username: <admin>
# Password: <gamma@123>

# ------------------------------------------------------------
# 🧹 RESET DATABASE (if needed)
# ------------------------------------------------------------
python manage.py flush
python manage.py migrate

# ------------------------------------------------------------
# 📄 LICENSE
# ------------------------------------------------------------
# This project is open-source and developed for educational and assessment purposes.

# ------------------------------------------------------------
# 👨‍💻 AUTHOR
# ------------------------------------------------------------
# Ayush Kumar Shukla
# Backend Developer Intern Assignment – AlignTurtle
