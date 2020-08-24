from flask import Flask
from flask_restful import Resource,Api
import random

app = Flask(__name__)
api = Api(app)

class GerarSenha(Resource):
    def __init__(self):
        self.caracteres = [
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            '*','_','@','Ç','#','&','$',
            '0','1','2','3','4','5','6','7','8','9'
        ]
        self.senha = ''

    def get(self,tamanho_senha):
        if tamanho_senha <= 63:
            while len(self.senha) < tamanho_senha:
                self.senha += random.choice(self.caracteres)
            return {'status':'sucesso','senha':self.senha}
        else:
            return {'status':'erro','msg':'o tamanho da senha não é permitido'}

api.add_resource(GerarSenha,'/<int:tamanho_senha>/')

if __name__ == '__main__':
    app.run(debug=True)