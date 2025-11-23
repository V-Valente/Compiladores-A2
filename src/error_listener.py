from antlr4.error.ErrorListener import ErrorListener

class MiniLangErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Esse metodo irá parar a compilação ao achar um erro, e depois apontar onde o erro se econtra
        """
        # Mensagem amigável (Bônus do trabalho)
        error_message = f"Linha {line}:{column} -> {msg}"
        
        # Trava o programa aqui mesmo
        raise SyntaxError(error_message)
