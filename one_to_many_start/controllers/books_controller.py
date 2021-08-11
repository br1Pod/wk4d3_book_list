from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

##### MVP #####

# INDEX
@books_blueprint.route("/books", methods=["GET"])
def show_all_books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

# DELETE


##### EXTENSION #####


# NEW


# CREATE


# SHOW



##### ADVANCED EXTENSION #####


# EDIT


# UPDATE


