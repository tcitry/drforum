from rest_framework.views import APIView, Response
from ..models import TopicListModel
from ..serializers import TopicListSerializer


class TopicListView(APIView):
    def get(self, request, *args, **kwargs):
        topic_list = TopicListModel.objects.all()
        serializer = TopicListSerializer(topic_list, many=True)
        res_data = serializer.data
        return Response(res_data)

    def post(self, request, *args, **kwargs):
        param = {
            'info': 'hahaha'
        }
        return Response(param)


class TopicDetailView(APIView):
    def get(self, request, *args, **kwargs):
        return Response()
