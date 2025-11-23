import sys
from antlr4 import *
from src.generated.MiniLangLexer import MiniLangLexer
from src.generated.MiniLangParser import MiniLangParser
from src.visitor import MiniLangVisitorImpl
from src.semantic import check_semantics, print_symtab
from src.interp import exec_program
from src.codegen import codegen_python
from src.pretty import print_ast_ascii
from src.error_listener import MiniLangErrorListener

def main():
    # --- MUDANÇA AQUI: Rigor na CLI ---
    # Se não tiver argumentos suficientes, avisa e sai.
    if len(sys.argv) < 2:
        print("❌ Erro: Nenhum arquivo de entrada fornecido.")
        print("Uso correto: python -m src.main <caminho_do_arquivo.min>")
        return # Sai do programa
    
    filename = sys.argv[1]
    # ----------------------------------

    print(f"Compilando arquivo: {filename}...")
    
    try:
        with open(filename, 'r') as f:
            input_stream = InputStream(f.read())
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{filename}' não foi encontrado.")
        return

    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)

    # Configuração de Erros Sintáticos
    parser.removeErrorListeners()
    parser.addErrorListener(MiniLangErrorListener())

    try:
        tree = parser.program()
    except SyntaxError as e:
        print(f"\n❌ ERRO DE SINTAXE DETECTADO:\n{e}")
        return 

    visitor = MiniLangVisitorImpl()
    ast = visitor.visit(tree)

    print("\n=== AST ASCII ===")
    print_ast_ascii(ast)

    print("\n=== TABELA DE SÍMBOLOS ===")
    try:
        symtab = check_semantics(ast)
        print_symtab(symtab)
    except Exception as e:
        print(f"\n❌ ERRO SEMÂNTICO: {e}")
        return

    print("\n=== EXECUÇÃO (INTÉRPRETE) ===")
    try:
        exec_program(ast, trace=False)
    except Exception as e:
        print(f"\n❌ ERRO RUNTIME: {e}")
        return

    print("\n=== PYTHON GERADO ===")
    print(codegen_python(ast))

if __name__ == '__main__':
    main()
