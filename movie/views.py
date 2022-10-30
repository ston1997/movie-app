from rest_framework.viewsets import ReadOnlyModelViewSet

from movie.models import Movie
from movie.serializers import MovieListSerializer, MovieDetailSerializer


class MovieAPIVieSet(ReadOnlyModelViewSet):
    """Return detail information about movie and list of movies."""

    queryset = Movie.objects.order_by("-release_date", "title").prefetch_related(
        "genres", "actors", "similar_movies"
    ).all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        return MovieDetailSerializer
