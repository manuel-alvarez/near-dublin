import json
import unittest

from main import distance, read_cities


class TestReader(unittest.TestCase):
    # TODO: Add right urls
    empty_url = ""
    small_url = ""
    # large_url will be, initially, the full list
    large_url = "https://gist.githubusercontent.com/mwtorkowski/16ca26a0c072ef743734/raw/2aa20e8de9f2292d58a4856602c1f0634d8611a7/cities.json"
    # This is not a valid url
    wrong_url = "thisisnotavalidurl"
    # This url returns a bad formatted list
    format_url = ""

    def test_read_empty(self):
        self.assertEqual(len(read_cities()), 0)

    def test_read_empty_list(self):
        self.assertEqual(len(read_cities(self.empty_url)), 0)

    def test_read_small_list(self):
        self.assertEqual(len(read_cities(self.small_url)), 2)

    def test_read_large_list(self):
        self.assertEqual(len(read_cities(self.large_url)), 661)

    def test_read_wrong_url(self):
        self.assertIsNone(read_cities(self.wrong_url))

    def test_read_bad_formatted_list(self):
        self.assertIsNone(read_cities(self.format_url))


class TestDistance(unittest.TestCase):
    point_a = {'lat': 42.0, 'lon': 23.0}
    point_b = {'lat': 42.000001, 'lon': 23.00001}
    point_c = {'lat': 55.0, 'lon': 230.0}
    point_d = {'lon': 230.0}
    point_e = 0
    point_f = 'This is not a point'

    def test_near(self):
        dist = distance(self.point_a, self.point_b)
        self.assertLess(dist, 1, "Distance should be less than 1km")

    def test_far(self):
        dist = distance(self.point_a, self.point_c)
        self.assertGreater(dist, 500, "Distance should be greater than 500km")

    def test_same(self):
        dist = distance(self.point_a, self.point_a)
        self.assertEqual(dist, 0, "Distance should be 0")

    def test_wrong(self):
        self.assertIsNone(distance(self.point_a, self.point_d), "Distance should not be valid")
        self.assertIsNone(distance(self.point_d, self.point_a), "Distance should not be valid")
        self.assertIsNone(distance(self.point_a, self.point_e), "Distance should not be valid")
        self.assertIsNone(distance(self.point_e, self.point_a), "Distance should not be valid")
        self.assertIsNone(distance(self.point_a, self.point_f), "Distance should not be valid")
        self.assertIsNone(distance(self.point_f, self.point_a), "Distance should not be valid")