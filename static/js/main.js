const user_input = $("#user-input")
const categories_div = $('#replaceable-content')
const endpoint = '/explore/'
const delay_by_in_ms = 200
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            // fade out the categories_div
            /*categories_div.fadeTo('fast', 0).promise().then(() => {
                // replace the HTML contents
                categories_div.html(response['html_from_view'])
                // fade in new contents
                categories_div.fadeTo('fast', 1)
            })*/
            categories_div.html(response['html_from_view'])
        })
}

user_input.on('keyup', function () {
    const request_parameters = {
        q: $(this).val() // value of user_input
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})