import logging

def set_custom_logger(name:str, level=logger.DEBUG):
  formatter = logging.Formatter(fmt="%(asctime)s: %(levelname)s: %(module)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
  handler = logging.StreamHandler()
  handler.setFormatter(formatter)
  logger = logging.getLogger(name)
  logger.setLevel(level)
  logger.addHandler(handler)
  return logger

if __name__ == "__main__":
  pass # This is a lib file not an application

