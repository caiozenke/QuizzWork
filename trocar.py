from modelo import *

#Trocar os ids de quem nao tem time para o 0
def trocar_null():
  dados = db.session.query(Jogador).filter(Jogador.times_id == None).all()
  
  for ids in dados:
    db.session.execute(f'UPDATE  Jogador SET times_id = 0 where id = {ids.id}')    
    db.session.commit()
  