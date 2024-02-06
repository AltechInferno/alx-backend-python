#!/usr/bin/env python3
"""testing the utils module.
"""
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""

    def create_test_class_instance(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        return TestClass()

    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        test_class = self.create_test_class_instance()

        with patch.object(test_class, "a_method", return_value=42) as memo_fxn:
            result1 = test_class.a_property()
            result2 = test_class.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            memo_fxn.assert_called_once()


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""

    def create_mock_response(self, payload: Dict) -> Mock:
        attrs = {'json.return_value': payload}
        return Mock(**attrs)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Tests `get_json`'s output."""
        with patch("requests.get", return_value=self.create_mock_response(test_payload)) as req_get:
            result = get_json(test_url)
            req_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str], expected: Union[Dict, int]) -> None:
        """Tests `access_nested_map` with valid inputs."""
        # Arrange & Act
        result = access_nested_map(nested_map, path)

        # Assert
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple[str], exception: Exception) -> None:
        """Tests `access_nested_map` exception handling."""
        # Assert
        with self.assertRaises(exception):
            # Act
            access_nested_map(nested_map, path)
