import unittest
import time
from datetime import datetime, UTC
from utils import time_helper as th


class TimeHelperTestCase(unittest.TestCase):

    def test_format_seconds_since_epoch_to_iso(self):
        # get example value
        seconds_since_epoch_float = time.time()

        # run test function
        test_function_iso_str = th.format_seconds_since_epoch_to_iso(seconds_since_epoch_float)

        # run comparison function
        strftime_iso_str = datetime.fromtimestamp(
            timestamp=seconds_since_epoch_float,
            tz=UTC
        ).strftime('%Y-%m-%dT%H:%M:%S.%f%:z')

        self.assertEqual(test_function_iso_str, strftime_iso_str)


if __name__ == '__main__':
    unittest.main()
