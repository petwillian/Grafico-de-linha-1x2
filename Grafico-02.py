
# passo 1 - importa a biblioteca
import matplotlib.pyplot as plt

#passo 2 - intanciar o objeto figura
fig, ax = plt.subplots(1, 2) # 1x2

#passo 3 - Definir os dados
indices = [1,2,3,4]
amostra_a = [1,4,2,3]
amostra_b = [2,8,4,6]

#passo 4 - plotar os dados no axe/eixo(grafico)
ax[0].plot(indices, amostra_a, label="Amostra A", color = 'blue', marker = 'o')
ax[1].plot(indices, amostra_b, label="Amostra B", color = 'green', marker = 'o')

# titulo do grafico
ax[0].set_title("Titúlo do Gráfico 0")
ax[1].set_title("Titúlo do Gráfico 1")

# titulo do x
ax[0].set_xlabel("Label X 0")
ax[1].set_xlabel("Label X 1")

# titulo y
ax[0].set_ylabel("Label y 0")
ax[1].set_ylabel("Label y 1")

# a legenda
ax[0].legend()
ax[1].legend()

# Salvando o gráfico como uma imagem PNG
plt.savefig('Gráfico-02.png')

#passo 5 - apresentar o grafico
plt.show()
