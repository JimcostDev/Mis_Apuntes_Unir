import ply.lex as lex

# Diccionario de palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
}

# Lista de tokens: se incluyen los tokens simples y se agregan las palabras reservadas
tokens = (
    'ID',      # Identificador
    'NUMBER',  # Números enteros
    'PLUS',    # +
    'MINUS',   # -
    'TIMES',   # *
    'DIVIDE',  # /
    'LPAREN',  # (
    'RPAREN',  # )
    'EQUALS',  # =
) + tuple(reserved.values())

# Expresiones regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALS  = r'='

# Token para identificadores (ID)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Verificar si el identificador es una palabra reservada
    t.type = reserved.get(t.value, 'ID')
    return t

# Token para números (NUMBER)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convertir el valor a entero
    return t

# Caracteres a ignorar (espacios y tabulaciones)
t_ignore = ' \t'

# Función para manejo de errores léxicos
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para probar el analizador con una cadena dada
def prueba_lexer(data):
    lexer.input(data)
    print("Entrada:", data)
    print("Tokens:")
    for tok in lexer:
        print(tok)
    print("\n" + "-" * 40 + "\n")

# Función para probar varios ejemplos
def test_examples():
    ejemplos = [
        "if x = 10 + 20",
        "while contador = 0",
        "suma = a + b - c * d / e",
        "error@123",             
        "if else while",         
        "identificador123 = 45",
        " ( x + y ) * z "        
    ]
    
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"Ejemplo {i}:")
        prueba_lexer(ejemplo)

if __name__ == "__main__":
    # LexToken(TIPO, 'valor', línea, posición)
    test_examples()
    
