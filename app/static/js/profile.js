

const postes = document.querySelectorAll('.gallery-item');

postes.forEach(post => {
	post.addEventListener('click', () => {
		//Get original image URL
		const imgUrl = post.firstElementChild.src.split("?")[0];
		//Open image in new tab
		window.open(imgUrl, '_blank');
	});
});
