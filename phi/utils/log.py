import logging
import datetime
import os

from phi.cli.settings import phi_cli_settings
from rich.logging import RichHandler


# get current datatime as file name
now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d_%H-%M-%S")

# create log directory if not exists
if not os.path.exists("log"):
    os.makedirs("log")


LOGGER_NAME = "phi"
LOGGER_FILE = f"log/phi_{file_name}.log"


def get_logger(logger_name: str, log_file: str) -> logging.Logger:
    # https://rich.readthedocs.io/en/latest/reference/logging.html#rich.logging.RichHandler
    # https://rich.readthedocs.io/en/latest/logging.html#handle-exceptions
    rich_handler = RichHandler(
        show_time=False,
        rich_tracebacks=False,
        show_path=True if phi_cli_settings.api_runtime == "dev" else False,
        tracebacks_show_locals=False,
    )
    rich_handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(name)s %(levelname)s %(filename)s:%(funcName)s:%(lineno)d %(message)s",
            datefmt="[%X]",
        )
    )

    file_handler = logging.FileHandler(log_file)  # 设置日志输出到文件
    file_handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(name)s %(levelname)s %(filename)s:%(funcName)s:%(lineno)d %(message)s",
            datefmt="[%X]",
        )
    )

    _logger = logging.getLogger(logger_name)
    _logger.addHandler(rich_handler)
    _logger.addHandler(file_handler)  # 添加文件输出处理器
    _logger.setLevel(logging.INFO)
    _logger.propagate = False
    return _logger


logger: logging.Logger = get_logger(LOGGER_NAME, LOGGER_FILE)


def set_log_level_to_debug():
    _logger = logging.getLogger(LOGGER_NAME)
    _logger.setLevel(logging.DEBUG)
