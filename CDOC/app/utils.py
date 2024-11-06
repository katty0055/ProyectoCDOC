# app/utils.py

import re
import os

def parse_comments_from_file(file_path):
    comments = []
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
            html_file.write("<head><title>Documentación de archivo</title></head>\n")
            html_file.write("<body>\n")
            html_file.write("<h1>Documentación de division.c</h1>\n")
            html_file.write("<br/><hr/><br/>\n")

            for comment in comments:
                print("comienzo")
                print(comment)
                lines = comment.splitlines()
                function_name = ""
                params = []
                returns = ""
                error = ""
                extra = ""

                # for line in lines:
                #     line = line.strip()
                #     if line.startswith('@name'):
                #         function_name = line[len('@name '):].strip()  # Aseguramos que no haya espacios
                #     elif line.startswith('@param'):
                #         param_desc = line[len('@param '):].strip()
                #         params.append(param_desc)
                #     elif line.startswith('@return'):
                #         returns = line[len('@return '):].strip()
                #     elif line.startswith('@error'):
                #         error = line[len('@error '):].strip()
                #     elif line.startswith('@extra'):
                #         extra = line[len('@extra '):].strip()

                # if function_name:  # Solo crea la tabla si hay un nombre de función
                #     # Generar tabla para la función
                #     html_file.write("<table border='1'>")
                #     html_file.write(f"<tr><td>Nombre</td><td><b>{function_name}</b><br/>{extra}</td></tr>")

                #     for param in params:
                #         param_name = param.split()[0]  # El primer elemento es el nombre del parámetro
                #         param_desc = ' '.join(param.split()[1:])  # El resto es la descripción
                #         html_file.write(f"<tr><td>Parámetro</td><td><b>{param_name}</b><br/>{param_desc}</td></tr>")

                #     if returns:
                #         html_file.write(f"<tr><td>Retorna</td><td>{returns}</td></tr>")
                #     if error:
                #         html_file.write(f"<tr><td>Error</td><td>{error}</td></tr>")

                #     html_file.write("</table>")
                #     html_file.write("<br/><hr/><br/>")

            html_file.write("</body>\n")
            html_file.write("</html>\n")
    except Exception as e:
        print(f"Error al generar el archivo HTML en {output_path}: {e}")