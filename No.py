class No:
  def __init__(self, estado):
    # print(estado.variaveis())
    self.estado = estado
    self.proximos = []

    self.construir_arvore()
  
  def variaveis(self):
    return self.estado.variaveis
  
  def terminal(self):
    return len(self.proximos) == 0
  
  def construir_arvore(self):
    visinhos = self.estado.proximos_estados()
    for estado in visinhos:
      self.proximos.append(No(estado))