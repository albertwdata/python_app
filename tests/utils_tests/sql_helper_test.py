import unittest
from utils import sql_helper as sh


class SqlHelperTestCase(unittest.TestCase):

    def test_add_sql_statement_terminator_if_missing(self):
        # get example value
        test_none = 'Hello World'
        test_n = 'Hello World\n'
        test_s = 'Hello World;'
        test_sn = 'Hello World;\n'
        test_ns = 'Hello World\n;'
        test_nsn = 'Hello World\n;\n'

        # run test function
        test_none_returned = sh.add_sql_statement_terminator_if_missing(test_none)
        test_n_returned = sh.add_sql_statement_terminator_if_missing(test_n)
        test_s_returned = sh.add_sql_statement_terminator_if_missing(test_s)
        test_sn_returned = sh.add_sql_statement_terminator_if_missing(test_sn)
        test_ns_returned = sh.add_sql_statement_terminator_if_missing(test_ns)
        test_nsn_returned = sh.add_sql_statement_terminator_if_missing(test_nsn)

        # run comparison
        self.assertEqual(test_none_returned, test_none + ';')
        self.assertEqual(test_n_returned, test_n + ';')
        self.assertEqual(test_s_returned, test_s)
        self.assertEqual(test_sn_returned, test_sn)
        self.assertEqual(test_ns_returned, test_ns)
        self.assertEqual(test_nsn_returned, test_nsn)


if __name__ == '__main__':
    unittest.main()
