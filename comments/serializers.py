from rest_framework import serializers
from comments.models import Comment
from sentry_sdk import capture_exception

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
    
    def create(self, data):
        
        try:
            instance = self.Meta.model(**data)
            instance.save()
        except Exception as e:
            # Alternatively the argument can be omitted
            capture_exception(e)
        return instance 