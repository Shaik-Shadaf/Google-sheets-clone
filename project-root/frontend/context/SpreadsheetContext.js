
import React, { createContext, useState } from 'react';

export const SpreadsheetContext = createContext();

export const SpreadsheetProvider = ({ children }) => {
  const [data, setData] = useState(Array(10).fill(Array(10).fill('')));

  return (
    <SpreadsheetContext.Provider value={{ data, setData }}>
      {children}
    </SpreadsheetContext.Provider>
  );
};
