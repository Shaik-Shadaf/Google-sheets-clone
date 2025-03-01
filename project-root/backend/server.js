
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const Spreadsheet = require('./models/Spreadsheet');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });

app.post('/save', async (req, res) => {
  const sheet = new Spreadsheet({ data: req.body.data });
  await sheet.save();
  res.send(sheet);
});

app.get('/load', async (req, res) => {
  const sheets = await Spreadsheet.find();
  res.send(sheets);
});

app.listen(5000, () => console.log('Server running on port 5000'));
