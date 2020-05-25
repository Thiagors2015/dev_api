from flask_restful import Resource
from flask import request
import json

lista_habilitades=['Python','Java']
class Habilidades(Resource):
    def get(self):
        return lista_habilitades
    def post(self):
        dados = json.loads(request.data)
        try:
            pos = lista_habilitades.index(dados['habilidade'])
        except ValueError:
            pos=-1
        if pos<0:
            lista_habilitades.append(dados['habilidade'])
            mensagem = 'Habilidade incluída com sucesso'
            retorno = {'status': 'sucesso', 'mensagem': mensagem}
        else:
            mensagem = 'Habilidade já exite'
            retorno = {'status': 'erro', 'mensagem': mensagem}
        return retorno

class Habilidade(Resource):
    def delete(self,id):
        try:
            lista_habilitades.pop(id)
            mensagem = 'Habilidade Excluída com sucesso'
            retorno = {'status': 'sucesso', 'mensagem': mensagem}
        except IndexError:
            mensagem = 'Habilidade não foi encontrada'
            retorno = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro não identificado'
            retorno = {'status': 'erro', 'mensagem': mensagem}
        return retorno
    def put(self,id):
        try:
            dados = json.loads(request.data)
            try:
                pos = lista_habilitades.index(dados['habilidade'])
            except ValueError:
                pos = -1
            if pos < 0:
                lista_habilitades[id] = dados['habilidade']
                mensagem = 'Habilidade alterada com sucesso'
                retorno = {'status': 'sucesso', 'mensagem': mensagem}
            else:
                mensagem = 'Habilidade não foi alterada, habilidade informada já existe'
                retorno = {'status': 'erro', 'mensagem': mensagem}
        except IndexError:
            mensagem = 'Habilidade não foi encontrada'
            retorno = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro não identificado'
            retorno = {'status': 'erro', 'mensagem': mensagem}
        return retorno

def validarHabilidades(dados):
        achou=True
        naoAchou=[]
        for x in dados['habilidades']:
            if x not in lista_habilitades:
                naoAchou.append(x)
                achou=False
        if achou:
            return {'status':achou}
        else:
            return {'status':achou,'habilidades':naoAchou}