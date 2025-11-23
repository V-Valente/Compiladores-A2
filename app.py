import streamlit as st
import sys
import os
from io import StringIO
from antlr4 import *
from src.generated.MiniLangLexer import MiniLangLexer
from src.generated.MiniLangParser import MiniLangParser
from src.visitor import MiniLangVisitorImpl
from src.semantic import check_semantics, print_symtab
from src.interp import exec_program
from src.codegen import codegen_python
from src.error_listener import MiniLangErrorListener
from src.pretty import print_ast_ascii

# --- Configuração da Página ---
st.set_page_config(page_title="MiniLang Compiler", page_icon="🚀", layout="wide")

st.title("🚀 Compilador MiniLang (ANTLR4)")
st.markdown("Escreva seu código abaixo e clique em **Compilar**.")

# --- Área de Texto (Editor) ---
default_code = """{
    int max = 10;
    int n1 = 0; int n2 = 1; int next; int count = 0;
    while (count < max) {
        next = n1 + n2;
        print(next);
        n1 = n2; n2 = next;
        count = count + 1;
    }
}"""

code = st.text_area("Código Fonte (.min)", value=default_code, height=200)

# --- Botão de Ação ---
if st.button("⚙️ Compilar e Executar"):
    st.divider()
    
    # Captura de stdout (para pegar os prints do interpretador)
    old_stdout = sys.stdout
    redirected_output = StringIO()
    sys.stdout = redirected_output

    try:
        # 1. Setup do ANTLR
        input_stream = InputStream(code)
        lexer = MiniLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiniLangParser(stream)
        
        parser.removeErrorListeners()
        parser.addErrorListener(MiniLangErrorListener())

        # 2. Parse
        try:
            tree = parser.program()
            st.success("✅ Análise Sintática: Sucesso!")
        except SyntaxError as e:
            st.error(f"❌ {e}")
            st.stop()

        # 3. Visitor (AST)
        visitor = MiniLangVisitorImpl()
        ast = visitor.visit(tree)

        # Mostra a AST em uma aba expansível
        with st.expander("🌳 Ver Árvore Sintática (AST)"):
            # Captura o print da árvore
            temp_out = StringIO()
            sys.stdout = temp_out
            print_ast_ascii(ast)
            st.code(temp_out.getvalue())
            sys.stdout = redirected_output # restaura para o buffer principal

        # 4. Semântica
        try:
            symtab = check_semantics(ast)
            st.info("✅ Análise Semântica: OK")
            
            # Mostra Tabela de Símbolos
            with st.expander("📋 Ver Tabela de Símbolos"):
                # Formata a tabela para exibição visual
                data = []
                for s in symtab:
                    data.append({
                        "Escopo": s['scope_depth'],
                        "Nome": s['name'],
                        "Tipo": s['type'],
                        "Const": "Sim" if s['const'] else "Não"
                    })
                st.table(data)

        except Exception as e:
            st.error(f"❌ Erro Semântico: {e}")
            st.stop()

        # 5. Execução e Codegen
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("▶️ Saída do Intérprete")
            # Limpa o buffer para capturar apenas a execução
            redirected_output.truncate(0)
            redirected_output.seek(0)
            
            try:
                exec_program(ast, trace=False)
                resultado = redirected_output.getvalue()
                if resultado:
                    st.code(resultado, language="text")
                else:
                    st.warning("O programa rodou mas não imprimiu nada.")
            except Exception as e:
                st.error(f"Erro de Runtime: {e}")

        with col2:
            st.subheader("🐍 Código Python Gerado")
            py_code = codegen_python(ast)
            st.code(py_code, language="python")

    except Exception as e:
        st.error(f"Erro Inesperado: {e}")
    
    finally:
        # Restaura o stdout original para não quebrar o terminal
        sys.stdout = old_stdout