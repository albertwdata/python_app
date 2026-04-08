import unittest
import contextlib
import io


class LoggingUtilTestCase(unittest.TestCase):

    def test_standard_out_formatter_for_message(self):

        with contextlib.redirect_stdout(io.StringIO()) as f:

            # configure logging
            import logging
            import sys
            from utils import logging_util as lg

            formatter = lg.StandardOutFormatter()

            handler = logging.StreamHandler(stream=sys.stdout)
            handler.setFormatter(formatter)

            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)

            # log message
            logger.debug('message')
            stdout_str = f.getvalue()

        self.assertIn('time: ', stdout_str)
        self.assertIn('logger: ', stdout_str)
        self.assertIn('module: ', stdout_str)
        self.assertIn('function: ', stdout_str)
        self.assertIn('level: ', stdout_str)
        self.assertIn('message: ', stdout_str)
        self.assertNotIn('\n\ndetails:\n\n', stdout_str)
        self.assertNotIn('\n\nexception:\n\n', stdout_str)
        self.assertNotIn('\n\nstack:\n\n', stdout_str)


    def test_standard_out_formatter_for_details(self):

        with contextlib.redirect_stdout(io.StringIO()) as f:

            # configure logging
            import logging
            import sys
            from utils import logging_util as lg

            formatter = lg.StandardOutFormatter()

            handler = logging.StreamHandler(stream=sys.stdout)
            handler.setFormatter(formatter)

            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)

            # log details
            details_dl = {
                'detail1': 'value1',
                'detail2': 'value2'
            }

            logger.debug('message', extra={'details': details_dl})
            stdout_str = f.getvalue()

        self.assertIn('time: ', stdout_str)
        self.assertIn('logger: ', stdout_str)
        self.assertIn('module: ', stdout_str)
        self.assertIn('function: ', stdout_str)
        self.assertIn('level: ', stdout_str)
        self.assertIn('message: ', stdout_str)
        self.assertIn('\n\ndetails:\n\n', stdout_str)
        self.assertNotIn('\n\nexception:\n\n', stdout_str)
        self.assertNotIn('\n\nstack:\n\n', stdout_str)


    def test_standard_out_formatter_for_exception(self):

        with contextlib.redirect_stdout(io.StringIO()) as f:

            # configure logging
            import logging
            import sys
            from utils import logging_util as lg

            formatter = lg.StandardOutFormatter()

            handler = logging.StreamHandler(stream=sys.stdout)
            handler.setFormatter(formatter)

            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)

            # log exception
            try:
                raise ValueError('test value error')
            except ValueError:
                logger.exception('message', stack_info=False)
                stdout_str = f.getvalue()

        self.assertIn('time: ', stdout_str)
        self.assertIn('logger: ', stdout_str)
        self.assertIn('module: ', stdout_str)
        self.assertIn('function: ', stdout_str)
        self.assertIn('level: ', stdout_str)
        self.assertIn('message: ', stdout_str)
        self.assertNotIn('\n\ndetails:\n\n', stdout_str)
        self.assertIn('\n\nexception:\n\n', stdout_str)
        self.assertNotIn('\n\nstack:\n\n', stdout_str)


    def test_standard_out_formatter_for_exception_stack(self):

        with contextlib.redirect_stdout(io.StringIO()) as f:

            # configure logging
            import logging
            import sys
            from utils import logging_util as lg

            formatter = lg.StandardOutFormatter()

            handler = logging.StreamHandler(stream=sys.stdout)
            handler.setFormatter(formatter)

            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)

            # log exception with stack info
            try:
                raise ValueError('test value error')
            except ValueError:
                logger.exception('message', stack_info=True)
                stdout_str = f.getvalue()

        self.assertIn('time: ', stdout_str)
        self.assertIn('logger: ', stdout_str)
        self.assertIn('module: ', stdout_str)
        self.assertIn('function: ', stdout_str)
        self.assertIn('level: ', stdout_str)
        self.assertIn('message: ', stdout_str)
        self.assertNotIn('\n\ndetails:\n\n', stdout_str)
        self.assertIn('\n\nexception:\n\n', stdout_str)
        self.assertIn('\n\nstack:\n\n', stdout_str)


    def test_standard_out_formatter_for_details_exception_stack(self):

        with contextlib.redirect_stdout(io.StringIO()) as f:

            # configure logging
            import logging
            import sys
            from utils import logging_util as lg

            formatter = lg.StandardOutFormatter()

            handler = logging.StreamHandler(stream=sys.stdout)
            handler.setFormatter(formatter)

            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)

            # log details, exception, and stack info
            details_dl = {
                'detail1': 'value1',
                'detail2': 'value2'
            }

            try:
                raise ValueError('test value error')
            except ValueError:
                logger.exception('message', stack_info=True, extra={'details': details_dl})
                stdout_str = f.getvalue()

        self.assertIn('time: ', stdout_str)
        self.assertIn('logger: ', stdout_str)
        self.assertIn('module: ', stdout_str)
        self.assertIn('function: ', stdout_str)
        self.assertIn('level: ', stdout_str)
        self.assertIn('message: ', stdout_str)
        self.assertIn('\n\ndetails:\n\n', stdout_str)
        self.assertIn('\n\nexception:\n\n', stdout_str)
        self.assertIn('\n\nstack:\n\n', stdout_str)


if __name__ == '__main__':
    unittest.main()
