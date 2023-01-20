from comments.models import Comment
from comments.serializers import CommentSerializer
from comments.paginators import TinnyResultsSetPagination

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class CommentsRecordsView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = TinnyResultsSetPagination
    
    
    @action(methods=['POST'], permission_classes = [IsAuthenticated], detail=False, url_path='store')
    def store(self, request):
        user = request.user
        data = request.data | {'user_id': user.id}
        data['course_id'] = data['course_id'][0]
        data['text'] = data['text'][0]
        
    
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'msg': 'Created successfully', 'comment': serializer.data})
    