from flask_restful import Resource
from flask import request
import json

lista_habilitades=[{'Python','Java'}]

class Habilidades(Resource):
    def get(self):
        return lista_habilitades
    def post(self):
        dados=json.loads(request.data)
        lista_habilitades.append(dados)
    def put(self,hbAnt,hbNova):
        posicao=lista_habilitades.index(hbAnt)
        if posicao>=0:
            lista_habilitades[posicao]=hbNova
            mensagem='Habilidade {} alterada para {} com sucesso.'.format(hbAnt,hbNova)
            resposta={'status':'sucesso','mensagem':mensagem}
        else:
            mensagem = 'Erro habilidade {} não foi encontrada'.format(hbAnt)
            resposta = {'status': 'erro', 'mensagem': mensagem}
        return resposta
    def delete(self,hbAnt):
        posicao = lista_habilitades.index(hbAnt)
        if posicao >= 0:
            lista_habilitades.pop(posicao)
            mensagem = 'Habilidade {} excluída com sucesso.'.format(hbAnt)
            resposta = {'status': 'sucesso', 'mensagem': mensagem}
        else:
            mensagem = 'Erro habilidade {} não foi encontrada'.format(hbAnt)
            resposta = {'status': 'erro', 'mensagem': mensagem}
        return resposta

