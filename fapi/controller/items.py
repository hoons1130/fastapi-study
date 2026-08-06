from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.item import ItemCreate, ItemResponse, ItemUpdate
from service.item_service import (
    create_item,
    delete_item,
    get_item,
    get_items,
    update_item,
)


router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.post(
    "",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(
    request: ItemCreate,
    db: Session = Depends(get_db),
):
    return create_item(request, db)


@router.get(
    "",
    response_model=list[ItemResponse],
)
def find_all(
    db: Session = Depends(get_db),
):
    return get_items(db)


@router.get(
    "/{item_id}",
    response_model=ItemResponse,
)
def find_by_id(
    item_id: int,
    db: Session = Depends(get_db),
):
    return get_item(item_id, db)


@router.put(
    "/{item_id}",
    response_model=ItemResponse,
)
def update(
    item_id: int,
    request: ItemUpdate,
    db: Session = Depends(get_db),
):
    return update_item(item_id, request, db)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete(
    item_id: int,
    db: Session = Depends(get_db),
):
    delete_item(item_id, db)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )