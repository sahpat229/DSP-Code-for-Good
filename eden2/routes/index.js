'use strict';

var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
	res.render('index', { title: 'Eden II' });
});

router.get('/interpret', function(req, res, next) {
	res.render('interpret', { title: 'Interpret', text: dbQueryForInterpretSpeech() });
});

module.exports = router;
