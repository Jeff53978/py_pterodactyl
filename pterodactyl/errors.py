class AuthenticationError(Exception):
    """Raised when authentication fails"""
    pass

class InvalidCredentials(AuthenticationError):
    """Raised when invalid credentials are provided"""
    pass