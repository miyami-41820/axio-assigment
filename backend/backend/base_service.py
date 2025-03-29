from rest_framework import status

class BaseService(object):
    def __init__(self):
        self.response = {
            "code": "",
            "data": {},
            "errors": {},
            "message": ""
        }

    @property
    def ret(self):
        return self.response

    def set_response(self, code=status.HTTP_200_OK, data={}, errors={}, message="Success"):
        self.response = {
            "code": code,
            "data": data,
            "errors": errors,
            "message": message
        }
        return self.response

    def set_data(self, data):
        self.response["data"] = data
        return self.response

    def set_errors(self, errors):
        self.response["errors"] = errors
        return self.response

    def set_message(self, message):
        self.message = message

    #----------  2XX response code here ----------

    @classmethod
    def get_200_response(cls, data, message="Success"):
        return {
            "code": status.HTTP_200_OK,
            "data": data,
            "errors": {},
            "message": message
        }

    @classmethod
    def get_202_response(self, data, message="Accepted"):
        return {
            "code": status.HTTP_202_ACCEPTED,
            "data": data,
            "errors": {},
            "message": message
        }

    @classmethod
    def get_201_response(cls, data, message="Created Successfully"):
        return {
            "code": status.HTTP_201_CREATED,
            "data": data,
            "errors": {},
            "message": message
        }

    @classmethod
    def get_204_response(cls):
        return status.HTTP_204_NO_CONTENT

    #----------  4XX response code here ----------

    def get_baked_403_response(self, data={}, errors=['Forbidden'], message="Forbidden"):
        return {
            "code": status.HTTP_403_FORBIDDEN,
            "data": data,
            "errors": errors,
            "message": message
        }

    def get_baked_400_response(self, errors, data={}, message="Bad Request"):
        return {
            "code": status.HTTP_400_BAD_REQUEST,
            "data": data,
            "errors": errors,
            "message": message
        }

    @classmethod
    def get_baked_412_response(cls, errors, data={}, message="Precondition Failed"):
        return {
            "code": status.HTTP_412_PRECONDITION_FAILED,
            "data": data,
            "errors": errors,
            "message": message
        }

    @classmethod
    def get_baked_404_response(cls, errors, data={}, message="Bad Request"):
        return {
            "code": status.HTTP_404_NOT_FOUND,
            "data": data,
            "errors": errors,
            "message": message
        }

    def get_404_response(self, errors, data={}, message="Bad Request"):
        return {
            "code": status.HTTP_404_NOT_FOUND,
            "data": data,
            "errors": errors,
            "message": message
        }

    @classmethod
    def get_400_response(cls, errors, data={}, message="Bad Request"):
        return {
            "code": status.HTTP_400_BAD_REQUEST,
            "data": data,
            "errors": errors,
            "message": message
        }

    @classmethod
    def get_401_response(cls, errors, data={}, message="Unauthorized Request"):
        return {
            "code": status.HTTP_401_UNAUTHORIZED,
            "data": data,
            "errors": errors,
            "message": message
        }

    @classmethod
    def get_baked_409_response(cls, errors, data={}, message="Conflict"):
        return {
            "code": status.HTTP_409_CONFLICT,
            "data": data,
            "errors": errors,
            "message": message
        }

    #----------  5XX response code here ----------

    @classmethod
    def get_500_response(cls, data, errors={}, message="Internal Server Error"):
        return {
            "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "data": data,
            "errors": errors,
            "message": message
        }
