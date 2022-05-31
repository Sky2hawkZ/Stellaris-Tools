const express = require('express')
var fs = require('fs')
const {spawn} = require('child_process')
const app = express()
const port = 3005

// var uint8arrayToString = function (data) {
// 	return String.fromCharCode.apply(null, data);
// };

app.get('/', (req, res) => {
	let jsonObject;
	const python = spawn('python', ['modifier_parser.py'])
	python.stdout.on('data', (data) => {
		let jsonObject;
		try {
			jsonObject = JSON.parse(data)
		} catch (error) {
			console.error(error)
		}
		res.send(jsonObject)
		// fs.readFile('modifier_groups.json', 'utf8', function(err,data) {
		// 	console.log('Read from generated file...')
		// 	if (err) throw err
		// 	jsonObject = JSON.parse(data)
		// 	res.send(jsonObject)
		// 	try {
		// 		fs.unlinkSync('modifier_groups.json')
		// 	} catch (error) {
		// 		console.error(err)
		// 	}
		// 	console.log("modifier_groups.json file consumed!")
		// })
	})

	python.on('exit', (code) => {
		console.log("Process quit with code : " + code);
	});
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))