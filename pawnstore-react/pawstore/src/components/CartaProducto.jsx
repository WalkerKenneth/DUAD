function CartaProducto({ producto }) {
    return (
        <article className="product-card">
            <img src={producto.imagen} alt={producto.nombre} />
            <h3>{producto.nombre}</h3>
            <p>{producto.precio}</p>
        </article>
    );
}

export default CartaProducto;