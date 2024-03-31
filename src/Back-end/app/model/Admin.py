from datetime import datetime

class Admin():
  
    def __init__(self, **kwargs):
        self.email = kwargs['email']
        self.nome = kwargs['nome']
        self.data_cadastro = datetime.now().strftime("%d/%m/%Y - %H:%M")
        self.data_atualizacao = datetime.now().strftime("%d/%m/%Y - %H:%M") 
    

    @staticmethod
    def verify_new_admin_data(data: dict):

        available_keys = ['email','nome']

        data_keys = data.keys()

        if len(data_keys) != 2:
            return f'há campos faltantes no corpo da requisição.'

        wrong_keys = [key for key in data_keys if key not in available_keys]

        if wrong_keys:
            return f'Campos incorretos inseridos na requisição: {wrong_keys}'
        
        none_values = {key for key in data if not data[key]}

        if none_values:
            return f'Foi atribuido um valor nulo nas seguintes propriedades: {none_values}'
        
        wrong_values = none_values = {key for key in data if type(data[key]) is not str and type(data[key]) is not list }

        if wrong_values:
            return f'Valores incorretos foram atribuidos as seguintes propriedades: {none_values}'