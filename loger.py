import logging

# получение пользовательского логгера и установка уровня логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
logger.addHandler(py_handler)


def logger_read(log):
    lt, ls = log[0], log[1]
    match ls:
        case "warn":
            logger.warning(lt)
        case "err":
            logger.error(lt)
        case "info":
            logger.info(lt)
        case "crt":
            logger.critical(lt)
        case _:
            logger.debug(lt)