
import React from 'react';
import { SpreadsheetProvider } from './context/SpreadsheetContext';
import Table from './components/Table';
import './App.css';

const App = () => {
  return (
    <SpreadsheetProvider>
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-4">Google Sheets Clone</h1>
        <Table />
      </div>
    </SpreadsheetProvider>
  );
};

export default App;
