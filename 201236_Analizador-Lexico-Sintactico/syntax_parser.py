import ply.yacc as yacc
import lexer

tokens = lexer.tokens

def p_program(p):
    'program : statement'
    p[0] = p[1]

def p_statement(p):
    '''statement : for_loop
                 | print_statement'''
    p[0] = p[1]

def p_for_loop(p):
    'for_loop : FOR LPAREN assignment SEMI condition SEMI increment RPAREN LBRACE print_statement RBRACE'
    p[0] = 'Estructura FOR correcta'

def p_assignment(p):
    'assignment : INT ID EQUALS NUMBER'
    p[0] = ('assignment', p[2], p[4])

def p_condition(p):
    'condition : ID LE NUMBER'
    p[0] = ('condition', p[1], p[3])

def p_increment(p):
    'increment : ID PLUS'
    p[0] = ('increment', p[1])

def p_print_statement(p):
    'print_statement : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS NUMBER RPAREN SEMI'
    p[0] = ('print_statement', p[7], p[9])

# Manejo de errores
def p_error(p):
    if p:
        error_message = f"Error de sintaxis en '{p.value}' en la línea {p.lineno}"
    else:
        error_message = "Error de sintaxis en EOF"
    p.parser.error = error_message

# Construir el analizador sintáctico
parser = yacc.yacc()
parser.error = None  # Inicializar el atributo de error
