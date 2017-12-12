from rest_framework import routers

from books.views import BookViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)
urlpatterns = router.urls
