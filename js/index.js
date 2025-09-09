// Testimonial slider
const track = document.querySelector('.testimonial-track');
const slides = document.querySelectorAll('.testimonial-slide');
const nextBtn = document.querySelector('.next-btn');
const prevBtn = document.querySelector('.prev-btn');
let currentIndex = 0;

function moveSlider() {
    track.style.transform = `translateX(-${currentIndex * 100}%)`;
}

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % slides.length;
    moveSlider();
});

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    moveSlider();
});

// Auto slide every 5 seconds
setInterval(() => {
    currentIndex = (currentIndex + 1) % slides.length;
    moveSlider();
}, 5000);

// Newsletter form
const newsletterForm = document.querySelector('.newsletter-form');
const newsletterMessage = document.querySelector('.newsletter-message');

newsletterForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = newsletterForm.querySelector('input').value;
    
    // Simulate subscription success
    newsletterMessage.textContent = "Merci pour votre inscription! Vous recevrez bientôt nos actualités.";
    newsletterMessage.style.display = 'block';
    newsletterMessage.style.color = '#fff';
    
    // Reset form
    newsletterForm.reset();
    
    // Hide message after 5 seconds
    setTimeout(() => {
        newsletterMessage.style.display = 'none';
    }, 5000);
});

// Animate on scroll
const animateElements = document.querySelectorAll('.animate-on-scroll');

function checkScroll() {
    animateElements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;
        
        if (elementPosition < screenPosition) {
            element.classList.add('is-visible');
        }
    });
}

// Counter animation for stats
const counters = document.querySelectorAll('.stat-number');
const speed = 200;

function animateCounters() {
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-count');
        const count = +counter.innerText;
        const increment = Math.ceil(target / speed);
        
        if (count < target) {
            counter.innerText = Math.min(count + increment, target);
            setTimeout(() => animateCounters(), 1);
        }
    });
}

// Start counter animation when stats are in view
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

observer.observe(document.querySelector('.hero-stats'));