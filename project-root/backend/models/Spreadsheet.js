
const mongoose = require('mongoose');

const SpreadsheetSchema = new mongoose.Schema({
  data: { type: Array, required: true },
});

module.exports = mongoose.model('Spreadsheet', SpreadsheetSchema);
