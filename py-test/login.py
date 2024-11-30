def logar(usuario, senha):
    # Vamos considerar um banco de dados fictício para a autenticação
    usuarios = {"admin": "1234", "usuario": "senha123"}
    return usuarios.get(usuario) == senha
