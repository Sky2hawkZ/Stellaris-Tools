const express = require('express')
var fs = require('fs')
const {spawn} = require('child_process')
const app = express()
const port = 3005

app.get('/', (req, res) => {
	let jsonObject;
	const python = spawn('python', ['modifier_parser.py'])
	python.stdout.on('data', function () {
		console.log('Read from generated file...')
		fs.readFile('modifier_groups.json', 'utf8', function(err,data) {
			if (err) throw err
			jsonObject = JSON.parse(data)
		})
	})
	python.on('close', (code) => {
		console.log(`child process close all stdio with code ${code}`)
		res.send(jsonObject)
	})
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))