

from config import *

class Time(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(254))
    fundado = db.Column(db.Integer)
    jogadores = db.relationship('Jogador', backref ='time')
    def __str__(self) -> str:
        return f'{str(self.id)}) {self.nome} , {str(self.fundado)}' 


class Jogador(db.Model):
    
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    titulos = db.Column(db.Integer)
    kills = db.Column(db.Integer)
    valor = db.Column(db.Float)

    times_id = db.Column(db.Integer, db.ForeignKey(Time.id), 
                          nullable=True)
    
    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            str(self.titulos) + ", " + str(self.kills) + " , " + str(self.valor)
    def json(self):
    
        j1 = {'nome': self.nome,'titulos': self.titulos , "kills": self.kills , "valor": self.valor}
        return j1




if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe
    t1= Time(nome = 'T1' , fundado = 1923) 
    p1 = Jogador(nome = "Oner", titulos = 3, 
        kills = 10323, valor = 32)
    p5 = Jogador(nome = "Showmaker", titulos = 1, 
        kills = 323, valor = 22)
    p2 = Jogador(nome = "Faker", titulos = 7, 
        kills = 1323, valor = 213, time= t1)
    p3 = Jogador(nome = "guamyusi", titulos = 0, 
        kills = 23, valor = 13, time= t1)
   
   
    
    # persistir
    db.session.add(t1)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p5)
    db.session.commit()
    

    # exibir

    print('JOGADORES DA T1')
    for j in t1.jogadores:
        print(j)

    
    print()
    print('jogadores sem time')
    for js in db.session.query(Jogador).filter(Jogador.times_id == None):
        del(js)