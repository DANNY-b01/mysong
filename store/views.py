from rest_framework.response import Response
from .models import Song
from .serializers import Songserializers
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def all_songs(request):
    if request.method =="GET":
        all_songs= Song.objects.all()
        serialized_student =Songserializers(all_songs, many=True)
        return Response(serialized_student.data)
    else:
        Song_data = Songserializers(data=request.data)
        if Song_data.is_valid():
            Song_data.save()
            return Response("You'eve added a new song")
        return Response(Song_data.errors)
    



@api_view(["GET","PUT","DELETE"])
def single_song_view(request,id):
    if request.method =="GET":
        single_song = Song.objects.get(id=id)
        serialized_song = Songserializers(single_song)
        return Response(serialized_song.data)
    elif request.method =="PUT":
        single_song= Song.objects.get(id=id)
        serialized_song= Songserializers(single_song, data=request.data, partial=True)
        if serialized_song.is_valid():
            serialized_song.save()
            return Response("you have successfully update this song")
        return Response(serialized_song.errors)
    else:
        single_song = Song.objects.get(id=id)
        single_song.delete()
        return Response ("you have successfully deleted this song")

    

# Create your views here.
