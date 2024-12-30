#app imports
from django.shortcuts import render
from .models import Watchlist,StreamPlatform,Review
from .serializers import WatchlistSerializer,StreamPlatformSerializer,ReviewSerializer

#rest framework imports
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class ReviewList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get (self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post (self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get (self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

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
        