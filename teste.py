from modelo import *
from config import *
from flask import request



aa = Jogador.valor == 10
#dados = db.session.query(Jogador).filter(aa).all()#pegando jogador sem time e pelo seu nome 
dados = db.session.query(Jogador).filter(Jogador.valor == 10.0).all()
teste = []

  
print(dados)



#    db.session.execute(f'UPDATE  Jogador SET valor = (valor * {1.26}) where kills > {1000}')
for ids in dados:
    
    a =(ids.id)
            
print(a)

#db.session.execute(f'UPDATE  Jogador SET valor = (valor * {1.7}) where id = {a}')