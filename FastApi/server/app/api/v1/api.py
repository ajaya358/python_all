from fastapi import APIRouter
from app.api.v1.endpoints import user, product, auth, file

router = APIRouter(prefix="/api/v1")

router.include_router(auth.router)
router.include_router(user.router)
router.include_router(product.router)
router.include_router(file.router)
