let fadeElements = document.querySelectorAll('section');

const updateFade = () => {
    for (let element of fadeElements) {
        const bounding = element.getBoundingClientRect();
        const centerY = bounding.top + bounding.height / 2;
        const windowCenterY = window.innerHeight / 2;
        const distanceToCenter = Math.abs(windowCenterY - centerY);
        const maxDistance = window.innerHeight / 2;
        const opacity = 1 - (distanceToCenter / maxDistance);
        element.style.opacity = opacity.toString();
        console.log(element.style.opacity);
    }
}

window.addEventListener('load', updateFade);
window.addEventListener('scroll', updateFade);
window.addEventListener('resize', updateFade);
