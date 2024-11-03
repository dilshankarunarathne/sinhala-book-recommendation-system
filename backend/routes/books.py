from fastapi import APIRouter, Form

from services.books_service import get_recommendations
from services.similar_books_service import get_similar_books

router = APIRouter(
    prefix="/api/books",
    tags=["books"],
    responses={404: {"description": "The requested uri was not found"}},
)


@router.post("/get-recommendations")
async def get_recommend(
        age: int = Form(...),
        gender: str = Form(...)
):
    return get_recommendations(age, gender)


@router.post("/get-similar")
async def get_similar(
        book_name: str = Form(...)
):
    return get_similar_books(book_name)


@router.post("get-book-info")
async def get_book_info(
        isbn: str = Form(...)
):
    return get_info(isbn)
