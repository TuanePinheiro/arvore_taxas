def probabilidade_estado(no, estado_alvo, prob):
  # print(no.estado.variaveis())
  if (no.estado == estado_alvo):
    return prob
  
  prob_total = 0.0

  for proximo_no in no.proximos:
    nova_prob = prob  * proximo_no.estado.peso / no.estado.peso_total
    prob_total += probabilidade_estado(proximo_no, estado_alvo, nova_prob)
  
  return prob_total


def esperanca_tempo(no):
  if (no.terminal()):
    return 0.0
  
  total = 1.0 / (no.estado.peso_total)

  for proximo_no in no.proximos:
    prob = proximo_no.estado.peso / no.estado.peso_total
    total += prob * esperanca_tempo(proximo_no)
  
  return total

def transformada_laplace(no, alvo, caminho, acumulador):
  if (no.estado == alvo):
    acumulador.append(caminho)
    pass
  
  for proximo_no in no.proximos:
    peso = proximo_no.estado.peso
    peso_total = no.estado.peso_total
    proximo = f"{peso}/({peso} + s) * {peso}/{peso_total}"
    transformada_laplace(proximo_no, alvo, [*caminho, proximo], acumulador)

  pass