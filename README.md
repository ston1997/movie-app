# live-coding-movies-app

# SRS:
Develop a RESTful web service to obtain movie information.

The following information about the movie should be stored in the database:
1. Title
2. Release Date
3. Rating (min value - 1, max value - 5)
4. Genres - id, title
5. Actors - id, name
6. Similar movies

Create API endpoints to get a list of movies and detailed information about a particular movie.

The endpoint with collection of movies should return the following:
1. Title
2. Rating
3. Genres (id, title)
4. Number of actors
Users should be able to order movies by release date, rating, filter by genres (multiple by ids) and search by title. 
Default ordering by rating (desc).

The endpoint with detailed information should return the following:
1. Title
2. Release Date
3. Rating
4. Genres (id, title)
5. Actors (id, name)
6. Similar movies (title, release date)


# TODO: add filtering