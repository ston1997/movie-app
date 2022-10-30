from rest_framework import serializers

from movie.models import Movie, Genre, Actor


class GenreSerializer(serializers.ModelSerializer):
    """Return genre information."""

    class Meta:
        model = Genre
        fields = (
            "id",
            "title"
        )


class ActorSerializer(serializers.ModelSerializer):
    """Return actor information."""

    class Meta:
        model = Actor
        fields = (
            "id",
            "name"
        )


class MovieListSerializer(serializers.ModelSerializer):
    """Return short movie information for collection of movies."""

    genres = GenreSerializer(many=True)
    number_of_actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            "title",
            "rating",
            "genres",
            "number_of_actors"
        )

    @staticmethod
    def get_number_of_actors(obj):
        return obj.actors.all().count()


class SimilarMovieSerializer(serializers.ModelSerializer):
    """Information about similar movies."""

    class Meta:
        model = Movie
        fields = (
            "title",
            "release_date"
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    """Return detail information for single movie."""

    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    similar_movies = SimilarMovieSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            "title",
            "release_date",
            "rating",
            "genres",
            "actors",
            "similar_movies"
        )
