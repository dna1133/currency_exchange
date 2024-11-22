import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import ExchangeRates from '../components/ExchangeRates.jsx'; // Путь к компоненту с курсами валют

const root = ReactDOM.createRoot(document.getElementById('root'));

// Отображение компонента
root.render(
  <React.StrictMode>
    <ExchangeRates />
  </React.StrictMode>
);