import tkinter as tk

# Funções

## Função da Pegada de carbono do Veiculo

def pgcveiculo ():
    km = int(quilometros.get())
    ltr = int(litros.get())
    caculo_veiculo = (km * (2.3/1 * km/ltr))
    pgcresultcar.insert(0, int(caculo_veiculo))

## Função da Pegada de Carbono de Eletricidade

def pgceletricidade ():
    cnmeletrico = int(eletricidade.get())
    calculo_eletricidade = (cnmeletrico * 0.07)
    pgcresultenel.insert(0, float(calculo_eletricidade))

## Função da Pegada Total

def pgctotalizado ():
    resultcar = int(pgcresultcar.get())
    resultenel = float(pgcresultenel.get())
    total = (resultcar + resultenel)
    pgcresulttotal.insert(0, float(total))

## Função dos Créditos de Carbono

def credcarbo ():
    pgctotal = float(pgcresulttotal.get())
    calculo_creditos_carbono = (pgctotal / 1)
    cdcarbonoresult.insert(0, float(calculo_creditos_carbono))

## Função para Limpar

def excluir ():
    quilometros.delete(0, tk.END)
    litros.delete(0, tk.END)
    eletricidade.delete(0, tk.END)
    pgcresultcar.delete(0, tk.END)
    pgcresultenel.delete(0, tk.END)
    pgcresulttotal.delete(0, tk.END)
    cdcarbonoresult.delete(0, tk.END)

# Interface da 1 Janela

janela =tk.Tk()
janela.title('Calculadora De Créditos de Carbono')
janela.configure(background = "gray")
titulo = tk.Label(janela, text = 'Caculadora de Créditos de Carbono', bg = 'gray', fg = 'black', font = '20')
titulo.pack(pady = 10)

# Interface das informações que o usario irá colocar

pergunta_km = tk.Label(janela, text = 'Quilometros percorridos de carro:', bg = 'gray', fg = 'black', font = '20')
pergunta_km.place(x = 330, y = 70)
quilometros = tk.Entry(janela, font = '5', fg = 'black')
quilometros.pack(pady = 20)

pergunta_lt = tk.Label(janela, text = 'Litros Usados:', bg = 'gray', fg= 'black', font = '20')
pergunta_lt.place(x = 500, y = 140)
litros = tk.Entry(janela, font = '5', fg = 'black')
litros.pack(pady = 25)

pergunta_enel = tk.Label(janela, text = 'Consumo eletrico hoje:', bg = 'gray', fg = 'black', font = '20')
pergunta_enel.place(x = 430, y = 220)
eletricidade = tk.Entry(janela, font = '5', fg = 'black')
eletricidade.pack(pady = 30)

# Interface dos Resultados

pgccar = tk.Label(janela, text = 'Pegada de Carbono do Veiculo - Formula: km * (2.3 / 1 * litros / km)', bg = 'gray', fg = 'black', font = '20')
pgccar.place(x = 450, y = 270)
pgcresultcar = tk.Entry(janela, font = '5', fg = 'black')
pgcresultcar.pack(pady = 35)

pgcenel = tk.Label(janela, text = 'Pegada de Carbono da eletricidade - Formula: eletricidade * 0.07', bg = 'gray', fg = 'black', font = '20')
pgcenel.place(x = 450, y = 360)
pgcresultenel = tk.Entry(janela, font = '5', fg = 'black')
pgcresultenel.pack(pady = 40)

pgctot = tk.Label(janela, text = 'Pegada de Carbono Total', bg = 'gray', fg = 'black', font = '20')
pgctot.place(x = 650, y = 470)
pgcresulttotal = tk.Entry(janela, font = '5', fg = 'black')
pgcresulttotal.pack(pady = 45)

cdcarbono = tk.Label(janela, text = 'Ceditos de Carbonos', bg = 'gray', fg = 'black', font = '20')
cdcarbono.place(x = 670, y = 580)
cdcarbonoresult= tk.Entry(janela, font = '5', fg = 'black')
cdcarbonoresult.pack(pady = 45)

#Inteface dos Botões

## Botão Pegada de Carbono do Carro

carro = tk.Button(janela, text = 'PGC Carro', font = '5', command = pgcveiculo)
carro.place(x = 420, y = 750)

## Botão Pegada de Carbono da Eletricidade

enel = tk.Button(janela, text = 'PGC Eletricidade', font = '5', command = pgceletricidade)
enel.place(x = 550, y = 750)

## Botão Pegada de Carbono Total

soma = tk.Button(janela, text = 'PGC Total', font = '5', command = pgctotalizado)
soma.place(x = 730, y = 750)

## Botão Creditos de Carbonos

creditoscarbonos = tk.Button(janela, text = 'CDC Possuido', font = '5', command = credcarbo)
creditoscarbonos.place(x = 850, y = 750)

## Botão para limpar tudo 

limpar = tk.Button(janela, text = 'Limpar', font = '5', command = excluir)
limpar.place(x = 1010, y = 750)

janela.mainloop()