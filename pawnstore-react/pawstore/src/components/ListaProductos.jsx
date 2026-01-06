import CartaProducto from './CartaProducto';

function ListaProductos({ productos }) {
    return (
        <div className="product-list">
            {productos.map(producto => (
                <CartaProducto key={producto.id} producto={producto} />
            ))}
        </div>
    );
}

export default ListaProductos;