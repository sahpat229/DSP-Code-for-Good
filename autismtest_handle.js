var PythonShell = require('python-shell');
var pyshell = new PythonShell('autismtest.py');

// sends a message to the Python script via stdin
//Get wavefile, trainfile
pyshell.send('test.wav', 'train.txt');

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});

// end the input stream and allow the process to exit
pyshell.end(function (err) {
  if (err) throw err;
  console.log('finished');
});