import sys
import logging

# --------------------- logger start -----------------------------
# 建立logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename='{}.log'.format(__file__[:-3]), filemode="w")

formatter = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)-8s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')  # 設定 formatter to sys.stderr

console = logging.StreamHandler(sys.stderr)  # 設定 Handler to sys.stderr
console.setFormatter(formatter)  # 把 formatter 設定到 handler

logger = logging.getLogger(__name__)  # 建立 logger
logger.addHandler(console)  # 加入 handler

# --------------------- logger end -----------------------------

# output log
logger.debug("loggin message, DEBUG")
logger.info("loggin message, INFO")
logger.warning("loggin message, WARNING")
logger.error("loggin message, ERROR")
logger.critical("loggin message, CRITICAL")

print("-" * 50 + "\n")
