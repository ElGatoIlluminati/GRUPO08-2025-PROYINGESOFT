from django.test import TestCase
import unittest
import requests
from django.contrib.auth.models import User
import random
import string

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "http://127.0.0.1:8000/login/"

    def test_login_valido(self):
        """Usuario y contraseña correctos"""

        response = requests.post(self.url, data={
            "username": "editor54",
            "pwd": "1234"
        }, allow_redirects=False)

        self.assertEqual(response.status_code, 302)
        self.assertIn("Location", response.headers)

    def test_login_usuario_invalido(self):
        """Usuario no existe"""
        response = requests.post(self.url, data={
            "username": "hola",
            "pwd": "1234"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Nombre de usuario o contraseña incorrectos.", response.text)

    @classmethod
    def tearDownClass(cls):
        pass


def generar_usuario_random():
    return 'user_' + ''.join(random.choices(string.ascii_lowercase, k=5))

class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "http://127.0.0.1:8000/register/"

    def test_registro_valido(self):
        response = requests.post(self.url, data={
            "username": "prueba4",
            "email": "hola@gmail.com",
            "password": "Clave1234",
            "role": "editor"
        }, allow_redirects=False)  

        self.assertIn(response.status_code, [200, 302])

        if response.status_code == 302:
            self.assertIn('Location', response.headers)

    def test_registro_datos_invalidos(self):
        """Registro con datos faltantes - Esperamos error 400 Bad Request"""
        response = requests.post(self.url, data={
            "username": "",
            "email": "correo@example.com",
            "password": "Clave1234",
            "role": "lector"
        })
        self.assertEqual(response.status_code, 400)
        if "username" == "":
            self.assertIn("Por favor ingresa un nombre de usuario.", response.text)
        if "email" == "":
            self.assertIn("El correo electrónico es obligatorio.", response.text)
        if "password" == "":
            self.assertIn("Por favor ingresa la contraseña.", response.text)

    @classmethod
    def tearDownClass(cls):
        pass
