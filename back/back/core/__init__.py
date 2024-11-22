from .common import Response
from fastapi import HTTPException, status


# HTTP Error
async def raise_http_error(status_code: int, detail: str):
    raise HTTPException(status_code=status_code, detail=detail)


# 404 not found
def raise_not_found(detail: str = "The requested resource was not found."):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


# 400 bad request
def raise_bad_request(detail: str = "Bad request. Please check your input data."):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


# 401 Unauthorized
def raise_unauthorized(detail: str = "Unauthorized access. Please login first."):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


# 403 Forbidden
def raise_forbidden(detail: str = "Forbidden access. You don't have permission."):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


# 500 Internal server error
def raise_internal_server_error(
    detail: str = "Internal server error. Please try again later.",
):
    """500 Internal Server Error를 발생시킨다."""
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail
    )
