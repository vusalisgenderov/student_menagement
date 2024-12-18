from fastapi import HTTPException,status

class DetailHTTPException(HTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "server error"
    def __init__(self):
        super().__init__(status_code=self.STATUS_CODE,detail=self.DETAIL)
    
class UserNottFoundException(DetailHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "user is not found"

class StudentNotFoundException(DetailHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "student is not found"

class CourseNotFoundException(DetailHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "course is not found"

class UserIsExists(DetailHTTPException):
    STATUS_CODE=status.HTTP_400_BAD_REQUEST
    DETAIL = "User is exists"


class StudentIsExists(DetailHTTPException):
    STATUS_CODE=status.HTTP_400_BAD_REQUEST
    DETAIL = "student is exists"

class CourseIsExists(DetailHTTPException):
    STATUS_CODE=status.HTTP_400_BAD_REQUEST
    DETAIL = "course is exists"

class Unauthorized(DetailHTTPException):
    STATUS_CODE=401
    DETAIL = "permission denied"