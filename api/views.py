#app imports
from django.shortcuts import render
from .models import Watchlist,StreamPlatform,Review
from .serializers import WatchlistSerializer,StreamPlatformSerializer,ReviewSerializer
from .permissions import AdminOrReadOnly,AuthorOrReadOnly
#rest framework imports
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = Watchlist.objects.get(pk=pk)
        
        author = self.request.user
        query_set = Review.objects.filter(watchlist=movie,author=author)
        
        if query_set.exists():
            raise ValidationError("you have already reviewed this movie")
        
        
        
        serializer.save(watchlist=movie,author=author)

class ReviewList(generics.ListCreateAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    




# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get (self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post (self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     def get (self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

class StreamPlatformAV(APIView):
    def get(self,request):
        streaming_platform_list = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streaming_platform_list,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    def put(self,request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        item = StreamPlatform.objects.get(pk=pk)
        item.delete()
        return Response({"success":"Record Deleted Successfully!"},status.HTTP_301_MOVED_PERMANENTLY)
        

class WatchlistAV(APIView):
    def get(self,request):
        watchlists = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlists,many=True)
       
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchlistDetailAV(APIView):
    def get(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie,data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        