from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'', views.AccountViewSet, base_name='user')
urlpatterns = router.urls
