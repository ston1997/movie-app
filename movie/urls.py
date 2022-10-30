from rest_framework.routers import SimpleRouter

from movie.views import MovieAPIVieSet

router = SimpleRouter()
router.register("", MovieAPIVieSet, basename="movie")

urlpatterns = router.urls
