# Google Sheets Clone Web Application

## Project Overview
This project is a web application that mimics the core functionalities of Google Sheets, including spreadsheet interface, mathematical functions, data quality functions, and data entry validation. The project also supports bonus features like saving and loading spreadsheets and data visualization.

## Tech Stack
### Frontend:
- React.js: Component-based UI framework
- Tailwind CSS: Utility-first CSS framework
- React-Table: Grid management
- Formik + Yup: Form validation
- Chart.js: Data visualization (Bonus Feature)

### Backend:
- Node.js with Express.js: API server
- MongoDB: Data storage for Save & Load feature

### Libraries:
- Lodash: Utility functions
- Axios: HTTP requests

## Folder Structure
```
project-root/
│
├─ frontend/                  # React App
│   ├─ components/            # UI Components
│   ├─ context/               # Global State Management
│   ├─ hooks/                 # Custom Hooks
│   ├─ App.js                 # Main App Component
│   └─ index.js               # Entry Point
└─ backend/                   # Node.js Backend
    ├─ models/                # MongoDB Models
    ├─ server.js              # API Server
    └─ .env                   # Environment Variables
```

## Features
### 1. Spreadsheet Interface
- Google Sheets-like UI
- Cell-based grid layout
- Drag functionality for cells
- Add/Delete rows and columns
- Cell formatting (bold, italics, color)

### 2. Mathematical Functions
- SUM
- AVERAGE
- MAX
- MIN
- COUNT

### 3. Data Quality Functions
- TRIM
- UPPER
- LOWER
- REMOVE_DUPLICATES
- FIND_AND_REPLACE

### 4. Data Entry and Validation
- Numeric validation
- Text, Date, and Number data types

### 5. Bonus Features
- Save & Load Spreadsheet
- Data Visualization (Chart.js)
- Data Validation

## Installation and Setup
### Backend
1. Navigate to the backend folder:
```bash
cd backend
```
2. Install dependencies:
```bash
npm install
```
3. Set environment variables in `.env`:
```bash
MONGO_URI=mongodb://localhost:27017/spreadsheet
```
4. Start the backend server:
```bash
node server.js
```

### Frontend
1. Navigate to the frontend folder:
```bash
cd frontend
```
2. Install dependencies:
```bash
npm install
```
3. Start the frontend app:
```bash
npm start
```

## API Endpoints
- **POST /save**: Save spreadsheet data
- **GET /load**: Load spreadsheet data

## Testing

- Use form inputs to test various functions.
- Check Save & Load functionality.
- Try visualization features.

## Conclusion

This project is a simplified version of Google Sheets with core spreadsheet functionality and bonus features. The code is modular, maintainable, and scalable.
