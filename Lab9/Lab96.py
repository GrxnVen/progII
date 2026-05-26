#Parte C: Clases y Métodos finales
#Clases Finales: no se pueden heredar
from typing import final

@final
class Base:
    pass

#Un linter (como mypy) marcará error si intentamos heredar de Base
class Derivada(Base): #ERROR: no se puede heredar de una clase final
    pass
