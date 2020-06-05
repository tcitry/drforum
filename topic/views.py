import logging

from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from .models import TopicModel, TopicCommentModel
from .serializers import TopicListSerializer, TopicCommentSerializer

logger = logging.getLogger(__name__)


class TopicListView(APIView):
    """
    列出所有主题列表
    """

    def get(self, request, *args, **kwargs):
        topic_list = TopicModel.objects.all()
        serializer = TopicListSerializer(topic_list, many=True)
        res_data = serializer.data
        return Response(res_data, status=200)

    def post(self, request, *args, **kwargs):
        total_topic = TopicModel.objects.all()
        index = total_topic.count() + 1
        serializer = TopicListSerializer()
        create_param = {
            'title': f'title_{index}'.format(index),
            'content': f'content_{index}'.format(index),
            'author_id': 1
        }
        serializer.create(create_param)
        res_data = {
            'msg': 'ok'
        }
        return Response(res_data, status=status.HTTP_200_OK)


class TopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    每条主题内容
    """

    lookup_field = 'id'
    lookup_url_kwarg = 'topic_id'
    serializer_class = TopicListSerializer

    def get_queryset(self):
        logger.debug('query_params is ', self.request.query_params)
        return TopicModel.objects.all()


class TopicCommentView(generics.ListCreateAPIView):
    """
    所有的评论列表
    """

    serializer_class = TopicCommentSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TopicCommentModel.objects.filter(
            topic_id=self.kwargs['topic_id'])
