#tratamento de erros
try:
    print(x)
except NameError: #erro especificado
    print("X não definido")
except: #except para erros desconhecidos
    print("Erro desconhecido")

#try com ELSE
x = 10
try:
    print(x)
except:
    print("Erro no programa")
else: #uso do else com except. caso não haja exceção, vai ter else
    print("tudo certo")

    # finally é a execução final. independente se ocorreu ou não o erro, ele executa
    x = 10
    try:
        print(x)
    except:
        print("Erro no programa")
    else:
        print("tudo certo")
    finally:
        print("Fim do tratamento")

#exemplo usando if com exceção
num = -10

if num < 1:
    raise Exception("Valor não permitido") #criando exceção sem TRY

#outro exemplo
num = "Bruno"

if not type(num) is int: #dar erro caso o tipo de num não seja numerico. ps:não utilizar "not" o programa vai dar verdadeiro e o erro não vai existir
    raise Exception("Valor não permitido")
num = "Bruno"

if not type(num) is int:
    raise Exception("somente numeros permitidos") #vai dar erro pois o num está mostrando String
else: #exemplo usando else
    print(num) #vai mostrar o numero caso seja int