#!/usr/bin/env python3
"""unittests for the utils module"""
from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Any
import unittest.mock as mock


class TestAccessNestedMap(unittest.TestCase):
    """class to test access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Any) -> None:
        """test method fot the
        nested map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str]) -> None:
        """testing if exception is raised when
        supposed to
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class to test function get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """mocking get_json
        """
        attrs = {'json.return_value': test_payload}
        with mock.patch("requests.get", return_value=mock.Mock(**attrs)) as mocked_get:
            self.assertEqual(get_json(test_url), test_payload)
            mocked_get.assert_called_once_with(test_url)
