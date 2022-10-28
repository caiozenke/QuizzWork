from modelo import *

#acabar o calculo 
def calcular():
  dados = db.session.query(Jogador).filter(Jogador.valor == 10.0).all()
  
  for ids in dados:
    db.session.execute(f'UPDATE  Jogador SET valor = (valor * {1.7}) where id = {ids.id}')    
    db.session.commit()
  