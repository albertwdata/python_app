# %%
# import modules
import logging
import json

from utils import time_helper as th


# %%
# define custom formatters
class StandardOutFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord):

        log_li = [
            # python docs indicate that LogRecord.created is a value returned from time.time_ns()
                # time.time_ns() returns nano seconds since epoch as int
                # but LogRecord.created appears to be seconds since epoch as float
            'time: ' + th.format_seconds_since_epoch_to_iso(record.created),
            'logger: ' + record.name,
            'module: ' + record.module,
            'function: ' + record.funcName,
            'level: ' + record.levelname,
            'message: ' + record.getMessage()
        ]

        log_str = '\n' + ' - '.join(log_li)

        if hasattr(record, 'details'):
            log_str += '\n\ndetails:\n\n' + json.dumps(record.details, indent=4)

        if record.exc_info is not None:
            log_str += '\n\nexception:\n\n' + self.formatException(record.exc_info)

        if record.stack_info is not None:
            log_str += '\n\nstack:\n\n' + self.formatStack(record.stack_info)

        return log_str


# %%
