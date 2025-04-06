import { useState, useEffect } from 'react'
import './App.css'
import { Routes, Route, Link} from 'react-router-dom'
import Stocks from './pages/stocks/Stocks';
import Home from './pages/home/Home';
function App() {

  const [comparisonData, setComparisonData] = useState(null)
  const [loading, setLoading] = useState(true)
  const ticker = "AAPL"

  useEffect(() => {
    fetch(`http://localhost:8000/compare?ticker=${ticker}`)
      .then(response => response.json())
      .then(data => {
        setComparisonData(data)
        setLoading(false)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
        setLoading(false)
      })
  }, [])

  if (loading) return <div>Loading...</div>

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

      <h2>Stock Comparison for {ticker} from April 2nd to yesterday</h2>
      {comparisonData && (
        <pre>
          <code>
            {JSON.stringify(comparisonData, null, 2)}
          </code>
        </pre>
      )}
      {!loading && !comparisonData && (
        <div>No stock data available or failed to load</div>
      )}
    </>
  )
}

export default App
