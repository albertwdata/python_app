# %%
# import modules
import os
import tomllib
from pathlib import Path


# %%
# load config
app_config_path = os.getenv(
    'APP_CONFIG_PATH',
    Path.home().joinpath('.app/config.toml')
)

with open(app_config_path, 'rb') as f:
    config = tomllib.load(f)


# %%
