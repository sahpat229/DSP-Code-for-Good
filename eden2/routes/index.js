'use strict';

var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
	res.render('index', { title: 'Eden II - Login' });
});

router.get('/kids', function(req, res, next) {
	// var listOfKids = getListOfKids ();

	res.render('kids', { title: 'Kids Page' });
});

router.get('/interpret', function(req, res, next) {
	res.render('interpret', { title: 'Interpret Speech', text: dbQueryForInterpretSpeech() });
});

module.exports = router;
