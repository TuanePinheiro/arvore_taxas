class Estado:
  def __init__(self, saque, deposito, fila, alpha=None, betha=None, peso=None):
    self.saque = saque
    self.deposito = deposito
    self.fila = fila

    self.alpha = alpha
    self.betha = betha

    self.peso = peso
    self.peso_total = 0.0
  
  def variaveis(self):
    return (self.saque, self.deposito, self.fila)
  
  def __eq__(self, outro): 
    if not isinstance(outro, Estado):
      return NotImplemented

    return self.variaveis() == outro.variaveis()

  def proximos_estados(self):
    saque = self.saque
    deposito = self.deposito
    fila = self.fila
    alpha = self.alpha
    betha = self.betha

    estados = []

    if (saque > 0):
      peso = alpha * saque
      proximo_estado = Estado(saque-1, deposito, fila, alpha, betha, peso)
      estados.append(proximo_estado)
      self.peso_total += peso

    if (deposito > 0):
      peso = betha * deposito
      
      if fila > 0:
        proximo_estado = Estado(saque, deposito, fila-1, alpha, betha, peso)
      else:
        proximo_estado = Estado(saque, deposito-1, fila, alpha, betha, peso)
      
      estados.append(proximo_estado)
      self.peso_total += peso
    
    return estados