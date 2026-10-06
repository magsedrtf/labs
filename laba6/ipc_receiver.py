import posix_ipc
import sys

QUEUE_NAME = "/sys_prog_queue"

try:
    mq = posix_ipc.MessageQueue(QUEUE_NAME)
except posix_ipc.ExistentialError:
    print("[ОШИБКА] Очередь не найдена в ядре. Сначала запустите ipc_sender.py!")
    sys.exit(1)

print("[ПРИЕМНИК] Успешно подключено к системной очереди. Начинаем чтение...")


while True:
    binary_data, priority = mq.receive()
    
    message = binary_data.decode('utf-8')
    print(f"[ПРИЕМНИК] Получено из ядра: '{message}'")
    
    if "5" in message:
        print("[ПРИЕМНИК] Получено последнее сообщение.")
        break

mq.close()
posix_ipc.unlink_message_queue(QUEUE_NAME)
print("[ПРИЕМНИК] Очередь удалена из операционной системы.")