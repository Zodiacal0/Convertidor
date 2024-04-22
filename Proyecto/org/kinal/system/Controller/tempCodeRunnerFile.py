        parametro_atributo = palabras_filtradas[i - 1]  # Cambio aquí
            procesando_tipo_parametro = True
            if parametro_atributo in ["verdadero","True","true","Verdadero"]:
                salida.append("{},\n".format(parametro_atributo))
            elif parametro_atributo in ["falso","False","false","Falso"]:
                salida.append("{},\n".format(parametro_atributo))