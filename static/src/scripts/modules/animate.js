export function animate() {
    //animate_section
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                $(entry.target).addClass('show')
            } else {
                $(entry.target).removeClass('show')
            }
        })
    })
    const hiddenElements = document.querySelectorAll('.hidden-scroll')
    hiddenElements.forEach((el) => observer.observe(el))
}