from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movies/<int:movie_id>/shows/', views.ShowListView.as_view(), name='show-list'),
    path('shows/<int:show_id>/book/', views.BookSeatView.as_view(), name='book-seat'),
    path('my-bookings/', views.MyBookingsView.as_view(), name='my-bookings'),
    path('bookings/<int:booking_id>/cancel/', views.CancelBookingView.as_view(), name='cancel-booking'),
]
