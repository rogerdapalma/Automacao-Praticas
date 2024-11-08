import pydirectinput
import time

def log_action(action, key, duration=None):
    """Exibe qual ação e tecla estão sendo executadas."""
    msg = f"[{time.strftime('%H:%M:%S')}] {action.upper()} - Tecla: {key.upper()}"
    if duration:
        msg += f" | Tempo de espera: {duration:.2f}s"
    print(msg)

def press_key(key):
    """Pressiona rapidamente uma tecla."""
    log_action("Pressionando", key)
    pydirectinput.press(key)

def hold_and_release_key(key, duration=0.5):
    """Pressiona e solta uma tecla em intervalos regulares."""
    log_action("Pressionando", key)
    pydirectinput.keyDown(key)
    time.sleep(duration)
    log_action("Soltando", key)
    pydirectinput.keyUp(key)

def main():
    print("Iniciando sequência de alternância de 'W' e pressionamento de 'B' a cada 4 segundos...")

    try:
        while True:
            # Alterna W pressionando e soltando
            hold_and_release_key('w', duration=0.5)  # Alterna W a cada 0,5s

            # Pressiona 'B' com intervalo de 4 segundos
            press_key('b')  # Pressiona 'B'
            time.sleep(4)  # Espera 4 segundos antes de pressionar 'B' novamente
    except KeyboardInterrupt:
        print("\nScript encerrado com segurança.")

if __name__ == "__main__":
    main()
