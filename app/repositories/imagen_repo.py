from sqlalchemy import select
from app.models.imagen import ImagenProducto


async def get_by_producto_id(db, producto_id: int):
    result = await db.execute(
        select(ImagenProducto)
        .where(ImagenProducto.id_producto == producto_id)
        .order_by(ImagenProducto.orden)
    )
    return result.scalars().all()
