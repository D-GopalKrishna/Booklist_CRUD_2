from Bookdetails.viewsets import BookViewset, GenreViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('booklist', BookViewset)
router.register('genrelist', GenreViewsets)
