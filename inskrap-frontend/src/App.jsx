import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [country, setCountry] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const response = await axios.post('http://localhost:5000/search', { query, country });
    setResults(response.data);
  };

  return (
    <div className="App">
      <h1>Instagram Business Search</h1>
      <input
        type="text"
        placeholder="Business Category"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <input
        type="text"
        placeholder="Country"
        value={country}
        onChange={(e) => setCountry(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
      <div>
        {results.map((result, index) => (
          <div key={index}>
            <a href={result} target="_blank" rel="noopener noreferrer">{result}</a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
