# Setup

## Python packages
All the required packages along with whith the specific version are listed in the `requirements.txt` configuration file. They can be installed in the usual manner:

```
pip install -r requirements.txt
```

## Flashcards fixture
The attached flashcards fixture (`flashcards/seed/0001_Flashcard.json`) has been generated with the attached script (`flashcards/seed/flashcards_fixture_generator.py`) that extracts all acronyms list from the attached exam objectives PDF file (`flashcards/seed/comptia-sec-exam-objectives.pdf`).

In order to initialize the database with the generated acronyms list use Django's out-of-the box `loaddata` feature:

```
python manage.py loaddata flashcards/seed/0001_Flashcard.json
```