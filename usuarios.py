def validar_email(email: str) -> bool:
    """Valida se o email atende aos critérios de aceite."""
    if not isinstance(email, str) or " " in email or email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")
    partes = dominio.split(".")
    return bool(usuario) and len(partes) >= 2 and all(partes)

