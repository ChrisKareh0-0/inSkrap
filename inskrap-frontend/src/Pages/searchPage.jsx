import React, { useState } from 'react';
import axios from 'axios';

import './CSS/searchPage.css';

function SearchPage() {
  const [keyword, setKeyword] = useState('');
  const [location, setLocation] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:5000/scrape', {
        keyword,
        location
      });

      setResults(response.data);
    } catch (error) {
      console.error('There was an error with the request:', error);
    }
  };



  return (
    <div className="search-page">
      <h1>Google Maps Scraper</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Keyword:</label>
          <input
            type="text"
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Location:</label>
          <input
            type="text"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            required
          />
        </div>
        <button type="submit">Search</button>
      </form>
      <div>
        <h2>Results</h2>
        <p>Total Results: {results.length}</p>
        {results.length > 0 && (
          <div>
            
            <table>
              <thead>
                <tr>
                  <th>Title</th>
                  <th>Link</th>
                  <th>Website</th>
                  <th>Phone</th>
                  <th>Stars</th>
                  <th>Reviews</th>
                </tr>
              </thead>
              <tbody>
                {results.map((result, index) => (
                  <tr key={index}>
                    <td>{result.title}</td>
                    <td>
                      <a href={result.link} target="_blank" rel="noopener noreferrer">
                        <button>Map Link</button>
                      </a>
                    </td>
                    <td>
                      <a href={result.website} target="_blank" rel="noopener noreferrer">
                        <button>Website</button>
                      </a>
                    </td>
                    <td>{result.phone}</td>
                    <td>{result.stars}</td>
                    <td>{result.reviews}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default SearchPage;
