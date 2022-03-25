from dataclasses import field
from rest_framework import serializers

from .models import Card,Comments,Likes



class LikesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Likes
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ["comment","createdDate"]



class CardSerializer(serializers.ModelSerializer):
    
    comments =CommentSerializer(many = True,read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)
    likes =LikesSerializer(many = True,read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Card
        fields = ["id","user","title","image","content","createdDate","updateDate","comments","comments_count","likes","likes_count"]

    def get_comments_count(self,obj):
        return obj.comments.count()

    def get_likes_count(self,obj):
        return obj.comments.count()
