import unittest
from usuarios import validar_email


def test_valido():
    assert validar_email("ana@exemplo.com") is True


def test_sem_arroba():
    assert validar_email("ana.exemplo.com") is False


class TestEmail(unittest.TestCase):
    def test_none(self):
        self.assertFalse(validar_email(None))

    def test_dominio_incompleto(self):
        self.assertFalse(validar_email("ana@empresa."))

    def test_usuario_vazio(self):
        self.assertFalse(validar_email("@empresa.com"))