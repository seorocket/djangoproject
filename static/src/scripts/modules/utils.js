export function utils() {
    /**
     * Кнопка наверх
     */

    $('.up').click(function () {
        $('html, body').animate({scrollTop: 0}, 0);
        return false;
    });

    $('.reviews-btn').on('click', () => {
        // exampleModal
        $('#exampleModal').modal('show')
    })
    var element = document.querySelectorAll('.phone-input');
    var maskOptions = {
        mask: '+{7} (000) 000-00-00',
        prepare: function (value, maskedInput) {
            if (value === '8' && maskedInput._value.length === 0) {
                return '';
            }
            return value;
        }
    }
    element.forEach((el) => {
        new IMask(el, maskOptions);
    })

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}
