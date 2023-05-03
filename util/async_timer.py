"""
Модуль декоратора для вычисления времени выполнения
асинхронной функции
"""
import time

def async_timed(func):
  async def wrapper(*args, **kwargs):
    print(f'Старт выполнения {func} с аргументами {args} {kwargs}')
    dt_1 = time.time()
    try:
      return await func(*args, **kwargs)
    finally:
      dt_2 = time.time() - dt_1
      print(f'{func} с аргументами {args} {kwargs} завершилась за {dt_2}')
  return wrapper