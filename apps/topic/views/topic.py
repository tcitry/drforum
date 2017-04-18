import logging
from rest_framework.views import APIView, Response

from ..models import TopicModel
from ..serializers import TopicListSerializer

logger = logging.getLogger(__name__)


class TopicListView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.stream)
        topic_list = TopicModel.objects.all()
        serializer = TopicListSerializer(topic_list, many=True)
        res_data = serializer.data
        return Response(res_data, status=200)

    def post(self, request, *args, **kwargs):
        total_topic = TopicModel.objects.all()
        index = total_topic.count() + 1
        serializer = TopicListSerializer()
        create_param = {
            'title': 'title_%s' % index,
            'content': 'content_%s' % index,
            'author_id': 1
        }
        serializer.create(create_param)
        res_data = {
            'msg': 'ok'
        }
        return Response(res_data, status=200)


class TopicDetailView(APIView):
    def get(self, request, *args, **kwargs):
        return Response()
