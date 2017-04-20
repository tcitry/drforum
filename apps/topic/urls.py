from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.TopicListView.as_view({'get': 'list', 'post': 'create'})),
    url(r'^$', views.TopicListView.as_view()),
    url(r'^(?P<topic_id>[0-9]+)$', views.TopicDetailView.as_view()),
    url(r'^(?P<topic_id>[0-9]+)/comments$', views.TopicCommentView.as_view()),
]
