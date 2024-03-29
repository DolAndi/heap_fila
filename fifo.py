
class Fifo:    
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item): 
        self._vet.append(item)
    
    def dequeue(self): 
        if len(self._vet) > 0:
            return self._vet.pop(0)
        else:
            raise Exception("Fila Vazia")

    def front(self): 
        return self._vet[0]
                
    def is_empty(self):
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): 
        return str(self._vet)