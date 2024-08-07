import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

import NeuralNoiseBackground from './Components/background';
import SearchPage from './Pages/searchPage';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        {/* <NeuralNoiseBackground /> */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/search" element={<SearchPage />} />
        </Routes>
      </div>
    </Router>
  );
}

function Home() {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate('/search');
  };

  return (
    <div className="home">
    <NeuralNoiseBackground />
    <div className="content">
      <h1>Welcome to inSkrap</h1>
      <p>This is supposed to be the landing page.</p>
      <button className="cssbuttons-io-button" onClick={handleButtonClick}>
        Get started
        <div className="icon">
          <svg
            height="24"
            width="24"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M0 0h24v24H0z" fill="none"></path>
            <path
              d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"
              fill="currentColor"
            ></path>
          </svg>
        </div>
      </button>
    </div>
  </div>
  );
}

export default App;
