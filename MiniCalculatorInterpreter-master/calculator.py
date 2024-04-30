import math
import ply.lex as lex
import ply.yacc as yacc

# Définition des tokens (si nécessaire)
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

# Définition des règles de correspondance pour les tokens (si nécessaire)
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Ignorer les espaces et les tabulations
t_ignore = ' \t'

# Fonction de correspondance pour les nombres
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Fonction de gestion des erreurs de token
def t_error(t):
    print("Caractère illégal : '%s'" % t.value[0])
    t.lexer.skip(1)

# Création de l'analyseur lexical
lexer = lex.lex()

# Définition des opérations mathématiques
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Division par zéro impossible.")
        return None
