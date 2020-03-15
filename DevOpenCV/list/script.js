
var tiers = ['S', 'A', 'B', 'C', 'D', 'E', 'F'];
var tier_colors = ['#ff7f7f', '#ffbf7f', '#ffff7f', '#7fff7f', '#7fbfff', '	#7f7fff', '#ff7fff' ];
var numtiers = tiers.length;

//Open up file containing the dataset, manipulate the number of images and labels, etc

document.addEventListener("DOMContentLoaded", function(event) { 
	const body = document.querySelector("body");
	for (let i = 0; i < numtiers; i++) {
		let row = document.createElement("div");
		row.classList.add("row");
		body.append(row);
		let letter_box = document.createElement("div");
		letter_box.classList.add("column");
		letter_box.classList.add("letter-box");
		letter_box.style.backgroundColor = tier_colors[i];
		letter_box.innerHTML = tiers[i];

		// let text = document.createElement("div");
		// text.innerHTML = tiers[i];
		// text.classList.add("letter-box");

		// letter_box.append(text);
		row.append(letter_box);
	}

	let newboc = document.createElement("div");
	newboc.classList.add("column");
	document.querySelector(".row").append(newboc);


});

