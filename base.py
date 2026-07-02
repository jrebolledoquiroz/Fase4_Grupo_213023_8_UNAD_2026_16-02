# =============================================================================
# SOFTWARE FJ - CLASE ABSTRACTA BASE DE ENTIDADES
# Este archivo define la estructura mínima y obligatoria para cualquier 
# objeto que forme parte del sistema de gestión.
# =============================================================================

from abc import ABC, abstractmethod

class EntidadBase(ABC):
    """
    Clase abstracta que actúa como la base para todas las entidades del sistema.
    Asegura que todos los objetos (Clientes, Servicios, etc.) tengan un 
    identificador único y un comportamiento mínimo estandarizado.
    """

    def __init__(self, id_entidad):
        """
        Constructor de la clase base.
        
        :param id_entidad: Identificador único de la entidad (ej. C001, S01).
        
        Este método implementa el principio de encapsulación al marcar el 
        atributo como protegido mediante el uso del guion bajo (_).
        """
        # Se asigna el ID de forma protegida para evitar modificaciones accidentales
        self._id_entidad = id_entidad

    def get_id(self):
        """
        Método 'getter' para obtener de forma segura el identificador.
        
        :return: El ID de la entidad.
        """
        return self._id_entidad

    @abstractmethod
    def mostrar_detalle(self):
        """
        Método abstracto que obliga a todas las clases derivadas a 
        implementar su propia forma de mostrar su información detallada.
        
        Este es un pilar del polimorfismo: el sistema sabe que toda entidad
        puede mostrar su detalle, pero cada una lo hará a su manera.
        """
        pass

    @abstractmethod
    def validar_identidad(self):
        """
        Método abstracto para la validación de integridad de los datos base.
        Cada clase hija (Cliente o Servicio) definirá sus propias reglas 
        estrictas de validación de parámetros.
        """
        pass