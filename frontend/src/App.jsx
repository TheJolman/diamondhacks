import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [stockData, setStockData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(response => response.json())
      .then(data => {
        setStockData(data)
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
      <h2>Stock Data</h2>
      {stockData && (
        <pre>
          <code>
            {JSON.stringify(stockData, null, 2)}
          </code>
        </pre>
      )}
      {!loading && !stockData && (
        <div>No stock data available or failed to load</div>
      )}
    </>
  )
}

export default App
