import pydirectinput
import time
import random

# Dicionário de teclas mapeadas para facilitar o log
KEY_MAP = {
    'u': 'U',
    '1': '1',
    'g': 'G',
    'w': 'W',
    'shift': 'SHIFT'
}

def log_action(action, key, duration=None):
    """Exibe qual ação e tecla estão sendo executadas, e o tempo de espera quando aplicável."""
    msg = f"[{time.strftime('%H:%M:%S')}] {action.upper()} - Tecla: {KEY_MAP[key]}"
    if duration:
        msg += f" | Tempo de espera: {duration:.2f}s"
    print(msg)

def countdown(seconds):
    """Exibe uma contagem regressiva no console."""
    print(f"O script começará em {seconds} segundos...")
    for i in range(seconds, 0, -1):
        print(f"Começando em: {i}...")
        time.sleep(1)

def wait_with_countdown(seconds):
    """Espera com uma contagem regressiva detalhada."""
    for i in range(int(seconds), 0, -1):
        print(i)
        time.sleep(1)
    # Ajusta para valores fracionários no final da contagem
    remainder = seconds - int(seconds)
    if remainder > 0:
        time.sleep(remainder)

def press_key(key):
    """Pressiona rapidamente uma tecla."""
    log_action("Pressionando", key)
    pydirectinput.press(key)

def hold_key(key, duration):
    """Mantém uma tecla pressionada por um determinado tempo."""
    log_action("Pressionando e segurando", key, duration)
    pydirectinput.keyDown(key)
    time.sleep(duration)
    pydirectinput.keyUp(key)
    log_action("Soltando", key)

def main(timer_duration=10):
    """Executa o script principal com contagem regressiva e tempos detalhados."""
    countdown(timer_duration)

    while True:
        # Pressiona 'U' com espera aleatória
        wait_time = random.uniform(2.5, 2.6)
        press_key('u')
        log_action("Esperando após pressionar", 'u', wait_time)
        wait_with_countdown(wait_time)

        # Pressiona '1' com espera aleatória
        wait_time = random.uniform(37, 39)
        press_key('1')
        log_action("Esperando após pressionar", '1', wait_time)
        wait_with_countdown(wait_time)

        # # Pressiona 'G' com espera aleatória
        # wait_time = random.uniform(6.5, 7.5)
        # press_key('g')
        # log_action("Esperando após pressionar", 'g', wait_time)
        # wait_with_countdown(wait_time)

        # Pressiona SHIFT com espera aleatória
        wait_time = random.uniform(6.1, 6.2)
        press_key('shift')
        log_action("Esperando após pressionar", 'shift', wait_time)
        wait_with_countdown(wait_time)

        # Pressiona SHIFT com espera aleatória
        wait_time = random.uniform(6.1, 6.2)
        press_key('shift')
        log_action("Esperando após pressionar", 'shift', wait_time)
        wait_with_countdown(wait_time)

        # Pressiona e segura 'W' por um tempo aleatório
        hold_time = random.uniform(0.9,1.0)
        hold_key('w', hold_time)

if __name__ == "__main__":
    main(timer_duration=2)  # Altere o tempo da contagem regressiva inicial aqui
