# app/utils.py

import re
import os

def parse_comments_from_file(file_path):
    comments = []
    #convierte a expresion regular y captura lo que comienza con /** y terminan con */
    comment_pattern = re.compile(r'/\*\*(.*?)\*/', re.DOTALL)
    
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            content = file.read()
            matches = comment_pattern.findall(content)
            for match in matches:
                comments.append(match.strip())
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo {file_path}: {e}")
    
    return comments

def generate_html_documentation(comments, output_path):
    """
    Genera un archivo HTML con la documentación basada en los comentarios.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        with open(output_path, 'w', encoding='UTF-8') as html_file:
            html_file.write("<html>\n")
            html_file.write("<head><meta charset='UTF-8'>\n<title>Documentación de archivo</title></head>\n")
            html_file.write("<body>\n")
            html_file.write("<h1>Documentación de division.c</h1>\n")
            html_file.write("<br/><hr/><br/>\n")

            function_name = ""
            params = []
            returns = ""
            error = ""
            extra = ""
            ultimo_parametro = ""

            # Expresión regular para capturar líneas que empiezan con "* "
            pattern = re.compile(r'\*\s*(.*)')          


            #Recorremos cada comentario
            for comment in comments:
                print("comienzo")
                print(comment)
                
                #Separa por salto de linea            
                for line in comment.splitlines():
                    print("line")
                    print(line)
                    #Separacion del texto
                    match = pattern.match(line)
                    # print(match.group(1))
                    if match:
                        if match.group(1).startswith('@name'):
                            print("1")
                            function_name = match.group(1).replace('@name ', '', 1)
                            ultimo_parametro = 'function_name'
                        elif match.group(1).startswith('@param'):
                            print("2")
                            params.append(match.group(1).replace('@param ', '', 1))
                            ultimo_parametro = 'params'
                        elif match.group(1).startswith('@return'):
                            print("3")
                            returns = match.group(1).replace('@return ', '', 1)
                            ultimo_parametro = 'returns'
                        elif match.group(1).startswith('@error'):
                            print("4")
                            error = match.group(1).replace('@error ', '', 1)
                            ultimo_parametro = 'error'
                        elif match.group(1).startswith('@extra'):
                            print("5")
                            extra = match.group(1).replace('@extra ', '', 1)
                            ultimo_parametro = 'extra'
                    else:
                        # Si no coincide con ninguna etiqueta y `ultimo_parametro` está definido
                        if ultimo_parametro == 'function_name':
                            function_name += " " + line
                        elif ultimo_parametro == 'params' and params:
                            params[-1] += " " + line
                        elif ultimo_parametro == 'returns':
                            returns += " " + line
                        elif ultimo_parametro == 'error':
                            error += " " + line
                        elif ultimo_parametro == 'extra':
                            extra += " " + line
                # Solo crea la tabla si hay un nombre de función
                if function_name:  
                    # Generar tabla para la función
                    html_file.write("<table border='1'>\n")
                    # El primer elemento es el nombre de la funcion
                    function_name_name = function_name.split()[0]  
                    # El resto es la descripción
                    function_name_desc = ' '.join(function_name.split()[1:])  
                    html_file.write(f"<tr>\n<td>Parámetro</td>\n<td><b>{function_name_name}</b><br/>{function_name_desc}</td>\n</tr>\n")

                    for param in params:
                        # El primer elemento es el nombre del parámetro
                        param_name = param.split()[0]  
                        # El resto es la descripción
                        param_desc = ' '.join(param.split()[1:])  
                        html_file.write(f"<tr>\n<td>Parámetro</td>\n<td><b>{param_name}</b><br/>{param_desc}</td>\n</tr>\n")

                    if returns:
                        html_file.write(f"<tr><td>Retorna</td>\n<td>{returns}</td>\n</tr>\n")
                    if error:
                        html_file.write(f"<tr><td>Error</td>\n<td>{error}</td>\n</tr>\n")
                    if extra:
                        html_file.write(f"<tr><td>Doc. adicional</td>\n<td>{extra}</td>\n</tr>\n")

                    html_file.write("</table>\n")
                    html_file.write("<br/><hr/><br/>\n")


            html_file.write("</body>\n")
            html_file.write("</html>\n")
    except Exception as e:
        print(f"Error al generar el archivo HTML en {output_path}: {e}")