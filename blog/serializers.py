from dataclasses import field
from rest_framework import serializers

from .models import Card,Comments

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ["comment","createdDate"]



class CardSerializer(serializers.ModelSerializer):
    
    comments =CommentSerializer(many = True,read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Card
        fields = ["title","content","createdDate","comments","updateDate","comments_count"]

    def get_comments_count(self,obj):
        return obj.comments.count()
