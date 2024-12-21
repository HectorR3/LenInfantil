from lenguajeInfantilParser import lenguajeInfantilParser
from lenguajeInfantilListener import lenguajeInfantilListener
from antlr4 import TerminalNode
import time
class inlenIngtoPy(lenguajeInfantilListener):
    def __init__(self):
        self.codePy = ""
        self.indent_level = 0  # Variable para rastrear el nivel de sangría
        self.current_expression=""
        self.imports_added = False
    #GENERA LA SANGRÍA
    def addIndentation(self):
        return "    " * self.indent_level  

    # Enter a parse tree produced by lenguajeInfantilParser#programa.
    def enterPrograma(self, ctx:lenguajeInfantilParser.ProgramaContext):
        # print( 'No es raiz' if ctx.parentCtx is not None else 'Es raiz')
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#programa.
    def exitPrograma(self, ctx:lenguajeInfantilParser.ProgramaContext):
        # print(self.codePy)
        with open("salida.py", "w") as file:
            file.write(self.codePy)
        


    # Enter a parse tree produced by lenguajeInfantilParser#declaracion.
    def enterDeclaracion(self, ctx:lenguajeInfantilParser.DeclaracionContext):
        
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#declaracion.
    def exitDeclaracion(self, ctx:lenguajeInfantilParser.DeclaracionContext):
        if ctx.DECLARAR_CONSTANTE():
            # Estructura: tipo_dato = valor
            var_name = ctx.ID().getText()
            value_ctx = ctx.valor()
            
            # Procesamos el valor
            if value_ctx.NUMERO():
                value = value_ctx.NUMERO().getText()
            elif value_ctx.TEXTO():
                value = value_ctx.TEXTO().getText()
            elif value_ctx.VERDADERO():
                value = 'True'
            elif value_ctx.FALSO():
                value = 'False'
            elif value_ctx.ID():
                value = value_ctx.ID().getText()
            else:
                value = 'None'  # Valor por defecto

            # Generamos código en mayúsculas para constantes
            const_line = f"{var_name.upper()} = {value}\n"
            self.codePy += const_line
            print(f"Declaración de constante: {const_line.strip()}")  # Debugging
        elif ctx.DECLARAR():
            # Estructura: declarar ID como tipo_dato
            var_name = ctx.ID().getText()
            # Inicializamos con un valor por defecto según el tipo
            default_values = {
                'int': '0',
                'float': '0.0',
                'str': '""',
                'bool': 'False',
                'list': '[]'
            }
            default_value = default_values.get(self.current_type, 'None')
            var_line = f"{var_name} = {default_value}\n"
            self.codePy += var_line
            print(f"Declaración de variable: {var_line.strip()}")  # Debugging

        # Reiniciamos el tipo actual después de la declaración
        self.current_type = None



    # Enter a parse tree produced by lenguajeInfantilParser#tipo_dato.
    def enterTipo_dato(self, ctx:lenguajeInfantilParser.Tipo_datoContext):
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#tipo_dato.
    def exitTipo_dato(self, ctx: lenguajeInfantilParser.Tipo_datoContext):
        tipo = ctx.getText()
        # Mapeo de tipos 
        tipo_map = {
            'NumeroEntero': 'int',
            'NumeroDecimal': 'float',
            'Texto': 'str',
            'VerdaderoFalso': 'bool',
            'lista': 'list'
        }
        self.current_type = tipo_map.get(tipo, 'object')  # Por defecto 'object' si no se encuentra
        
        #RECORDAR BORRAR ESTO SOLO ES PARA SABER SI ENTRA
        print(f"Tipo detectado: {self.current_type}") 



    # Enter a parse tree produced by lenguajeInfantilParser#valor.
    def enterValor(self, ctx:lenguajeInfantilParser.ValorContext):
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#valor.
    def exitValor(self, ctx:lenguajeInfantilParser.ValorContext):
        pass


    # Enter a parse tree produced by lenguajeInfantilParser#sentencia.
    def enterSentencia(self, ctx:lenguajeInfantilParser.SentenciaContext):
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#sentencia.
    def exitSentencia(self, ctx:lenguajeInfantilParser.SentenciaContext):
        
        pass


    # Enter a parse tree produced by lenguajeInfantilParser#asignacion.
    def enterAsignacion(self, ctx:lenguajeInfantilParser.AsignacionContext):
        self.codePy+= "\n"      
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#asignacion.
        # Exit a parse tree produced by lenguajeInfantilParser#asignacion.
    def exitAsignacion(self, ctx: lenguajeInfantilParser.AsignacionContext):
        # Extraer identificador y valor asignado
        # id_ = ctx.ID().getText()
        # asignacion = ctx.getChild(2).getText()  # Valor u operación
        
        # # Verificamos si el valor es 'verdadero' o 'falso' y lo convertimos
        # if asignacion.lower() == "verdadero":
        #     asignacion = "True"
        # elif asignacion.lower() == "falso":
        #     asignacion = "False"

        # # Agregar la línea de asignación con indentación
        # asignacion_line = f"{self.addIndentation()}{id_} = {asignacion}\n"
        # self.codePy += asignacion_line

        # print(f"Debug: Asignación generada: {asignacion_line.strip()}")
        pass



    # Enter a parse tree produced by lenguajeInfantilParser#operacion.
    def enterOperacion(self, ctx:lenguajeInfantilParser.OperacionContext):
        self.codePy+= "\n"
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#operacion.
    def exitOperacion(self, ctx: lenguajeInfantilParser.OperacionContext):
        current = ctx.parentCtx
        count = 0
        asing=''
        while current is not None:
            count+=1
            current = current.parentCtx 
        
        if(count <= 2):
            # print(f'numero de subidas para llegar a la raiz {count} del token = {ctx.getText()}')
            asing+=ctx.getText()
            self.codePy += asing
        else:        
            pass

    # def process_sentencia(self, ctx):
    #     if ctx.asignacion():
    #         return self.process_asignacion(ctx.asignacion())  # Procesa asignaciones
    #     elif ctx.operacion():
    #         return self.process_operacion(ctx.operacion())    # Procesa operaciones
    #     elif ctx.condicional():
    #         return self.process_condicional(ctx.condicional())  # Procesa condicionales
    #     elif ctx.mostrar():
    #         return self.process_mostrar(ctx.mostrar())        # Procesa mostrar
    #     return ""  # Retorna cadena vacía si no hay coincidencia


    def process_mostrar(self, ctx):
        # Obtener el contenido del nodo (el valor a mostrar)
        valor = ctx.getChild(1).getText()  # El segundo hijo contiene el valor
        return f"print({valor})"

    def process_asignacion(self, ctx):
        # Obtiene el identificador y la operación/valor asignado
        id_ = ctx.ID().getText()
        asignacion = ctx.getChild(2).getText()  # Captura la operación o valor

        # Generar el código en Python con indentación
        return f"{self.addIndentation()}{id_} = {asignacion}"


    def process_operacion(self, ctx):
        operacion = ctx.getText()
        operacion = operacion.replace("^", "**")

        print("OPERACIONNN"+operacion)
        return operacion

    def process_condicional(self, ctx):
        # Obtener la condición con reemplazo de operadores
        condicion = ctx.expresion().getText()
        condicion = condicion.replace("mayorque", ">") \
                            .replace("menorque", "<") \
                            .replace("mayorigualque", ">=") \
                            .replace("menorigualque", "<=") \
                            .replace("igual", "==") \
                            .replace("diferente", "!=")

        # Incrementar la indentación para el bloque `if`
        self.indent_level += 1
        programa_si = self.process_programa(ctx.programa(0),False)
        self.indent_level -= 1

        result = f"{self.addIndentation()}if ({condicion}):\n{programa_si}"

        # Procesar el bloque `else`, si existe
        if ctx.SINO():
            self.indent_level += 1
            programa_sino = self.process_programa(ctx.programa(1))
            self.indent_level -= 1
            result += f"{self.addIndentation()}else:\n{programa_sino}"

        return result




    # def process_programa(self, programa_ctx):
    #     result = ""  # Almacena el código generado en Python

    #     # Iterar sobre todos los hijos de 'programa'
    #     for child in programa_ctx.getChildren():
    #         if isinstance(child, TerminalNode):
    #             continue  # Ignorar terminales como NEWLINE o WS

    #         rule_index = child.getRuleIndex()
    #         rule_name = lenguajeInfantilParser.ruleNames[rule_index]

    #         # Procesar cada sentencia
    #         if rule_name == "sentencia":
    #             sentencia_code = self.process_sentencia(child)
    #             result += f"{self.addIndentation()}{sentencia_code}\n"  # Añadir indentación aquí
    #         else:
    #             print(f"Regla no soportada: {rule_name}")  # Debugging para reglas no manejadas

    #     return result

    def process_sentencia(self, ctx):
        if ctx.asignacion():
            return self.process_asignacion(ctx.asignacion())  # Procesa asignaciones
        elif ctx.operacion():
            return self.process_operacion(ctx.operacion())    # Procesa operaciones
        elif ctx.condicional():
            return self.process_condicional(ctx.condicional())  # Procesa condicionales
        elif ctx.mostrar():
            return self.process_mostrar(ctx.mostrar())
        elif ctx.ciclo():
            return self.process_ciclo(ctx.ciclo())        # Procesa mostrar
        return ""  # Retorna cadena vacía si no hay coincidencia

    def process_ciclo(self, ctx):
        if ctx.REPITE():  # Ciclo 'repetir'
            # Obtener el número de repeticiones
            veces = ctx.NUMERO().getText()
            bloque = self.process_programa(ctx.programa(), False)
            # Generar el código en Python para el ciclo 'for'
            return f"for _ in range({veces}):\n{bloque}"

        elif ctx.MIENTRAS():  # Ciclo 'mientras'
            # Obtener la condición con reemplazo de operadores
            condicion = ctx.expresion().getText()
            condicion = condicion.replace("mayorque", ">") \
                                .replace("menorque", "<") \
                                .replace("mayorigualque", ">=") \
                                .replace("menorigualque", "<=") \
                                .replace("igual", "==") \
                                .replace("diferente", "!=")

            bloque = self.process_programa(ctx.programa(), False)
           
            return f"while {condicion}:\n{bloque}"

        return ""


    def process_mostrar(self, ctx):
        valor = ctx.getChild(1).getText()  # El segundo hijo contiene el valor
        return f"print({valor})"

    def process_asignacion(self, ctx):
        id_ = ctx.ID().getText()
        asignacion = ctx.getChild(2).getText()

        
        return f"{self.addIndentation()}{id_} = {asignacion}"


    # def process_operacion(self, ctx):
        operacion = ctx.getText()
        operacion = operacion.replace("mayorque", ">") \
                            .replace("menorque", "<") \
                            .replace("mayorigualque", ">=") \
                            .replace("menorigualque", "<=") \
                            .replace("igual", "==") \
                            .replace("diferente", "!=")
        return operacion

    def process_condicional(self, ctx):
        condicion = ctx.expresion().getText()
        condicion = condicion.replace("mayorque", ">") \
                            .replace("menorque", "<") \
                            .replace("mayorigualque", ">=") \
                            .replace("menorigualque", "<=") \
                            .replace("igual", "==") \
                            .replace("diferente", "!=")

        self.indent_level += 1
        programa_si = self.process_programa(ctx.programa(0),False)
        self.indent_level -= 1

        result = f"{self.addIndentation()}if ({condicion}):\n{programa_si}"

        if ctx.SINO():
            self.indent_level += 1
            programa_sino = self.process_programa(ctx.programa(1),False)
            self.indent_level -= 1
            result += f"{self.addIndentation()}\telse:\n{programa_sino}"

        return result




    def process_programa(self, programa_ctx,bandera):
        result = "" 

        for child in programa_ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue

            rule_index = child.getRuleIndex()
            rule_name = lenguajeInfantilParser.ruleNames[rule_index]

            # Procesar cada sentencia
            if rule_name == "sentencia":
                sentencia_code = self.process_sentencia(child)
                result += f"\t{sentencia_code}\n" if (bandera) else f"{"\t"*2}{sentencia_code}\n" # Añadir indentación aquí
            else:
                print(f"Regla no soportada: {rule_name}")

        return result



    # Enter a parse tree produced by lenguajeInfantilParser#condicional.
    def enterCondicional(self, ctx:lenguajeInfantilParser.CondicionalContext):
        self.codePy += "\n"
        pass

    def exitCondicional(self, ctx:lenguajeInfantilParser.CondicionalContext):
        current = ctx.parentCtx
        count = 0

        while current is not None:
            count += 1
            current = current.parentCtx

        if(count <= 2):
            condicion = ctx.expresion().getText()
            condicion = condicion.replace("mayorque", ">") \
                                .replace("menorque", "<") \
                                .replace("mayorigualque", ">=") \
                                .replace("menorigualque", "<=") \
                                .replace("igual", "==") \
                                .replace("diferente", "!=")

            # Bloque para "si"
            programa_si = self.process_programa(ctx.programa(0),True if(count <= 2) else False)
            asig = f"\nif ({condicion}):\n{programa_si}"
            # Bloque para "sino", si existe
            if ctx.SINO():
                programa_sino = self.process_programa(ctx.programa(1),True if(count <= 2) else False)
                asig += f"\nelse:\n{programa_sino}"

            self.codePy += asig

    def enterCiclo(self, ctx: lenguajeInfantilParser.CicloContext):
        parents = ctx.parentCtx
        count = 0
        while(parents is not None):
            count += 1
            parents = parents.parentCtx
        

        if(count<=2):
            if ctx.REPITE():
                print(f"Lista de programas: {ctx.programa()}")
                num_veces = ctx.NUMERO().getText()
                self.codePy += f"{self.addIndentation()}for _ in range({num_veces}):\n{self.process_programa(ctx.programa(),True if count <= 2 else False)}"
                self.indent_level += 1
            elif ctx.MIENTRAS():
                print(f"Lista de programas del MIENTRAS: {ctx.programa()}")
                self.current_expression = ""
                self.exitExpresion(ctx.expresion())
                condicion = self.current_expression
                self.codePy += f"{self.addIndentation()}while {condicion}:\n{self.process_programa(ctx.programa(),True if count <= 2 else False)}"
                self.indent_level += 1
    


    # Exit a parse tree produced by lenguajeInfantilParser#ciclo.
    def exitCiclo(self, ctx: lenguajeInfantilParser.CicloContext):
        
        print('Salimos del CICLOOO!!')
        # Decrementa el nivel de sangría al salir del ciclo
        self.indent_level -= 1
        pass

    # Enter a parse tree produced by lenguajeInfantilParser#mostrar.
    def enterMostrar(self, ctx:lenguajeInfantilParser.MostrarContext):
        self.codePy+='\n'
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#mostrar.
    def exitMostrar(self, ctx:lenguajeInfantilParser.MostrarContext):
        current = ctx.parentCtx
        count = 0

        # Contar niveles para saber si estamos cerca de la raíz
        while current is not None:
            count += 1
            current = current.parentCtx

        if(count <= 2):
            contenido = ctx.getChild(1).getText()  # Captura el contenido después de "mostrar"
            self.codePy += f"{self.addIndentation()}print({contenido})\n"
            print("Entramos a mostrar: ")
            print(contenido)


    #Maneja la importación del time al inicio
    def addImports(self):
        if not self.imports_added:
            self.codePy = "import time\n" + self.codePy
            self.imports_added = True

    # Enter a parse tree produced by lenguajeInfantilParser#esperar.
    def enterEsperar(self, ctx: lenguajeInfantilParser.EsperarContext):
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#esperar.
    def exitEsperar(self, ctx: lenguajeInfantilParser.EsperarContext):
        self.addImports()  # Asegura que se agregue 'import time'
        segundos = ctx.NUMERO().getText()  # Captura el valor numérico
        timer_line = f"{self.addIndentation()}time.sleep({segundos})\n"
        self.codePy += timer_line
        print(f"Debug: Timer generado: {timer_line.strip()}")


    # Enter a parse tree produced by lenguajeInfantilParser#manejo_errores.
    def enterManejo_errores(self, ctx:lenguajeInfantilParser.Manejo_erroresContext):
            current = ctx.parentCtx
            count = 0

            # # Contar niveles para saber si estamos cerca de la raíz
            while current is not None:
                count += 1
                current = current.parentCtx

            if(count <= 2):
                asig = f""
                # print(ctx.INTENTAR())
                tryProgram = self.process_programa(ctx.programa(0),True)
                asig +=f"try:\n{tryProgram}"
                if(ctx.CAPTURAR()):
                    exceptProgram=self.process_programa(ctx.programa(1),True)
                    asig += f"\nexcept Exception as e:\n{exceptProgram}"
                self.codePy += asig

            # else: print("MANEJO DE ERRORES; ")
            pass

    # Exit a parse tree produced by lenguajeInfantilParser#manejo_errores.
    def exitManejo_errores(self, ctx:lenguajeInfantilParser.Manejo_erroresContext):
        pass


        # Enter a parse tree produced by lenguajeInfantilParser#funcion.
    def enterFuncion(self, ctx: lenguajeInfantilParser.FuncionContext):
        # Obtener el nombre de la función
        nombre_funcion = ctx.ID().getText()

        # Extraer parámetros si existen
        parametros_ctx = ctx.parametros()
        parametros = ""
        if parametros_ctx:
            parametros = ", ".join([p.getText() for p in parametros_ctx.ID()])

        # Agregar la definición de la función
        self.codePy += f"{self.addIndentation()}def {nombre_funcion}({parametros}):\n{self.process_programa(ctx.programa(),True)}"
        
        # Incrementar indentación para el cuerpo de la función
        self.indent_level += 1

    # Exit a parse tree produced by lenguajeInfantilParser#funcion.
    def exitFuncion(self, ctx: lenguajeInfantilParser.FuncionContext):
        # Decrementar la indentación al salir de la función
        self.indent_level -= 1



    # Enter a parse tree produced by lenguajeInfantilParser#callfuncion.
    def enterCallfuncion(self, ctx:lenguajeInfantilParser.CallfuncionContext):
        pass

    def exitCallfuncion(self, ctx: lenguajeInfantilParser.CallfuncionContext):
        nombre_funcion = ctx.ID().getText()
        
        # Extraer los argumentos
        argumentos = []
        if ctx.argumentos():
            # Recorre cada valor en argumentos y realiza las transformaciones necesarias
            for arg in ctx.argumentos().valor():
                arg_text = arg.getText()
                if arg_text.lower() == "verdadero":
                    argumentos.append("True")
                elif arg_text.lower() == "falso":
                    argumentos.append("False")
                else:
                    argumentos.append(arg_text)

        # Generar la llamada a la función con la indentación
        argumentos_str = ", ".join(argumentos)
        self.codePy += f"{self.addIndentation()}{nombre_funcion}({argumentos_str})\n"

    # Enter a parse tree produced by lenguajeInfantilParser#parametros.
    def enterParametros(self, ctx:lenguajeInfantilParser.ParametrosContext):
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#parametros.
    def exitParametros(self, ctx:lenguajeInfantilParser.ParametrosContext):
        pass

     # Enter a parse tree produced by lenguajeInfantilParser#expresion.
    def enterExpresion(self, ctx:lenguajeInfantilParser.ExpresionContext):
        self.current_expression = ""
        pass


    # Exit a parse tree produced by lenguajeInfantilParser#expresion.
    def exitExpresion(self, ctx: lenguajeInfantilParser.ExpresionContext):
        # Obtén los valores y el operador
        left = ctx.valor(0).getText()  # Primer valor (lado izquierdo)
        operator = ctx.getChild(1).getText()  # Operador entre los valores
        right = ctx.valor(1).getText()  # Segundo valor (lado derecho)

        # Mapea los operadores personalizados a Python
        op_map = {
            "mayorque": ">",
            "menorque": "<",
            "mayorigualque": ">=",
            "menorigualque": "<=",
            "igual": "==",
            "diferente": "!="
        }

        # Convierte el operador y guarda la expresión resultante
        python_operator = op_map.get(operator, operator)
        self.current_expression = f"{left} {python_operator} {right}"


    # Enter a parse tree produced by lenguajeInfantilParser#lista.
    def enterLista(self, ctx:lenguajeInfantilParser.ListaContext):
        pass

    # Exit a parse tree produced by lenguajeInfantilParser#lista.
    def exitLista(self, ctx:lenguajeInfantilParser.ListaContext):
        pass