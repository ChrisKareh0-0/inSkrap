import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

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
  return (
    <div className="home">
      <NeuralNoiseBackground />
      <div className="content">
        <h1>Welcome to inSkrap</h1>
        <p>This is supposed to be the landing page.</p>
        <Link to="/search">
          <button>Go to Search Page</button>
        </Link>
      </div>
    </div>
  );
}

export default App;
