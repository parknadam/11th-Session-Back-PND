from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response

# Create your views here.


class PostListView(views.APIView):
    def get(Self, request, format=None):
        posts=Post.objects.all()
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(Self, request, format=None):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors)
        return Response(serializer.errors)
    
class PostDetailView(views.APIView):
    def get(Self, request, pk, format=None):
        post=get_object_or_404(Post, pk=pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)
   
    def put(Self, request, pk, format=None):
        post=get_object_or_404(Post, pk=pk)
        serializer=PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        post=get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({"message":"게시물 삭제 성공"}) 
    
    
class CommentView(views.APIView):
    def post(Self, request, format=None):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(Self, request, format=None):
        comment=Comment.objects.all()
        serializer=CommentSerializer(comment, many=True)
        return Response(serializer.data)
    

class CommentDetailView(views.APIView):
    def get(Self, request, pk, format=None):
        comments=get_object_or_404(Comment, pk=pk)
        serializer=CommentSerializer(comments)
        return Response(serializer.data)
   
    def put(Self, request, pk, format=None):
        comment=get_object_or_404(Comment, pk=pk)
        serializer=CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        comment=get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({"message":"댓글 삭제 성공"}) 