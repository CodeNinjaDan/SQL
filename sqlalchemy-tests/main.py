from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

"""
SQLAlchemy is an Object Relational Mapper - it's able to map relationships in a database into Objects.
Tables are defined as separate Classes and each row of data is a new Object.
"""

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    #Create table if it doesn't exist
    db.create_all()

    # Create a new book instance
    new_book = Books(title="Harry Potter", author="J.K.Rowling", rating=4.5)

    # Add the new book instance to the session
    db.session.add(new_book)

    # Delete an instance
    db.session.delete(new_book)

    # Commit the session to save the changes in the database
    db.session.commit()

    # Read all records
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()

    # Read specific record
    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()

    # Update specific record
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

    # Update record by Primary Key
    book_id = 1
    with app.app_context():
        book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
        # or book_to_update = db.get_or_404(Book, book_id)
        book_to_update.title = "Harry Potter and the Goblet of Fire"
        db.session.commit()

    # Delete record by Primary Key
    book_id = 1
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()