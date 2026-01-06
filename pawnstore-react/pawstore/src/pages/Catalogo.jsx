import ListaProductos from '../components/ListaProductos';

function Catalogo({ productos }) {
    return (
        <>
            <h2>Catálogo de productos</h2>
            <ListaProductos productos={productos} />
        </>
    );
}

export default Catalogo;