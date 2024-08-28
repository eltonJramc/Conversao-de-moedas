import matplotlib.pyplot as plt

def grafico_barras(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores)
    plt.title('Conversões para Real (R$)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

def grafico_pizza(l_moedas, l_valores):
    plt.pie(l_valores, labels=l_moedas)
    plt.title('Proporção em relação ao BRL - Real Brasileiro')
    plt.show()

def grafico_dispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Conversões para Real (R$)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

