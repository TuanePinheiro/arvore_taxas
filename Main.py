from Estado import Estado
from No import No
from metodos import probabilidade_estado, esperanca_tempo, transformada_laplace



def main():

  estado_inicial = Estado(
    saque = 2,
    deposito = 1,
    fila = 1,
    alpha = 1,
    betha = 1,
  )

  raiz = No(estado_inicial)

  print("probabilidade:", probabilidade_estado(raiz, Estado(0,1,1), 1.0))
  print("probabilidade:", probabilidade_estado(raiz, Estado(0,0,0), 1.0))
  
  print("esperanca total:", esperanca_tempo(raiz))
  
  acumulador = []
  transformada_laplace(raiz, Estado(0,0,0), '', acumulador)

  laplace_texto = ' +\n'.join([' * '.join(caminho) for caminho in acumulador])
  print("Transformada Laplace:")
  print(laplace_texto)

  
if __name__ == "__main__":
  main()