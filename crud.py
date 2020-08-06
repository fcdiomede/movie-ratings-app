"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):

  movie = Movie(title=title, overview=overview,
                release_date=release_date, poster_path=poster_path)

  db.session.add(movie)
  db.session.commit()


def create_rating(score, movie_id, user_id):
    """Create and return a new rating"""

    rating = Rating(score=score, movie_id=movie_id, user_id=user_id)

    db.session.add(rating)
    db.session.commit()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)





