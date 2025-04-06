import { useState, useEffect } from 'react'
import './App.css'

function App() {

  const [comparisonData, setComparisonData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [ticker, setTicker] = useState("AAPL")
  const [inputTicker, setInputTicker] = useState("AAPL")
  const [shouldFetch, setShouldFetch] = useState(false)

  useEffect(() => {
    if (shouldFetch) {
      fetch(`/compare?ticker=${ticker}`)
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          setComparisonData(data)
          setLoading(false)
          setShouldFetch(false)
        })
        .catch(error => {
          console.error('Error fetching data:', error)
          setComparisonData({ error: `Failed to fetch: ${error.message}` })
          setLoading(false)
          setShouldFetch(false)
        })
    }
  }, [ticker, shouldFetch])

  const handleSubmit = (e) => {
    setShouldFetch(true)
    e.preventDefault()
    setLoading(true)
    setTicker(inputTicker)
  }

  const handleInputChange = (e) => {
    setInputTicker(e.target.value)
  }

  if (loading) return <div>Loading...</div>

  return (
    <>
      <h1>Lorem Ipsum</h1>
      <div>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="ticker"
            value={inputTicker}
            onChange={handleInputChange}
            placeholder="Enter stock ticker..."
          />
          <button type="submit">Search</button>
        </form>
      </div>

      {comparisonData && comparisonData.april_2nd_price && comparisonData.yesterday_price && (
        <div className="comparison-results">
          <h2>Stock Comparison for {ticker} from April 2nd to yesterday</h2>
          <div className="price-card">
            <h3>April 2nd Price</h3>
            <p className="price">${comparisonData.april_2nd_price}</p>
          </div>

          <div className="price-card">
            <h3>Current Price</h3>
            <p className="price">${comparisonData.yesterday_price}</p>
          </div>

          <div className="price-change">
            <h3>Price Change</h3>
            {(() => {
              const priceDiff = comparisonData.yesterday_price - comparisonData.april_2nd_price;
              const percentChange = (priceDiff / comparisonData.april_2nd_price) * 100;
              const isPositive = priceDiff >= 0;

              return (
                <>
                  <p className={isPositive ? "positive" : "negative"}>
                    {isPositive ? "+" : ""}{priceDiff.toFixed(2)} ({isPositive ? "+" : ""}{percentChange.toFixed(2)}%)
                  </p>
                </>
              );
            })()}
          </div>

        </div>
      )}

      {comparisonData && comparisonData.error && (
        <div className="error-message">
          <p>Error: {comparisonData.error}</p>
        </div>
      )}
    </>
  )
}

export default App
