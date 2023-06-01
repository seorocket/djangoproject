import Swiper from 'https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.esm.browser.min.js'

export function sliders() {

    new Swiper('.students-swiper', {
        loop: true,
        slidesPerView: 3,
        spaceBetween: 20,
        breakpoints: {
            // when window width is >= 320px
            320: {
                slidesPerView: 1,
            },
            // when window width is >= 480px
            768: {
                slidesPerView: 2,
            },
            // when window width is >= 640px
            990: {
                slidesPerView: 3,
            }
        }
    });
    new Swiper('.reviews-swiper', {
        loop: true,
        slidesPerView: 2,
        spaceBetween: 20,
        breakpoints: {
            // when window width is >= 320px
            320: {
                slidesPerView: 1,
            },
            // when window width is >= 480px
            768: {
                slidesPerView: 2,
            },

        }
    });

}
