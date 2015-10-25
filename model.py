"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Create Model class, which creates the Models table."""

    __tablename__ = "models"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=True)
    brand_name = db.Column(db.String(20), db.ForeignKey('brands.name'), nullable=False)
    name = db.Column(db.String(30), nullable=True)

    brand = db.relationship("Brand", backref=db.backref("models"))

    def __repr__(self):
        """Write out userful information about each object."""

        return "<Model id=%s year=%s brand_name=%s name=%s>" % (
            self.id, self.year, self.brand_name, self.name)


class Brand(db.Model):

    __tablename__ = "brands"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    founded = db.Column(db.Integer, nullable=True)
    headquarters = db.Column(db.String(30), nullable=True)
    discontinued = db.Column(db.Integer, nullable=True)

    model = db.relationship("Model", backref=db.backref("brands"))

    def __repr__(self):
        """Write out userful information about each object."""

        return "<Brand id=%s name=%s founded=%s headquarters=%s>" % (
            self.id, self.name, self.founded, self.headquarters)



# End Part 1
##############################################################################
# Helper functions


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
