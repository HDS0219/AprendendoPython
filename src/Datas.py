import datetime #Importando a biblioteca de data

data = datetime.datetime.now() #ver a hora exata do computador
nasc = datetime.datetime(1978,3,7) #criação de data especifica

print(f"{data.day}/{data.month}/{data.year}")
print(nasc.strftime("%A")) #aplicando formatação no date

''' %A = dia da semana completo(Monday)
    %a = dia da semana abreviado(Mon)
    %w = número do dia da semana(Monday = 1)
    %W = Número da semana do ano
    %d = dia do mês abreviado
    %D = dia do mês completo
    %b = mês abreviado
    %B = mês completo
    %m = número do mês
    %y = ano com 2 digitos
    %Y = ano com quatro digitos
    %H = hora com formatação 24 horas
    %I = hora com formatação 12 horas
    %p = AM / PM
    %M = minutos
    %S = segundos
    %f = microssegundos
    %j = dia do ano 001 ate 365
'''