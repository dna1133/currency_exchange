import { useState, useEffect } from 'react';
import axios from 'axios';

const CurrencyExchangePage = () => {
  const [baseCurrency, setBaseCurrency] = useState('');
  const [targetCurrency, setTargetCurrency] = useState('');
  const [rate, setRate] = useState('');
  const [rates, setRates] = useState([]);
  const [currencies, setCurrencies] = useState([]);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  // Загружаем все курсы и валюты
  useEffect(() => {
    const fetchData = async () => {
      const apiUrl = import.meta.env.VITE_API_URL;
      try {
        const ratesResponse = await axios.get(`${apiUrl}/exchange_rates/`);
        const currenciesResponse = await axios.get(`${apiUrl}/currenсies/`);
        
        setRates(ratesResponse.data);
        setCurrencies(currenciesResponse.data);
      } catch (err) {
        setError('Ошибка при загрузке данных.');
        console.error(err);
      }
    };

    fetchData();
  }, []);


  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column',minHeight: '100vh'  }}>
    <div style={{ width: '80%', display: 'flex', justifyContent: 'space-between', marginBottom: '20px' }}>
      
      {/* Блок отображения курсов обмена */}
      <div style={{ flex: 1, marginRight: '20px' }}>
        <h2>Курсы обмена</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        {success && <p style={{ color: 'green' }}>{success}</p>}

        <table>
          <thead>
            <tr>
              <th>Базовая валюта</th>
              <th>Целевая валюта</th>
              <th>Курс</th>
            </tr>
          </thead>
          <tbody>
            {rates.length > 0 ? (
              rates.map((rate) => (
                <tr key={rate.oid}>
                  <td>{rate.base_currency.code}</td>
                  <td>{rate.target_currency.code}</td>
                  <td>{rate.rate}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="3">Нет данных о курсах обмена.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* Блок отображения списка валют */}
      <div style={{ flex: 1 }}>
        <h2>Список валют</h2>
        <table>
          <thead>
            <tr>
              <th>Код валюты</th>
              <th>Полное имя</th>
              <th>Знак</th>
            </tr>
          </thead>
          <tbody>
            {currencies.length > 0 ? (
              currencies.map((currency) => (
                <tr key={currency.oid}>
                  <td>{currency.code}</td>
                  <td>{currency.fullname}</td>
                  <td>{currency.sign}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="3">Нет доступных валют.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  </div>
  );
};


export default CurrencyExchangePage;
