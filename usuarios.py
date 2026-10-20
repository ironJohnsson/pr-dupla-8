def validar_email(email: str) -> bool:
    """Valida se o email atende aos critérios de aceite."""
    if not isinstance(email, str):
        return False

    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    if not usuario:
        return False

    partes_dominio = dominio.split(".")
    if len(partes_dominio) < 2:
        return False

    if not all(partes_dominio):
        return False

    return True
