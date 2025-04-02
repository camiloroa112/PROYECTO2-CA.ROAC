# controllers/controlador.py
from sqlalchemy.orm import aliased

def obtener_productos(productos, ingredientes, db):
    """Obtiene todos los productos con sus ingredientes de la base de datos."""

    # Crear alias para cada uno de los ingredientes
    ingrediente1 = aliased(ingredientes)
    ingrediente2 = aliased(ingredientes)
    ingrediente3 = aliased(ingredientes)

    # Query para obtener los productos y sus ingredientes con los alias correspondientes
    productos_ingredientes = db.session.query(
        productos.id,
        productos.nombre,
        productos.volumen,
        productos.precio_publico,
        productos.tipo_vaso,
        ingrediente1.nombre.label('ingrediente1'),
        ingrediente2.nombre.label('ingrediente2'),
        ingrediente3.nombre.label('ingrediente3')
    ).join(ingrediente1, productos.ingrediente1_id == ingrediente1.id
    ).join(ingrediente2, productos.ingrediente2_id == ingrediente2.id
    ).join(ingrediente3, productos.ingrediente3_id == ingrediente3.id).all()

    return productos_ingredientes
