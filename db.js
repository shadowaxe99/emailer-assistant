const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/email-scheduler', { useNewUrlParser: true, useUnifiedTopology: true })
.then(() => console.log('Database connected successfully'))
.catch(err => console.log(err));

module.exports = mongoose;