from django.urls import path
from .views import all_songs,single_song_view



urlpatterns=[
    path("", all_songs, name="all_students"),
    path("<int:id>/",single_song_view, name="single_student_view")
]