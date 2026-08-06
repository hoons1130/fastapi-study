from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.item import Item
from schemas.item import ItemCreate, ItemUpdate


def create_item(
    request: ItemCreate,
    db: Session,
) -> Item:
    item = Item(
        name=request.name,
        description=request.description,
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def get_items(
    db: Session,
) -> list[Item]:
    statement = select(Item).order_by(Item.id)

    items = db.scalars(statement).all()

    return list(items)


def get_item(
    item_id: int,
    db: Session,
) -> Item:
    item = db.get(Item, item_id)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    return item


def update_item(
    item_id: int,
    request: ItemUpdate,
    db: Session,
) -> Item:
    item = get_item(item_id, db)

    item.name = request.name
    item.description = request.description

    db.commit()
    db.refresh(item)

    return item


def delete_item(
    item_id: int,
    db: Session,
) -> None:
    item = get_item(item_id, db)

    db.delete(item)
    db.commit()