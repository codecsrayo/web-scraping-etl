#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import os

# Asegurar que el script principal se puede importar
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar funciones a probar
try:
    from scraping_module import url_base, busqueda, headers, get_laptop_data, analyze_data
except ImportError:
    print("No se puede importar el módulo scraping_module")


class TestScraping(unittest.TestCase):
    """Pruebas para el script de scraping"""

    def test_url_exists(self):
        """Verificar que la URL base existe"""
        self.assertIsNotNone(url_base)
        self.assertTrue(isinstance(url_base, str))
        self.assertTrue(url_base.startswith('http'))

    def test_headers_has_user_agent(self):
        """Verificar que los headers incluyen un User-Agent"""
        self.assertIsNotNone(headers)
        self.assertTrue(isinstance(headers, dict))
        self.assertIn('User-Agent', headers)
        self.assertTrue(len(headers['User-Agent']) > 10)  # Asegurar que el User-Agent no esté vacío

    def test_search_term_exists(self):
        """Verificar que el término de búsqueda existe"""
        self.assertIsNotNone(busqueda)
        self.assertTrue(isinstance(busqueda, str))
        self.assertTrue(len(busqueda) > 0)


if __name__ == '__main__':
    unittest.main()
