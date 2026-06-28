from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disciplina = db.Column(db.String(100), nullable=False)
    enunciado = db.Column(db.Text, nullable=False)
    alternativa_a = db.Column(db.String(500), nullable=False)
    alternativa_b = db.Column(db.String(500), nullable=False)
    alternativa_c = db.Column(db.String(500), nullable=False)
    alternativa_d = db.Column(db.String(500), nullable=False)
    alternativa_e = db.Column(db.String(500), nullable=False)
    alternativa_correta = db.Column(db.String(1), nullable=False)
    explicacao = db.Column(db.Text, nullable=True)
    nivel = db.Column(db.String(20), default='medio')

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frente = db.Column(db.Text, nullable=False)
    verso = db.Column(db.Text, nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)
    acertos = db.Column(db.Integer, default=0)
    erros = db.Column(db.Integer, default=0)
    revisoes = db.Column(db.Integer, default=0)

    @property
    def dificuldade(self):
        total = self.acertos + self.erros
        if total == 0:
            return 1
        taxa = self.erros / total
        if taxa >= 0.5:
            return 4
        if taxa >= 0.3:
            return 3
        if taxa >= 0.1:
            return 2
        return 1

    def to_dict(self):
        return {
            'id': self.id,
            'frente': self.frente,
            'verso': self.verso,
            'disciplina': self.disciplina,
            'acertos': self.acertos,
            'erros': self.erros,
            'revisoes': self.revisoes,
            'indice_dificuldade': self.dificuldade
        }

class SimuladoResultado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, nullable=False)
    acertos = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)

class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao_id = db.Column(db.Integer, db.ForeignKey('questao.id'), nullable=False)
    simulado_id = db.Column(db.Integer, db.ForeignKey('simulado_resultado.id'), nullable=False)
    alternativa_escolhida = db.Column(db.String(1))
    correta = db.Column(db.Boolean, default=False)
    errou = db.Column(db.Boolean, default=False)

    questao = db.relationship('Questao', backref=db.backref('respostas', lazy='dynamic'))
    simulado = db.relationship('SimuladoResultado', backref=db.backref('respostas', lazy='dynamic'))