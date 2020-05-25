from flask import Flask,request
from flask_restful import Resource,Api
from habilidades import Habilidades,Habilidade,validarHabilidades
import json
app=Flask(__name__)
api=Api(app)


desenvolvedores=[{'nome':'Thiago','habilidades':['Delphi','PHP']}
    ,{'nome':'Miguel','habilidades':['Python','Django']}]

class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response=desenvolvedores[id]
        except IndexError:
            mensagem='Desenvolvedor de ID {} não existe'.format(id)
            response={'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status':'erro', 'mensagem':mensagem}
        return response
    def put(self,id):
        dados= json.loads(request.data)
        valid=validarHabilidades(dados)
        if valid['status']==True:
            desenvolvedores[id]=dados
            return dados
        else:
            return {'status':'erro','menagem':'Habilidades não encontradas, faço o cadastro',
                    'habilidades':valid['habilidades']}
    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status':'sucesso registro excluído'}

class Lista_Desenvolvedores(Resource):
    def post(self):
        dados= json.loads(request.data)
        valid=validarHabilidades(dados)
        if valid['status']==True:
            posicao=len(desenvolvedores)
            dados['id']=posicao
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]
        else:
            return {'status':'erro','mensagem':'Habilidades não encontradas, faço o cadastro','habilidades':valid['habilidades']}
    def get(self):
        return desenvolvedores





api.add_resource(Desenvolvedor,'/dev/<int:id>')
api.add_resource(Lista_Desenvolvedores,'/dev/')
api.add_resource(Habilidades,'/habilidades/')
api.add_resource(Habilidade,'/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)