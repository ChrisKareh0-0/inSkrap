import React, { useState } from 'react';
import axios from 'axios';
import Loader from '../Components/Loader'; // Make sure the path is correct

import './CSS/searchPage.css';

function SearchPage() {
  const [keyword, setKeyword] = useState('');
  const [location, setLocation] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true); // Show loader

    try {
      const response = await axios.post('http://127.0.0.1:5001/scrape', {
        keyword,
        location
      });

      setResults(response.data);
    } catch (error) {
      console.error('There was an error with the request:', error);
    } finally {
      setLoading(false); // Hide loader
    }
  };

  return (
    <div className="search-page">
      <h1 className="title">inSkrap</h1>
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
        <button className="searchButton" type="submit">Search</button>
      </form>
      <div>
        {loading && <Loader />}
        {!loading && results.length > 0 && (
          <>
            <h2>Results</h2>
            <p>Total Results: {results.length}</p>
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
                      {result.website ? (
                        <a href={result.website} target="_blank" rel="noopener noreferrer">
                          <button>Website</button>
                        </a>
                      ) : (
                        'N/A'
                      )}
                    </td>
                    <td>{result.phone}</td>
                    <td>{result.stars}</td>
                    <td>{result.reviews}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </>
        )}
      </div>
    </div>
  );
}

export default SearchPage;
