# =============================================================================
# SOFTWARE FJ - SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Grupo: PROGRAMACIÓN 213023_8
# FASE 4: COMPONENTE PRÁCTICO
# Integrantes: Jamer David Rebolledo Quiroz - Jaime Andrés Castilo
# =============================================================================

import logging
from cliente import Cliente
from servicios import SalaReunion, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ReservaInvalidaError, ValidacionDatosError

# Configuración del sistema de Logging
# Este bloque inicializa el archivo 'gestion_reservas.log' donde se registrarán
# todos los eventos importantes y errores, permitiendo que la aplicación 
# sea auditable y robusta.
logging.basicConfig(
    filename='gestion_reservas.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def ejecutar_simulaciones():
    """
    Función principal que ejecuta al menos 10 operaciones simuladas.
    Incluye casos de éxito y de error para demostrar la estabilidad
    del sistema ante situaciones adversas [2, 6].
    """
    
    # Listas internas para gestionar la información sin bases de datos
    lista_clientes = []
    lista_servicios = []
    lista_reservas = []

    print("--- INICIANDO SIMULACIÓN SISTEMA SOFTWARE FJ ---")
    logging.info("Inicio de la simulación del sistema.")

    # ---------------------------------------------------------
    # OPERACIÓN 1: Registro exitoso de un cliente
    # ---------------------------------------------------------
    try:
        # Se intenta crear un cliente con datos válidos
        cliente1 = Cliente(id_cliente="C001", nombre="Ana García", email="ana@mail.com")
        lista_clientes.append(cliente1)
        print("Op 1: Cliente registrado con éxito.")
        logging.info(f"Cliente registrado: {cliente1.get_nombre()}")
    except Exception as e:
        logging.error(f"Error inesperado en Op 1: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 2: Intento de registro con datos inválidos (Fallo)
    # ---------------------------------------------------------
    try:
        # Esto disparará una excepción personalizada de validación
        cliente_error = Cliente(id_cliente="", nombre="Error", email="email-invalido")
    except ValidacionDatosError as e:
        print(f"Op 2: Error controlado - {e}")
        logging.warning(f"Intento de registro inválido: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 3: Creación de servicio de Sala (Éxito)
    # ---------------------------------------------------------
    try:
        sala1 = SalaReunion(id_servicio="S01", capacidad=15, tipo="VIP")
        lista_servicios.append(sala1)
        print("Op 3: Servicio de Sala creado.")
    except Exception as e:
        logging.error(f"Error en Op 3: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 4: Creación de servicio de Alquiler (Éxito)
    # ---------------------------------------------------------
    try:
        equipo1 = AlquilerEquipo(id_servicio="E01", nombre_equipo="Laptop Pro")
        lista_servicios.append(equipo1)
        print("Op 4: Servicio de Equipo creado.")
    except Exception as e:
        logging.error(f"Error en Op 4: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 5: Creación de servicio de Asesoría (Éxito)
    # ---------------------------------------------------------
    try:
        asesoria1 = AsesoriaEspecializada(id_servicio="A01", consultor="Ing. Pérez")
        lista_servicios.append(asesoria1)
        print("Op 5: Servicio de Asesoría creado.")
    except Exception as e:
        logging.error(f"Error en Op 5: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 6: Reserva exitosa (Uso de polimorfismo)
    # ---------------------------------------------------------
    try:
        # La clase Reserva integra cliente, servicio y duración [8]
        reserva1 = Reserva(cliente1, sala1, horas=3)
        reserva1.procesar_confirmacion() # Implementa lógica de confirmación
        lista_reservas.append(reserva1)
        print("Op 6: Reserva 1 confirmada con éxito.")
    except ReservaInvalidaError as e:
        logging.error(f"Fallo en Op 6: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 7: Cálculo de costo con sobrecarga (Multipledispatch)
    # ---------------------------------------------------------
    try:
        # Se calcula el costo base del servicio usando el primer método
        costo_base = sala1.calcular_costo(3) 
        print(f"Op 7: Costo base calculado: ${costo_base}")
    except Exception as e:
        logging.error(f"Error en sobrecarga Op 7: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 8: Cálculo de costo con impuesto (Sobrecarga 2)
    # ---------------------------------------------------------
    try:
        # Uso de multipledispatch para variante con impuesto [1]
        costo_total = sala1.calcular_costo(3, 0.19)
        print(f"Op 8: Costo con IVA (19%) calculado: ${costo_total}")
    except Exception as e:
        logging.error(f"Error en sobrecarga Op 8: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 9: Intento de reserva con duración inválida (Fallo)
    # ---------------------------------------------------------
    try:
        # Se intenta reservar con 0 horas, lo que debería estar prohibido
        reserva_fallida = Reserva(cliente1, equipo1, horas=0)
    except ReservaInvalidaError as e:
        print(f"Op 9: Error controlado - {e}")
        logging.warning(f"Intento de reserva inválida: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 10: Intento de acceso a servicio no existente (Fallo)
    # ---------------------------------------------------------
    try:
        # Simulación de un error de parámetros faltantes o tipo incorrecto
        if not lista_servicios[9]: # Esto causará un IndexError
             pass
    except IndexError as e:
        # Se usa encadenamiento de excepciones si fuera necesario [7]
        print(f"Op 10: Error de sistema manejado - {e}")
        logging.error(f"Intento de acceso fuera de rango: {e}")
    finally:
        # Bloque que siempre se ejecuta para cerrar procesos [7, 10]
        print("--- SIMULACIÓN FINALIZADA ---")
        logging.info("Simulación terminada.")

if __name__ == "__main__":
    # El uso de try/except/else/finally garantiza que la app no se detenga [10]
    try:
        ejecutar_simulaciones()
    except Exception as global_e:
        # Última red de seguridad para errores no capturados
        print(f"Error crítico en el sistema: {global_e}")
        logging.critical(f"ERROR CRÍTICO: {global_e}")