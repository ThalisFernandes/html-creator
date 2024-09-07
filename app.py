from flask import Flask
from flask import request
from generate_document import *
from io import BytesIO
import ast
app = Flask(__name__)


@app.route('/')
def init()-> str:
    return "<p>Opá funcionou</p>"

@app.route('/about')
def about()-> str:
    return "<p> This page show how to generate a a HTML site using this API</p>"

"""
 {
    header: {
        type: numero de layout escolhido,
        title: nome do titulo do cabeçalho,
        button: [ //array de objetos
            {
                button_name: nome do buttão 
            }
        ]
    },
    body: {
        type: numero do layout escolhido,
        elements: [
            {
                img?: url para imagem,
                desc?: texto para a descrição da imagem
                button?: nome do button
                id?: id para ser atribuido ao elemento
                class?: class para ser atribuida ao elemento caso você queira adicionar bootstrap 
            }
        ]
    },
    footer: {
        type: numero do layout escolhido,
        social_media_links: {
            facebook?: url para o facebook,
            linkedin?: url para o linkedin,
            instagram?: url para o instagram,
            twitter?: url para o twitter
        },
        
    }
 }

"""
@app.route('/generate', methods=["GET", "POST"])
def generate()-> str:
    print(type(request.data))
    bytes_data = request.data
    dict_str = bytes_data.decode("UTF-8")
    request_data = ast.literal_eval(dict_str)
    if request_data["header"]:
        documento = generate_main_element(request_data["header"]["title"], request_data["header"],{}, {})
        with open(f'./temp/{request_data["header"]["title"]}.html', 'w') as file:
            file.write(documento)
            file.close()
    with open(f'./temp/{request_data["header"]["title"]}.html', 'rb') as stream:
        stream_file = BytesIO(stream.read())

    print(stream_file)

    return f"<p> rota para gerar site</p> </br> <div><a href='./temp/{request_data['header']['title']}.html'>download file</a></div>"