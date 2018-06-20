import math
import numpy
import matplotlib.pylab as plt

numpy.set_printoptions(floatmode='fixed', precision=4, suppress=True)

def run(X, Y):
    N = len(Y)

    # Z possui os valores obtidos com o somatório
    # [ [real, imaginario], [real, imaginario], ... ]
    Z = numpy.empty(shape=[N, 2])

    # mag é o array com os módulos
    mag = numpy.empty(N)

    # angle é o array com os angulos
    angle = numpy.empty(N)

    for k in range(0, N):
        for n in range(0, N):
            b = 2*math.pi*k*n / N
            Z[k][0] += Y[n]*math.cos(-b)
            Z[k][1] += Y[n]*math.sin(-b)

        mag[k] = math.sqrt(math.pow(Z[k][0], 2) + math.pow(Z[k][1], 2))

    # plotar espectro de linhas com mag no eixo Y
    plt.stem(X, mag)
    plt.title('Espectro de Linhas')
    plt.ylabel('Magnitude')

    print(Z)
    print(mag)
    print(angle)

    plt.show()
