from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
    
    def create(self, data):
        
        instance = self.Meta.model(**data)
        instance.save()
    
        return instance 