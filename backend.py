
from modelo import *
from config import *

@app.route("/")

def inicio():
    return 'Funcionando'

@app.route('/listar/<string:classe>')
def listar_tudo(classe):
    if classe == 'Jogador':
            
            #db.session.execute('UPDATE  Jogador SET valor = 100 where titulos < 6')
            dados = db.session.query(Jogador).all()

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
