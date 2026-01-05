import Header from './components/Header';
import Footer from './components/Footer';
import Main from './components/Main';
import Home from './pages/Home';

function App() {
  return (
    <>
      <Header />
      <Main>
        <Home />
      </Main>
      <Footer />
    </>
  );
}

export default App;