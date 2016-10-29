var express = require('express');
var router = express.Router();
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "cooper",
    database: "CooperCares"
});

con.connect(function(err){
  if(err){
    console.log('Error connecting to Db');
    return;
  }
  console.log('Connection established');
});

/* Handle requests to database */
router.get('/', function(req, res, next) {
    res.send('hello world!');
});

router.get('/GET/Users', function(req, res, next) {
    con.query('SELECT * FROM Users',function(err,rows){
      if(err) throw err;

      console.log('Data received from Db:\n');
      res.send(rows);
    });
});

router.get('/GET/Children', function(req, res, next) {
    con.query('SELECT * FROM Children',function(err,rows){
      if(err) throw err;

      console.log('Data received from Db:\n');
      res.send(rows);
    });
});

module.exports = router;
