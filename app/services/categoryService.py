from sqlalchemy.orm import Session
from app.models.categoryModel import Categories


def add_category(category: str,user_id: int, db: Session):
    newCategory = Categories(
        user_id = user_id,
        category = category
    )

    db.add(newCategory)
    db.commit()
    db.refresh(newCategory)
    return newCategory

def get_categories(user_id: int, db: Session):
    return db.query(Categories).filter(Categories.user_id == user_id)