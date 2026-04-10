# %%
# import modules
from config import config as cfg


# %%
# get logger
# loggers are singleton
    # so we can import logging and call:
        # app_logger = logging.getLogger('app_logger')
        # this must be done only after logging is configured in config module
app_logger = cfg.app_logger


# %%
# define main
def main():
    print('Hello from app.py!')
    app_logger.debug('run main')

if __name__ == '__main__':
    main()


# %%
