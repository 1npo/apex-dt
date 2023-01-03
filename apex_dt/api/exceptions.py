def gen_api_error_response(res):
    """Read an API response and generate an appropriate Python exception."""
    error_codes = {
        400: InvalidRequest,    #Try again in a few minutes.
        403: Unauthorized,      #Unauthorized / Unknown API key.
        404: PlayerNotFound,    #The player could not be found.
        405: ExternalError,     #External API error.
        410: UnknownPlatform,   #Unknown platform provided.
        429: RateLimitExceeded, #Rate limit reached.
        500: InternalError,     #Internal error.
    }
    
    error_code = res.status_code
    error_message = res.text

    raise error_codes[error_code](message=error_message, code=error_code, response=res)


class ApexAPIError(Exception):
    message = 'An unknown error occurred'
    code = -1
    response = None

    def __init__(
            self,
            message: str = None,
            code: str = None,
            response=None):

        self.response = response

        if message:
            self.message = message
        if code:
            self.code = code

    def __str__(self):
        if self.code:
            return f'{self.code}: {self.message}'
        return self.message


class InvalidRequest(ApexAPIError):
    pass

class Unauthorized(ApexAPIError):
    pass

class PlayerNotFound(ApexAPIError):
    pass

class ExternalError(ApexAPIError):
    pass

class UnknownPlatform(ApexAPIError):
    pass

class RateLimitExceeded(ApexAPIError):
    pass

class InternalError(ApexAPIError):
    pass

class MissingRequiredArgument(ApexAPIError):
    pass
