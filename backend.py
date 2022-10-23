
from modelo import *
from config import *

@app.route("/")

def inicio():
    return 'Funcionando'

def calcular():
    db.session.execute(f'UPDATE  Jogador SET valor = (valor * {1.7}) where titulos > {6}')
    db.session.execute(f'UPDATE  Jogador SET valor = (valor * {1.26}) where kills > {1000}')



def incluir(classe):
    dados = request.get_json(force=True)

    try: 
      if classe == "Time":
        nova = Time(**dados) 
      elif classe == "Professor":
        
        nova = Jogador(**dados) 
  
        
      db.session.add(nova)
      db.session.commit()


    except Exception as e: 
      
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})


    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 
  
    
@app.route('/listar/<string:classe>')

def listar_tudo(classe):
    if classe == 'Jogador':
            
        calcular()
        dados = db.session.query(Jogador).all()()

    elif classe == 'Time':
        dados = db.session.query(Time).all()

    lista_jsons = [x.json() for x in dados]
    resposta =jsonify(lista_jsons)
    
    resposta.headers.add("Access-Control-Allow-Origin" ,server)
    return resposta

@app.route('/listar_jogador_semtime/<string:classe>/<string:jogador_nome>')

def listar_jogador_semtime(classe,jogador_nome):
    try:
        if classe == "Jogador":
            jt= Jogador.times_id == None
            jn = Jogador.nome == jogador_nome
            dados = db.session.query(Jogador).filter(jt,jn).all()#pegando jogador sem time e pelo seu nome 
    except error as e:
        print('Erro' , e)
        
    lista_jsons = [ x.json() for x in dados ]
    resposta = jsonify(lista_jsons)
    resposta.headers.add("Access-Control-Allow-Origin" ,server)
    return resposta
    # Teste = curl localhost:5000/listar_jogador_semtime/Jogador/Showmaker
app.run(debug=True, host="0.0.0.0")
