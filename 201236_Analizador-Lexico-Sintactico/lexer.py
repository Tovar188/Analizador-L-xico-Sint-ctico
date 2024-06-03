import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'FOR',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'INT',
    'ID',
    'EQUALS',
    'PLUS',
    'SEMI',
    'LE',
    'NUMBER',
    'DOT',
    'COMMA',
    'SYSTEM',
    'OUT',
    'PRINTLN',
    'STRING',
)

# Expresiones regulares para tokens simples
t_FOR = r'for'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_INT = r'int'
t_EQUALS = r'='
t_PLUS = r'\+'
t_SEMI = r';'
t_LE = r'<='
t_DOT = r'\.'
t_COMMA = r','
t_SYSTEM = r'System'
t_OUT = r'out'
t_PRINTLN = r'println'

# Expresión regular para ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Expresión regular para NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Expresión regular para STRING
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # quitar las comillas
    return t

# Regla de seguimiento de números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres a ignorar
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
