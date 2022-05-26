import './style.css'
// const app = document.querySelector<HTMLDivElement>('#app')!

// app.innerHTML = `
//   <h1>Hello Vite!</h1>
//   <a href="https://vitejs.dev/guide/features.html" target="_blank">Documentation</a>
// `

let button = document.querySelector<HTMLButtonElement>('#read-button')
let fileInput = document.querySelector<HTMLInputElement>('#file-input')


button?.addEventListener('click', () => {
	if (fileInput?.files?.length == 0) {
		console.error('Error: No file selected!')
		return
	}

	let file = fileInput?.files[0]
	
	let reader = new FileReader();

	reader.readAsText(file);

	reader.onload = () => {
		console.log(reader.result);
	}
	
	console.log("DONE!")
})