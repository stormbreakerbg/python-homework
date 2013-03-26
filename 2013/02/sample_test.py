import unittest
import solution


class SecondHomeworkSimpleTests(unittest.TestCase):

    def test_groupby_simple_types(self):
        expected = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        actual = solution.groupby(lambda x: 'odd' if x % 2 else 'even',
                                  [1, 2, 3, 5, 8, 9, 10, 12])
        self.assertEqual(expected, actual)

    def test_iterate_start_with_identity_function(self):
        # there's no such word, really
        bracketisers = solution.iterate(lambda x: '(' + x + ')')
        no_brackets = next(bracketisers)
        self.assertEqual('hello world', no_brackets('hello world'))

    def test_iterate_ordered_calls(self):
        powers_of_two = solution.iterate(lambda x: x * 2)
        f = next(powers_of_two)
        self.assertEqual(1 * 'eggs', f('eggs'))
        f = next(powers_of_two)
        self.assertEqual(2 * 'ham', f('ham'))
        f = next(powers_of_two)
        self.assertEqual(4 * 'spam', f('spam'))
        f = next(powers_of_two)
        self.assertEqual(8 * 'spameggs', f('spameggs'))

    def test_zip_with_simple(self):
        first_names = ['Charlie', 'Dizzy']
        last_names = ['Parker', 'Gillespie']
        expected = ['CharlieParker', 'DizzyGillespie']
        actual = solution.zip_with(str.__add__, first_names, last_names)
        self.assertEqual(expected, list(actual))

    def test_zip_with_empty(self):
        first_names = ['Charlie', 'Dizzy']
        last_names = []
        expected = []
        actual = solution.zip_with(str.__add__, first_names, last_names)
        self.assertEqual(expected, list(actual))

    def test_zip_with_one_element(self):
        first = [1, 2]
        second = [3]
        expected = [(1, 3)]
        actual = solution.zip_with(lambda x, y: (x, y),
                                   first, second)
        self.assertEqual(expected, list(actual))

    def test_zip_with_three_iterables(self):
        first = ('a', 'b', 'c', 'd')
        second = ['e', 'f', 'g']
        third = ('h', 'i', 'j', 'k', 'l')
        expected = ['aeh', 'bfi', 'cgj']
        actual = solution.zip_with(lambda x, y, z: x + y + z,
                                   first, second, third)
        self.assertEqual(expected, list(actual))

    def test_cache_call_is_cached(self):
        call_count = 0

        def double(x):
            nonlocal call_count
            call_count += 1
            return 2 * x

        cached_double = solution.cache(double, 2)
        self.assertEqual(256, cached_double(128))
        self.assertEqual(256, cached_double(128))
        self.assertEqual(1, call_count)
        self.assertEqual(64, cached_double(32))
        self.assertEqual(64, cached_double(32))
        self.assertEqual(2, call_count)
        self.assertEqual(32, cached_double(16))
        self.assertEqual(32, cached_double(16))
        self.assertEqual(3, call_count)
        self.assertEqual(256, cached_double(128))
        self.assertEqual(4, call_count)

    def test_cache_zero_times(self):
        call_count = 0

        def double(x):
            nonlocal call_count
            call_count += 1
            return 2 * x

        cached_double = solution.cache(double, 0)
        self.assertEqual(256, cached_double(128))
        self.assertEqual(256, cached_double(128))
        self.assertEqual(2, call_count)

if __name__ == "__main__":
    unittest.main()
