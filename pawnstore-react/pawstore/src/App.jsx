import Header from './components/Header';
import Footer from './components/Footer';
import Main from './components/Main';
import Home from './pages/Home';
import Catalogo from './pages/Catalogo';
import Contacto from './pages/Contacto';
import productos from './data/productos.json';

function App() {
  return (
    <>
      <Header />

      <Main>
        {/* <Home /> */}
        <Catalogo productos={productos} />
        {/* <Contacto /> */}
      </Main>

      <Footer />
    </>
  );
}

export default App;