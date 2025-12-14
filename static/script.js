// Animated Particles Background
document.addEventListener('DOMContentLoaded', function() {
    createParticles();
    addScrollAnimations();
});

function createParticles() {
    const particlesContainer = document.createElement('div');
    particlesContainer.className = 'particles';
    document.body.appendChild(particlesContainer);
    
    for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 15 + 's';
        particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
        particlesContainer.appendChild(particle);
    }
}

function addScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.feature-card, .scale-item, .about-card').forEach(el => {
        observer.observe(el);
    });
}

// Smooth Number Animation for AQI Value
function animateValue(element, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        element.textContent = Math.floor(progress * (end - start) + start);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Apply animation if AQI value exists
const aqiValueElement = document.getElementById('aqiValue');
if (aqiValueElement) {
    const finalValue = parseInt(aqiValueElement.textContent);
    aqiValueElement.textContent = '0';
    setTimeout(() => {
        animateValue(aqiValueElement, 0, finalValue, 2000);
    }, 300);
}

// Add cursor trail effect
let mouseX = 0, mouseY = 0;
let cursorCircles = [];

for (let i = 0; i < 3; i++) {
    const circle = document.createElement('div');
    circle.style.position = 'fixed';
    circle.style.width = '20px';
    circle.style.height = '20px';
    circle.style.borderRadius = '50%';
    circle.style.pointerEvents = 'none';
    circle.style.zIndex = '9999';
    circle.style.background = `radial-gradient(circle, rgba(88, 166, 255, ${0.3 - i * 0.1}) 0%, transparent 70%)`;
    circle.style.transition = `all ${0.1 + i * 0.05}s ease-out`;
    document.body.appendChild(circle);
    cursorCircles.push(circle);
}

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    
    cursorCircles.forEach((circle, index) => {
        setTimeout(() => {
            circle.style.left = (mouseX - 10) + 'px';
            circle.style.top = (mouseY - 10) + 'px';
        }, index * 50);
    });
});