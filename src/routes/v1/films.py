from fastapi import APIRouter

router = APIRouter(
    prefix='/films',
    tags=['films'],
    responses={404: {'description': 'Not found'}},
)
