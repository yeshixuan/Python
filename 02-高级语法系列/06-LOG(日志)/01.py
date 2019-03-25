import logging

# logging.basicConfig(level=logging.DEBUG)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename="my.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
#不经过设置，默认debug,info不显示
logging.debug("This is a debug log.")
logging.info("This is a info log.")
# logging.warning("This is a warning log.")
logging.warning("%s is %d years old.","Tome",10)
logging.error("Some one delete the log file.", exc_info=True, stack_info=True, extra={"user":"Tom","ip":"47.98.43.222"})
logging.critical("This is a critical log.")

# logging.log(logging.DEBUG,"This is a debug log.")
# logging.log(logging.INFO,"This is a info log.")
# logging.log(logging.WARNING, "This is a warning log.")
# logging.log(logging.ERROR, "This is a error log.")
# logging.log(logging.CRITICAL,"This is a critical log.")