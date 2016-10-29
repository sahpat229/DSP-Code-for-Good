var express = require('express');
var router = express.Router();

/* Handle requests to database */
router.get('/', function(req, res, next) {
    res.send('hello world!');
});

module.exports = router;
