var express = require('express');
var router = express.Router();
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "cooper"
});

/* Handle requests to database */
router.get('/', function(req, res, next) {
    res.send('hello world!');
});

module.exports = router;
