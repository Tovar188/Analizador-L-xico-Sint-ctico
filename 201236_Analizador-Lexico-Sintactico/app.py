from flask import Flask, request, render_template
import lexer
import syntax_parser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    codigo = request.form['codigo']
    lexer.lexer.input(codigo)

    tokens = []
    while True:
        tok = lexer.lexer.token()
        if not tok:
            break
        tokens.append(tok)

    resultado_sintactico = syntax_parser.parser.parse(codigo)
    if syntax_parser.parser.error:
        resultado_sintactico = syntax_parser.parser.error
    
    return render_template('index.html', tokens=tokens, resultado_sintactico=resultado_sintactico)

if __name__ == '__main__':
    app.run(debug=True)
