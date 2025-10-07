from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Movie, Show, Booking
from .serializers import MovieSerializer, ShowSerializer, BookingSerializer


# ------------------------- Signup -------------------------
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password required"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"id": user.id, "username": user.username, "email": user.email}, status=201)


# ------------------------- Login -------------------------
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=400)

        if not user.check_password(password):
            return Response({"error": "Invalid credentials"}, status=400)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })


# ------------------------- Movie List -------------------------
class MovieListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# ------------------------- Shows by Movie -------------------------
class ShowListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, movie_id):
        shows = Show.objects.filter(movie_id=movie_id)
        serializer = ShowSerializer(shows, many=True)
        return Response(serializer.data)


# ------------------------- Book a Seat -------------------------
class BookSeatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, show_id):
        seat_number = request.data.get('seat_number')
        if not seat_number:
            return Response({"error": "Seat number is required"}, status=400)

        try:
            show = Show.objects.get(id=show_id)
        except Show.DoesNotExist:
            return Response({"error": "Show not found"}, status=404)

        if int(seat_number) > show.total_seats:
            return Response({"error": "Invalid seat number"}, status=400)

        # Check if seat is already booked (only active bookings matter)
        if Booking.objects.filter(show=show, seat_number=seat_number, status='booked').exists():
            return Response({"error": "Seat already booked"}, status=400)

        # Check total active bookings for show
        active_bookings = Booking.objects.filter(show=show, status='booked').count()
        if active_bookings >= show.total_seats:
            return Response({"error": "All seats booked"}, status=400)

        booking = Booking.objects.create(
            user=request.user,
            show=show,
            seat_number=seat_number,
            status='booked'
        )
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=201)


# ------------------------- View My Bookings -------------------------
class MyBookingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


# ------------------------- Cancel Booking -------------------------
class CancelBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found or not yours"}, status=404)

        if booking.status == 'cancelled':
            return Response({"message": "Booking already cancelled"}, status=400)

        booking.status = 'cancelled'
        booking.save(update_fields=["status"])
        booking.refresh_from_db()

        return Response({
            "message": f"Booking {booking.id} cancelled successfully",
            "status": booking.status
        })
