"""custom_exceptions.py

Raise these errors in code to handle them later.

"""


class NotFoundException(Exception):
    def __init__(self, message="Resource not found."):
        self.message = message
        super().__init__(self.message)
    pass


class NotEnoughPermissionsException(Exception):
    def __init__(self,
                 message="Not enough permissions to call this resource."):
        self.message = message
        super().__init__(self.message)

    pass


class ParameterException(Exception):
    def __init__(self,
                 message="Passed parameter is not correct."):
        self.message = message
        super().__init__(self.message)

    pass


class IdEncryptionException(Exception):
    def __init__(self,
                 message="Invalid id token in url path."):
        self.message = message
        super().__init__(self.message)

    pass


class TheGameHasNotStartedException(Exception):
    def __init__(self,
                 message="The game has not started yet"):
        self.message = message
        super().__init__(self.message)

    pass