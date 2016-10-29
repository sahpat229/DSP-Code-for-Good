'use strict';

var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
	res.render('index', { title: 'Eden II - Login' });
});

router.get('/main', function(req, res, next) {
	res.render('main', { title: 'Main Page' });
};

router.get('/interpret', function(req, res, next) {
	res.render('interpret', { title: 'Interpret Speech', text: dbQueryForInterpretSpeech() });
});

module.exports = router;
