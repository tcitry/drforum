from rest_framework.views import APIView, Response


class TopicListView(APIView):
    def get(self, request, *args, **kwargs):
        param = {
            'hello': 'world',
        }
        return Response(param)

    def post(self, request, *args, **kwargs):
        param = {
            'info': 'hahaha'
        }
        return Response(param)
