from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import NotFoundException, BadRequestException, UnauthorizedException
import logging

logger = logging.getLogger(__name__)

async def not_found_exception_handler(request: Request, exc: NotFoundException):
    logger.error(f"404 Error: {exc.message} | Path: {request.url.path}")
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": "Not Found", "message": exc.message}
    )

async def bad_request_exception_handler(request: Request, exc: BadRequestException):
    logger.error(f"400 Error: {exc.message} | Path: {request.url.path}")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": "Bad Request", "message": exc.message}
    )

async def unauthorized_exception_handler(request: Request, exc: UnauthorizedException):
    logger.error(f"401 Error: {exc.message} | Path: {request.url.path}")
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"error": "Unauthorized", "message": exc.message}
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation Error: {exc.errors()} | Path: {request.url.path}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"error": "Validation Error", "details": exc.errors()}
    )

async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"500 Error: {str(exc)} | Path: {request.url.path}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal Server Error", "message": "Something went wrong"}
    )
