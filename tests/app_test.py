import unittest
import contextlib
import io


class AppTestCase(unittest.TestCase):

    def test_main(self):

        with contextlib.redirect_stdout(io.StringIO()) as f:

            import app

            app.main()

            s = f.getvalue()

        self.assertEqual(s, 'Hello from app.py!\n')


if __name__ == '__main__':
    unittest.main()
