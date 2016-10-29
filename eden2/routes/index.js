'use strict';
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


router.get('/', function(req, res, next) {
	res.render('index', { title: 'Eden II - Login' });
});

router.get('/kids', function(req, res, next) {
	// var listOfKids = getListOfKids ();
    con.query('SELECT * FROM Children',function(err,rows){
      if(err) throw err;

      console.log('Data received from Db:\n');
      console.log(rows);
      res.render('kids', { title: 'Kids Page', children: rows });
    });

});

router.get('/interpret', function(req, res, next) {
	res.render('interpret', { title: 'Interpret Speech', text: dbQueryForInterpretSpeech() });
});

module.exports = router;
