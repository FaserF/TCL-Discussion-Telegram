import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import FlashingGuide from './pages/FlashingGuide';
import FAQ from './pages/FAQ';
import Contribute from './pages/Contribute';
import './index.css';

const App = () => {
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'dark');

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => prev === 'dark' ? 'light' : 'dark');
  };

  return (
    <Router>
      <div className="bg-white dark:bg-tcl-dark text-gray-900 dark:text-white min-h-screen transition-colors duration-300">
        <Navbar theme={theme} toggleTheme={toggleTheme} />
        <Routes>
          <Route path="/" element={<Home theme={theme} />} />
          <Route path="/guides" element={<FlashingGuide />} />
          <Route path="/faq" element={<FAQ theme={theme} />} />
          <Route path="/contribute" element={<Contribute />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
