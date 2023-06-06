class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass
PRECIO_TICKET = 70
PRIMARIO = "primario" #-50%
SECUNDARIO = "secundario" #-40%
UNIVERSITARIO = "universitario" #-30%
JUBILADO = "jubilado" #-25%
ACTIVADO = "activado"
DESACTIVADO = "desactivado"

DESCUENTOS={
PRIMARIO : 0.50,
SECUNDARIO : 0.40,
UNIVERSITARIO : 0.30,
JUBILADO: 0.25
}

class Sube():
    def __init__ (self, param_saldo = 0, param_beneficio = None, param_Estado = ACTIVADO):
        self.saldo = param_saldo
        self.grupo_beneficiario = param_beneficio
        self.estado = param_Estado
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == None:
            return PRECIO_TICKET
        if self.grupo_beneficiario == PRIMARIO:
            return PRECIO_TICKET - PRECIO_TICKET * DESCUENTOS[PRIMARIO]
        if self.grupo_beneficiario == SECUNDARIO:
            return PRECIO_TICKET - PRECIO_TICKET * DESCUENTOS[SECUNDARIO]
        if self.grupo_beneficiario == SECUNDARIO:
            return PRECIO_TICKET - PRECIO_TICKET * DESCUENTOS[UNIVERSITARIO]
        if self.grupo_beneficiario == SECUNDARIO:
            return PRECIO_TICKET - PRECIO_TICKET * DESCUENTOS[JUBILADO]

    def pagar_pasaje(self):
        if self.estado == ACTIVADO:
            if self.grupo_beneficiario == None and self.saldo < PRECIO_TICKET:
                raise NoHaySaldoException()
            elif self.grupo_beneficiario == PRIMARIO and self.saldo < PRECIO_TICKET*DESCUENTOS[PRIMARIO]:
                raise NoHaySaldoException()
            elif self.grupo_beneficiario == SECUNDARIO and self.saldo < PRECIO_TICKET*DESCUENTOS[SECUNDARIO]:
                raise NoHaySaldoException()
            elif self.grupo_beneficiario == UNIVERSITARIO and self.saldo < PRECIO_TICKET*DESCUENTOS[UNIVERSITARIO]:
                raise NoHaySaldoException()
            elif self.grupo_beneficiario == JUBILADO and self.saldo < PRECIO_TICKET*DESCUENTOS[JUBILADO]:
                raise NoHaySaldoException()
            if self.saldo >= PRECIO_TICKET and self.grupo_beneficiario==None:
                self.saldo -= PRECIO_TICKET
            elif self.saldo >= PRECIO_TICKET*DESCUENTOS[PRIMARIO] and self.grupo_beneficiario==PRIMARIO:
                self.saldo -= PRECIO_TICKET*DESCUENTOS[PRIMARIO]
            elif self.saldo >= PRECIO_TICKET and self.grupo_beneficiario==SECUNDARIO:
                self.saldo -= PRECIO_TICKET*DESCUENTOS[SECUNDARIO]
            elif self.saldo >= PRECIO_TICKET and self.grupo_beneficiario==JUBILADO:
                self.saldo -= PRECIO_TICKET*DESCUENTOS[JUBILADO]
            
        elif self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        
    def cambiar_estado(self, estado):
        if self.estado == DESACTIVADO:
            self.estado = estado
            if self.estado == DESACTIVADO:
                self.estado = ACTIVADO
        if self.estado == ACTIVADO:
            self.estado = estado
        if self.estado == "pendiente":
            raise EstadoNoExistenteException
        
        
            


 


        
            
    
    

            
                
    