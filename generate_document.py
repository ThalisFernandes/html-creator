from generate_body import *
from generate_footer import *

def generate_doc()->str:
    return 'teste'

def generate_main_element(title, header_dict, body_dict, footer_dict)-> str:
    header = generate_header(title, header_dict)
    #body = generate_body(body_dict)
    #footer = generate_footer(footer_dict)
    header_html = header["html"]
    header_css = header["css"]
    body_css = ''
    body_html = ''
    footer_css = ''
    footer_html = ''
    document = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <style>
            {header_css if header_css is not None else ''}
            {body_css if body_css is not None else ''}
            {footer_css if footer_css is not None else ''}
        </style>
        <body>
            {header_html if header_html is not None else ''}
            {body_html if body_html is not None else ''}
            {footer_html if footer_html is not None else ''}
        </body>
        </html>
    '''
    # with open(f'./temp/{title}.html', 'w') as file:
    #     file.write(element_body)
    return document

def generate_header(title, header_obj) -> dict:
    titulo = title
    header_style = header_obj["type"]
    header_string = ""
    header_css = ''
    css_base = '''
        .header {
                background-color: #333;
                color: white;
                padding: 20px;
                text-align: center;
            }
    '''
    final_css_header = ''
    if header_style:
        if header_style == "1":
            print("Entrou no 1")
            print(header_obj["button"][0]["button_name"] )
            header_string = f'''
                <div class="header"> 
                    <h1>{titulo}</h1>
                    <button class="button">{header_obj["button"][0]["button_name"] if header_obj["button"][0]["button_name"] else 'Button1'}</button>
                    <button class="button">{header_obj["button"][1]["button_name"] if header_obj["button"][1]["button_name"] else 'Button2'}</button>
                    <button class="button">{header_obj["button"][2]["button_name"] if header_obj["button"][2]["button_name"] else 'Button3'}</button>
                    <button class="button">{header_obj["button"][3]["button_name"] if header_obj["button"][3]["button_name"] else 'Button4'}</button>
                </div>'''
            
            header_css = '''
                .button {
                    background-color: #4CAF50;
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                }
            '''
            final_css_header = ''.join([css_base, header_css])
        elif header_style == '2':
            header_string = f'''
                <div class="header">
                    <h1>{titulo}</h1>
                </div>
                
                <div class="navbar">
                    <a href="#">Home</a>
                    <a href="#">About</a>
                    <a href="#">Services</a>
                    <a href="#">Contact</a>
                </div>
            '''
            header_css = '''
                .navbar {
                    overflow: hidden;
                    background-color: #333;
                }

                /* Style the links inside the navbar */
                .navbar a {
                    float: left;
                    display: block;
                    color: white;
                    text-align: center;
                    padding: 14px 20px;
                    text-decoration: none;
                }

                /* Change color on hover */
                .navbar a:hover {
                    background-color: #ddd;
                    color: black;
                }
            '''
            final_css_header = ''.join([css_base, header_css])
        elif header_style ==  3:
            header_string = f'''
                <div class="header">
                    <h1>{titulo}</h1>
                    <div class="search-container">
                        <input type="text" placeholder="Search...">
                        <button type="submit">{button}</button>
                    </div>
                </div>            
            '''
            header_css = '''

            '''
            final_css_header = ''.join([css_base, header_css])
        else: 
            header_string = '''            
                <div class="header">
                    <h1>Estilho de cabeçalho invalido</h1>
                </div>
            '''
    header_dict = {"html": header_string, "css": header_css}
    return header_dict