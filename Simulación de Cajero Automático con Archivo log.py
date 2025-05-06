# TalentoTech Orinoquía - Arauca 2025
# Análisis de Datos
# Simulación de Cajero Automático en Python
# Autores:   Leidy Dayana Andrade Garrido     cc 1116780233
#            Angie Gisel Silva Ochoa         cc 1117132586
#            Leonardo Pulido Martínez         cc 79348469
#            José Manuel Bello Romero         cc 17588236

import datetime
import io

# Nombre del archivo para guardar el registro
nombre_archivo_log = "registro_transacciones.txt"
log_encoding = "utf-8"  # Especifica la codificación UTF-8

def escribir_log(mensaje):
    """
    Función para escribir un mensaje con fecha y hora en el archivo de log.

    Parámetros:
    mensaje (str): El mensaje a escribir en el archivo.
    """
    hora_actual = datetime.datetime.now()
    formato_hora = "%Y-%m-%d %H:%M:%S"
    hora_formateada = hora_actual.strftime(formato_hora)
    mensaje_con_hora = f"[{hora_formateada}] {mensaje}\n"
    try:
        # Abre el archivo en modo "append" (añadir al final) y especifica la codificación.
        # El archivo se cierra automáticamente al salir del bloque "with".
        with io.open(nombre_archivo_log, "a", encoding=log_encoding) as archivo_log:
            archivo_log.write(mensaje_con_hora)
        # El archivo se cierra aquí automáticamente, incluso si ocurren errores.
    except Exception as e:
        print(f"Error al escribir en el archivo de log: {e}")
    print(mensaje_con_hora)  # Mostrar también en la consola

def mostrar_menu():
    '''
    Función que muestra el menú principal de opciones para el usuario.
    '''
    mensaje = "\n*** MENÚ DEL CAJERO AUTOMÁTICO ***\n1. Consultar saldo\n2. Retirar dinero\n3. Consignar dinero\n4. Salir"
    escribir_log(mensaje)


def consultar_saldo(saldo):
    '''
    Función que imprime el saldo actual del usuario.

    Parámetros:
    saldo (float): Saldo actual disponible en la cuenta.
    '''
    mensaje = f"\nSu saldo actual es: ${saldo:,.2f}"
    escribir_log(mensaje)


def retirar_dinero(saldo):
    '''
    Permite al usuario retirar dinero de su cuenta, validando que el saldo sea suficiente.

    Parámetros:
    saldo (float): Saldo actual del usuario.

    Retorna:
    float: Nuevo saldo después del retiro (si es válido).
    '''
    try:
        cantidad = float(input('Ingrese la cantidad a retirar: $'))  # Solicita la cantidad a retirar
        escribir_log(f"Retiro solicitado por: ${cantidad:,.2f}")
        if cantidad <= 0:
            mensaje = '⚠️  La cantidad debe ser un número positivo.'
            escribir_log(mensaje)
        elif cantidad > saldo:
            mensaje = '❌  Fondos insuficientes.'  # Validación de fondos
            escribir_log(mensaje)
        else:
            saldo -= cantidad  # Actualización del saldo
            mensaje = f'✅  Retiro exitoso. Nuevo saldo: ${saldo:,.2f}'
            escribir_log(mensaje)
    except ValueError:
        mensaje = '⚠️  Entrada inválida. Ingrese un valor numérico.'  # Validación de errores de entrada
        escribir_log(mensaje)
    return saldo  # Retorna el saldo actualizado


def consignar_dinero(saldo):
    '''
    Permite al usuario consignar dinero en su cuenta.

    Parámetros:
    saldo (float): Saldo actual del usuario.

    Retorna:
    float: Nuevo saldo después de la consignación (si es válida).
    '''
    try:
        cantidad = float(input('Ingrese la cantidad a consignar: $'))  # Solicita la cantidad a consignar
        escribir_log(f"Consignación solicitada por: ${cantidad:,.2f}")
        if cantidad <= 0:
            mensaje = '⚠️  La cantidad debe ser un número positivo.'
            escribir_log(mensaje)
        else:
            saldo += cantidad  # Suma al saldo actual
            mensaje = f'✅  Consignación exitosa. Nuevo saldo: ${saldo:,.2f}'
            escribir_log(mensaje)
    except ValueError:
        mensaje = '⚠️  Entrada inválida. Ingrese un valor numérico.'  # Validación de errores de entrada
        escribir_log(mensaje)
    return saldo  # Retorna el saldo actualizado


def cajero_automatico():
    '''
    Función principal que ejecuta el menú del cajero automático en bucle,
    permitiendo al usuario realizar múltiples operaciones hasta salir.
    '''
    saldo = 1_000_000  # Variable que representa el saldo inicial del usuario
    escribir_log("=== Inicio de la sesión del cajero automático ===")
    while True:  # Bucle infinito hasta que el usuario seleccione 'Salir'
        mostrar_menu()  # Mostrar el menú de opciones
        opcion = input('Seleccione una opción (1-4): ')  # Captura de la opción del usuario
        escribir_log(f"Opción seleccionada: {opcion}")
        if opcion == '1':
            consultar_saldo(saldo)
        elif opcion == '2':
            saldo = retirar_dinero(saldo)
        elif opcion == '3':
            saldo = consignar_dinero(saldo)
        elif opcion == '4':
            escribir_log('👋  Gracias por usar el cajero. ¡Hasta luego!\n=== Fin de la sesión del cajero automático ===')
            break  # Salida del bucle y del programa
        else:
            mensaje = '⚠️  Opción no válida. Intente nuevamente.'  # Manejo de opciones inválidas
            escribir_log(mensaje)



# Punto de entrada del programa
if __name__ == '__main__':
    cajero_automatico()  # Llama a la función principal para iniciar el cajero automático
    
'''
__name__	                -> Variable especial que indica si el archivo es principal o importado
'__main__'                  -> Valor de __name__ cuando se ejecuta el script directamente
if __name__ == '__main__'   -> Controla que cierto código solo se ejecute si el archivo se ejecuta y no al importarse
'''