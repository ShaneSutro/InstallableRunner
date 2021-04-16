const express = require('express');
const app = express();
const path = require('path');
const {spawn} = require('child_process');

app.use(express.static(path.resolve(__dirname, '../dist')))

app.get('/run', (req, res) => {
  console.log("Running Python Script")
  let dataToSend;
  const python = spawn('python3', ['./runner/repository.py', JSON.stringify({'name':'TestRepo', 'url': 'https://github.com/SonicRift/VBTEST'})])
  python.stdout.on('data', data => {
    dataToSend = data.toString();
  })

  python.on('close', code => {
    console.log("Python exited with the code", code);
    console.log("Data:", dataToSend)
    res.send(dataToSend)
  })
})

app.listen(3000);