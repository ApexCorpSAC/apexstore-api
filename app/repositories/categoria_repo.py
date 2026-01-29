from sqlalchemy import select
from app.models.categoria import Categoria


async def get_all(db):
    result = await db.execute(select(Categoria))
    return result.scalars().all()


async def get_by_id(db, categoria_id: int):
    result = await db.execute(
        select(Categoria).where(Categoria.id_categoria == categoria_id)
    )
    return result.scalar_one_or_none()
