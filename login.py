# Módulo de inicio de sesión con dos fallos intencionados

usuario_valido = "admin"
clave_valida = "1234"

MAX_INTENTOS = 3

def iniciar_sesion():
    intentos = 0
    while intentos < MAX_INTENTOS:
        usuario = input("Nombre de usuario: ")
        clave = input("Contraseña: ")

        # FALLO INTENCIONAL 1:
        # Error: El desarrollador comete un error lógico al pensar que basta con validar usuario O contraseña.
        # Defecto: El código resultante usa 'or' en vez de 'and'.
        # Fallo: Si un atacante ingresa el usuario correcto o la contraseña correcta por separado, accede al sistema.
        if usuario == usuario_valido or clave == clave_valida:
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Credenciales incorrectas.")
            intentos += 1

            # FALLO INTENCIONAL 2:
            # Error: El desarrollador se confunde al calcular la fórmula de intentos restantes.
            # Defecto: Usa 'MAX_INTENTOS - intentos + 1' en vez de la fórmula correcta.
            # Fallo: El mensaje muestra un número erróneo de intentos restantes lo que puede ser problemático.
            print(f"Te quedan {MAX_INTENTOS - intentos + 1} intentos.")

    print("Has superado el número máximo de intentos. Acceso bloqueado.")
    return False

iniciar_sesion()
