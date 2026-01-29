from pydantic import BaseModel


class ImagenProductoBase(BaseModel):
    url_imagen: str
    es_principal: bool = False
    orden: int = 1


class ImagenProductoCreate(ImagenProductoBase):
    id_producto: int


class ImagenProductoOut(ImagenProductoBase):
    id_imagen: int
    id_producto: int

    class Config:
        from_attributes = True
