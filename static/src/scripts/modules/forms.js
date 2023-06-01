export function forms() {
    /**
     * Объект данных отправляемых на сервер
     * @type {{phone: string, name: string, comment: string, type: string}}
     */
    const ajaxData = {
        type: '', name: '', phone: '', comment: '',
    }

    /**
     * Валидация телефона
     * @param input
     */
    function validationPhone(input) {
        const value = $(input).val()
        const length = value.length
        if (length !== 18) {
            $(input).addClass('error')
        } else {
            ajaxData.phone = value
            $(input).removeClass('error')
        }
    }

    /**
     * Валидация полей
     * @param inputs
     * @param callback
     */
    function validationInputs(inputs = [], callback = () => {
        console.log('ok')
    }) {
        $.each(inputs, (index, input) => {
            const type = $(input).attr('data-ajaxType')
            const value = $(input).val()
            if (value === '') {
                $(input).addClass('error')
            } else {
                ajaxData[type] = value
                $(input).removeClass('error')
            }
            if (type === 'phone') {
                validationPhone(input)
            }
        })
        const error = $('.error')
        if (error.length === 0) {
            callback()
        }
    }

    /**
     * Отправка ajax запроса
     * @param data
     */
    function sendAjax(data) {
        $.ajax({
            url: '/ajax/',
            method: "POST",
            data: data,
            success: (r) => {
                console.log(r)
            }
        })
    }

    $('.send-btn').on('click', function () {
        const form = $(this).parents('form')
        const inputs = form.find('input')
        ajaxData.type = $(this).attr('data-type')

        validationInputs(inputs, () => {
            const data = JSON.stringify(ajaxData)
            $('input').val('')
            for (const member in ajaxData) delete ajaxData[member];
            sendAjax(data)
        })
    })
}
