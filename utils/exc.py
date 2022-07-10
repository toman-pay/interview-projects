class AppException(Exception):
    code = 0
    message = ''
    status = 0
    extra = dict()

    def __init__(self, for_api=True, message='', status=0, **kwargs):
        self.for_api = for_api
        if message:
            self.message = message
        if status:
            self.status = status
        if kwargs:
            self.extra = kwargs
        self.set_complex_message()

    def set_complex_message(self):
        pass

    def __str__(self):
        return '{}-{}'.format(self.code, self.message)


class ConnectionErrorException(AppException):
    message = "Internal connection error occur!"
    code = 2001
    status = 503


class NotEnoughDataException(AppException):
    message = "Need more data!"
    code = 2002
    status = 422


class RouteHostDuplicateException(AppException):
    message = "The input 'host' exists!"
    code = 2003
    status = 409


class PasswordValidationException(AppException):
    message = "Password is wrong!"
    code = 2004
    status = 400


class UnexpectedErrorException(AppException):
    message = "An unexpected error occur!"
    code = 2005
    status = 503


class PermissionDeniedExceptions(AppException):
    message = "Permission denied!"
    code = 2007
    status = 400


class UniqueViolationException(AppException):
    message = "Entry exists!"
    code = 2008
    status = 409


class NotFoundException(AppException):
    message = "Not found!"
    code = 2009
    status = 404


class CustomMessageException(AppException):
    code = 2011
    status = 422

    def set_complex_message(self):
        self.message = f"{self.extra.get('custom_message')}!"
