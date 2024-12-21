grammar lenguajeInfantil;

// Lexer rules
TIPO_ENTERO: 'NumeroEntero';
TIPO_DECIMAL: 'NumeroDecimal';
TIPO_TEXTO: 'Texto';
TIPO_BOOLEANO: 'VerdaderoFalso';
DECLARAR: 'declarar';
DECLARAR_CONSTANTE: 'declararConstante';
COMO: 'como';
IGUAL: '=';
SUMA: '+';
RESTA: '-';
MULT: '*';
DIV: '/';
POTENCIA: '^';
MAYORQUE: 'mayorque';
MENORQUE: 'menorque';
MAYORIGUALQUE: 'mayorigualque';
MENORIGUALQUE: 'menorigualque';
IGUALDAD: 'igual';
DIFERENTE: 'diferente';
SI: 'si';
SINO: 'sino';
REPITE: 'repetir';
VECES: 'veces';
MIENTRAS: 'mientras';
FUNCION: 'funcion';
MOSTRAR: 'mostrar';
ESPERAR: 'esperar';
INTENTAR: 'intentar';
CAPTURAR: 'capturar';
ERROR: 'error';
LISTA: 'lista';
AGREGAR: 'agregar';
OBTENER: 'obtener';
LLAVE_IZQ: '{';
LLAVE_DER: '}';
PAREN_IZQ: '(';
PAREN_DER: ')';
NUMERO: [0-9]+ ('.' [0-9]+)?;
TEXTO: '"' .*? '"';
VERDADERO: 'verdadero';
FALSO: 'falso';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;

// Parser rules
programa: (declaracion | funcion | sentencia | lista | manejo_errores | callfuncion | NEWLINE)*;

declaracion: DECLARAR ID COMO tipo_dato NEWLINE
           | DECLARAR_CONSTANTE ID COMO tipo_dato IGUAL valor NEWLINE;

tipo_dato: TIPO_ENTERO | TIPO_DECIMAL | TIPO_TEXTO | TIPO_BOOLEANO | LISTA;

valor: NUMERO | TEXTO | VERDADERO | FALSO | ID;

sentencia: asignacion | operacion | condicional | ciclo | mostrar | esperar;

asignacion: ID IGUAL (operacion | valor) (NEWLINE | EOF);

operacion: valor (SUMA | RESTA | MULT | DIV | POTENCIA) valor;

condicional: SI expresion LLAVE_IZQ programa LLAVE_DER 
             (SINO LLAVE_IZQ programa LLAVE_DER)?;

ciclo: REPITE NUMERO VECES LLAVE_IZQ programa LLAVE_DER
     | MIENTRAS expresion LLAVE_IZQ programa LLAVE_DER;

mostrar: MOSTRAR (TEXTO | ID | valor | operacion) (NEWLINE | EOF);

esperar: ESPERAR NUMERO (NEWLINE | EOF);

manejo_errores: INTENTAR LLAVE_IZQ programa LLAVE_DER CAPTURAR ERROR LLAVE_IZQ programa LLAVE_DER;

funcion: FUNCION ID PAREN_IZQ parametros? PAREN_DER LLAVE_IZQ programa LLAVE_DER;

parametros: ID COMO tipo_dato (',' ID COMO tipo_dato)*;

expresion: valor (MAYORQUE | MENORQUE | MAYORIGUALQUE | MENORIGUALQUE | IGUALDAD | DIFERENTE) valor;

lista: DECLARAR ID COMO LISTA (NEWLINE | EOF)                    
     | ID AGREGAR PAREN_IZQ valor PAREN_DER (NEWLINE | EOF)       
     | MOSTRAR ID OBTENER PAREN_IZQ NUMERO PAREN_DER (NEWLINE | EOF)
     | ID OBTENER PAREN_IZQ NUMERO PAREN_DER (NEWLINE | EOF);

callfuncion: ID PAREN_IZQ argumentos? PAREN_DER (NEWLINE | EOF);

argumentos: valor (',' valor)*;
