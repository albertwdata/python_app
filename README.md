# Configuration

The python app looks to env var APP_CONFIG_PATH for the config path.

If APP_CONFIG_PATH is none, the python app uses: "~/.app/config.toml".

Options:
1. Provide path to config via env var: "APP_CONFIG_PATH".
2. Place config in: "~/.app/config.toml".

The test "tests/config_tests/config_test.py" requires the config.toml to contain:
``` toml
# hello world
[hello]
hello_str = 'Hello from config.toml!'
```
