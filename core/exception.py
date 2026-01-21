from rest_framework.exceptions import APIException

class CustomValidationError(APIException):
    
    status_code = 400
    default_code = 'bad request'
    default_detail = 'error exist'
    
    def __init__(self, detail=None, code=None):
        if detail:
            super().__init__(detail, code)
        else:
            super().__init__(self.default_detail, self.default_code)