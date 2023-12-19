"""error_handler.py

This package contains ErrorHandler class.

"""
import functools

from flask import make_response, jsonify, abort
from jwt import InvalidTokenError
from marshmallow import ValidationError

from app.utils.custom_exceptions import NotFoundException, \
    NotEnoughPermissionsException, ParameterException, IdEncryptionException, \
    TheGameHasNotStartedException


def add_api_error_responses(controller_func):
    #  Multiple decorators confuse their identity.
    #  The @functools.wraps decorator, which will preserve information about
    #  the original function.
    @functools.wraps(controller_func)
    def wrapper(*args, **kwargs):
        try:
            return controller_func(*args, **kwargs)
        except ValidationError as e:
            ErrorHandler.response_400(message=str(e))
        except NotFoundException as e:
            ErrorHandler.response_404(message=str(e))
        except NotEnoughPermissionsException as e:
            ErrorHandler.response_403(message=str(e))
        except ParameterException as e:
            ErrorHandler.response_400(message=str(e))
        except IdEncryptionException as e:
            ErrorHandler.response_400(message=str(e))
        except InvalidTokenError as e:
            ErrorHandler.response_400(message=str(e))
        except TheGameHasNotStartedException as e:
            ErrorHandler.response_201(message=str(e))
    return wrapper


class ErrorHandler:
    """This class abstracts error responses.

    """

    @staticmethod
    def response_404(message: str):
        """ Return 404 error

        :param message: error message
        """
        abort(make_response(jsonify(message=message), 404))

    @staticmethod
    def response_403(message: str):
        """ Return 403 error

        :param message: error message
        """
        abort(make_response(jsonify(message=message), 403))

    @staticmethod
    def response_400(message: str):
        """ Return 400 error

        :param message: error message
        """
        abort(make_response(jsonify(message=message), 400))

    @classmethod
    def response_201(cls, message):
        """ Return 201 status

                :param message: message
                """
        abort(make_response(jsonify(message=message), 201))
