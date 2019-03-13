const express = require('express');
const bodyParser = require("body-parser");

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true}));
app.use(bodyParser.json());




app.get('/get-data', (req, res) => res.send('<h1>Hello World!</h1>'));

app.post('/post-data',(req , res) => {
    var Sensordata = req.body.SensorValue
    console.log(Sensordata);
    
    res.end('Data Recieved')
})

app.listen(port,() => console.log('Listening...'))