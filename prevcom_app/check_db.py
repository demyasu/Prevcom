from app import app
from models import db, Questao, Flashcard
with app.app_context():
    for d, c in db.session.query(Questao.disciplina, db.func.count(Questao.id)).group_by(Questao.disciplina).all():
        print(f'{d}: {c}')
    print(f'Total questoes: {Questao.query.count()}')
    cards = Flashcard.query.count()
    print(f'Total flashcards: {cards}')
    for d, c in db.session.query(Flashcard.disciplina, db.func.count(Flashcard.id)).group_by(Flashcard.disciplina).all():
        print(f'  FC {d}: {c}')
