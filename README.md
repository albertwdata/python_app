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

## Logging
Logging configuation should be added to the config.toml:
``` toml
# logging
[logging]
version = 1
disable_existing_loggers = true


[logging.formatters.console_formatter]
'()' = 'utils.logging_util.StandardOutFormatter'


[logging.formatters.json_formatter]
'()' = 'utils.logging_util.JsonFormatter'


[logging.handlers.console_handler]
class = 'logging.StreamHandler'
stream = 'ext://sys.stdout'
formatter = 'console_formatter'
level = 'WARNING'


[logging.handlers.file_handler]
class = 'logging.handlers.TimedRotatingFileHandler'
filename = '~/.app/logs/log.jsonl'
when = 'D'
interval = 1
backupCount = 2
encoding = 'utf8'
delay = false
utc = false
formatter = 'json_formatter'
level = 'DEBUG'


[logging.loggers.app_logger]
handlers = [ 'console_handler', 'file_handler' ]
level = 'DEBUG'
propagate = false
```
