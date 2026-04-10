# %%
# import modules
import os
import tomllib
from pathlib import Path
import logging
import logging.config


# %%
# load config
app_config_path = os.getenv(
    'APP_CONFIG_PATH',
    Path.home().joinpath('.app/config.toml')
)

with open(app_config_path, 'rb') as f:
    config = tomllib.load(f)


# %%
# configure logging
# created logger
app_logger = logging.getLogger('app_logger')


# convert log filename to absolute path
log_path_from_user_dir = config['logging']['handlers']['file_handler']['filename']
log_path = Path(log_path_from_user_dir).expanduser()
config['logging']['handlers']['file_handler']['filename'] = log_path


# configure logger
logging.config.dictConfig(config['logging'])

app_logger.debug('configured logging')


# %%
