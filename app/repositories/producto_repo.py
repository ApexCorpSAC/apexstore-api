from sqlalchemy import select
from sqlalchemy.orm import joinedload
from app.models.producto import Producto


async def get_all(db):
    stmt = (
        select(Producto)
        .options(
            joinedload(Producto.categoria),
            joinedload(Producto.imagenes),
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_by_id(db, producto_id: int):
    stmt = (
        select(Producto)
        .where(Producto.id_producto == producto_id)
        .options(
            joinedload(Producto.categoria),
            joinedload(Producto.imagenes),
        )
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()
