import re

# Definindo o nome do arquivo a ser manipulado
nome = "teste.txt"
# Abrindo o arquivo no modo de leitura de texto ('rt')
# Coloque sua raíz
caminho = "" + nome
f = open(caminho, "rt")

# Leitura da primeira linha do arquivo
linha = f.readline()

# Substituindo todos os espaços em branco na linha lida por hifens
res = re.sub("\s", "-", linha)

# Fechando o arquivo de leitura
f.close()

# Abrindo o arquivo no modo de escrita de texto ('wt') para sobrescrever o conteúdo
f = open(caminho, "wt")
# Escrevendo a linha modificada no arquivo
f.write(res)
# Fechando o arquivo após a escrita
f.close()

# Imprimindo a linha modificada
print(res)
