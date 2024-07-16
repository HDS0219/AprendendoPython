# Definindo o nome do arquivo a ser manipulado
nome = "teste.txt"

# Abrindo o arquivo no modo de escrita ('w') que cria o arquivo se não existir
# O caminho do arquivo é concatenado com o nome do arquivo definido
# Adicionar pasta raíz de onde ficara o arquivo.
f = open("" + nome, "w")

# Modos de abertura de arquivos:
# 'r' - read: abre o arquivo para leitura
# 'a' - append: abre o arquivo para anexar dados ao final
# 'w' - write: abre o arquivo para escrita (cria se não existir, sobrescreve se existir)
# 'x' - create: cria um novo arquivo e retorna um erro se o arquivo já existir
# 't' - text: abre o arquivo no modo texto (padrão)
# 'b' - binary: abre o arquivo no modo binário

# Solicitando ao usuário que digite um texto
txt = input("Digite um texto:")

# Escrevendo o texto digitado no arquivo seguido de uma nova linha
f.write(txt + "\n")

# Tentando ler o arquivo, mas está no modo de escrita, o que causará um erro
# Remover ou corrigir esta linha
# f.read()

# Fechando o arquivo após a escrita para liberar os recursos
f.close()
