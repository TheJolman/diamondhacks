import './App.css'
import { Routes, Route, Link, BrowserRouter } from 'react-router-dom'
import Stocks from './pages/stocks/Stocks';
import Home from './pages/home/Home';
function App() {

  return (
    <>
      <div>
        <nav>
          <Link to="/" className='nav-link'>Home</Link>
          <Link to="/stocks" className='nav-link'>Stocks</Link>
        </nav>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/stocks' element={<Stocks/>}/>
        </Routes>
        
      </div>
    </>
  )
}

export default App
