from antlr4 import *;
from lenguajeInfantilLexer import lenguajeInfantilLexer;
from lenguajeInfantilParser import lenguajeInfantilParser;
from lenguajeInfantilListener import lenguajeInfantilListener;
from inlenIngtoPy import inlenIngtoPy
import os

def main():
    # in_morse_line = input ('File name>')
    # Leer archivo de entrada
    file = open (os.path.abspath('pruebaLen.txt'))
    lexer = lenguajeInfantilLexer(InputStream(file.read()))
    t_stream = CommonTokenStream(lexer)

    parser = lenguajeInfantilParser(t_stream)

    tree = parser.programa()

    # print(tree.toStringTree(recog=parser))
    walker = ParseTreeWalker()
    walker.walk(inlenIngtoPy(), tree)

# .... . .-. --- -----
if __name__== '__main__':
    main()