import os
from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title, User

from api_yamdb.settings import BASE_DIR

MODEL_FILE = {
    Category: "category.csv",
    Genre: "genre.csv",
    Title: "titles.csv",
    User: "users.csv",
    Review: "review.csv",
    Comment: "comments.csv",
}


class Command(BaseCommand):
    def import_data(self, model, filename: str):
        print(f"Import model {model.__name__}")
        if model.objects.exists():
            model.objects.all().delete()

        path = os.path.join(BASE_DIR, "static/data", filename)
        reader = list(DictReader(open(path, encoding="utf8")))

        for dct in map(dict, reader):
            if model.__name__ == "Title":
                category = Category.objects.get(id=dct.pop("category"))
                model.objects.create(**dct, category=category)

            elif model.__name__ == "Review":
                title = Title.objects.get(id=dct.pop("title_id"))
                author = User.objects.get(id=dct.pop("author"))
                model.objects.create(**dct, title=title, author=author)

            elif model.__name__ == "Comment":
                review = Review.objects.get(id=dct.pop("review_id"))
                author = User.objects.get(id=dct.pop("author"))
                model.objects.create(**dct, review=review, author=author)
            else:
                model.objects.create(**dct)
        print(f"Import model {model.__name__} done")

    def handle(self, *args, **options):
        for model, filename in MODEL_FILE.items():
            self.import_data(model, filename)

        print("Import Genre_title data")
        path = os.path.join(BASE_DIR, "static/data", "genre_title.csv")
        reader = list(DictReader(open(path, encoding="utf8")))

        for dct in map(dict, reader):
            title = Title.objects.get(id=dct.pop("title_id"))
            genre = Genre.objects.get(id=dct.pop("genre_id"))
            title.genre.add(genre)
            title.save()
        print("Import Genre_title data done")
