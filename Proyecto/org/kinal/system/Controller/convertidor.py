import sys
sys.path.append("C:\\Users\\Javier\\OneDrive - Fundación Kinal -Alumnos-\\Desktop\\Proyecto")
from org.kinal.system.View import mainFrame
from tkinter import filedialog
import tkinter as tk
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def abrir():
    root = tk.Tk()
    root.withdraw()  
    
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        print("Se seleccionó el archivo:", file_path)
        with open(file_path, 'r') as file:
            enunciado = file.read()
        mainFrame.entrada1.insert("1.0",enunciado)
        return enunciado
    else:
        print("No se seleccionó ningún archivo.")

def guardar():
    resultado = convertir_entry_to_db() 
    ruta_default = "..org"
    
    ruta_archivo = filedialog.asksaveasfilename(initialdir=ruta_default, defaultextension=".sql", filetypes=[("Archivos SQL", "*.sql")])
    if ruta_archivo:
        with open(ruta_archivo, "w") as file:
            file.write(resultado)

def salir():
    mainFrame.window.quit()

def convertir_entry_to_db():
    enunciado = mainFrame.entrada1.get("1.0", tk.END)
    resultado = procesar_frase(enunciado)
    mainFrame.entrada2.delete("1.0", tk.END)
    mainFrame.entrada2.insert("1.0", resultado) 
    return resultado   


def procesar_frase(frase):
    palabras = word_tokenize(frase.lower())  

    stop_words = set(stopwords.words('spanish'))
    palabras_filtradas = [palabra for palabra in palabras if palabra not in stop_words]

    mapeo_general = {
        "crear": "CREATE",
        "crea": "CREATE",
        "hacer": "CREATE",
        "has": "CREATE",
        "datos": "DATABASE",
        "entidad": "CREATE TABLE",
        "motor": ")Engine",
        "innodb": "InnoDB;\n \n",
        "numerico": "INT",
        "texto": "VARCHAR",
        "buleana": "BOOLEAN",
        
        
    }

    salida = []
    
    nombre_base_datos = ""
    nombre_entidad = ""
    nombre_atributo = ""
    parametro_atributo = ""
    procesando_nombre_base_datos = False
    procesando_nombre_entidad = False
    procesando_atributo = False  
    procesando_tipo_variable = False  
    procesando_tipo_parametro = False
    tipo_variable = None
    atributos = []
    
    for i, palabra in enumerate(palabras_filtradas):
        if palabra in mapeo_general:
            salida.append(mapeo_general[palabra])
        elif palabra in ["llame"] and i < len(palabras_filtradas) - 1:
            nombre_base_datos = palabras_filtradas[i + 1]
            procesando_nombre_base_datos = True
            if nombre_base_datos:
                salida.append("{};\n \n".format(nombre_base_datos))  
                print(nombre_base_datos + "1")
        elif procesando_nombre_base_datos:
            nombre_base_datos = palabra
            procesando_nombre_base_datos = False
        elif palabra in ["nombre", "llamada"] and i < len(palabras_filtradas) - 1:
            nombre_entidad = palabras_filtradas[i + 1]
            procesando_nombre_entidad = True
            if nombre_entidad:
                salida.append(" {}(\n".format(nombre_entidad))  
                i += 1
        elif palabra in ["atributo"] and i < len(palabras_filtradas) - 1:
            nombre_atributo = palabras_filtradas[i + 1]
            procesando_atributo = True
            if nombre_atributo:
                salida.append("{} ".format(nombre_atributo))  
                i += 1
        elif palabra in ["numeros","caracteres"] and i > 0:
            parametro_atributo = palabras_filtradas[i - 1]
            procesando_tipo_parametro = True
            if parametro_atributo:
                salida.append("({}),\n".format(parametro_atributo))
        elif palabra in ["inicie","empiece","comience","en"] and i > 0:
            parametro_atributo = palabras_filtradas[i + 1]
            if parametro_atributo in ["verdadero", "True", "true", "Verdadero"]:
                salida.append("True,\n")
            elif parametro_atributo in ["falso", "False", "false", "Falso"]:
                salida.append("False,\n")        
    
    print(salida)    
    return " ".join(salida)





