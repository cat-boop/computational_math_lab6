function draw_points(board, points, color) {
    points.forEach((point) => {
        board.create("point", [point.x, point.y], {fixed: true, color: color, label: "point"});
    });
}

function submitForm(board) {
    let x0 = $('#form #x').val(), interval_length = $('#form #length').val();
    $.ajax({
        type: 'POST',
        url: config.host + config.find_similar_endpoint,
        contentType: "application/json",
        data: JSON.stringify({
            odu_id: $('#form #dropdown').val(),
            x0: x0,
            y0: $('#form #y').val(),
            interval_length: interval_length,
            step: $('#form #step').val(),
            eps: $('#form #eps').val()
        }),
        dataType: 'json',
        success: (data) => {
            console.log(data);

            let x_range = data.x_range, y_range = data.y_range;

            if (x_range.length === 0 && y_range.length === 0) {
                showError(document.getElementById("error"), "Извините, рещение содержит сильно большие числа")
            } else {
                showSuccess(document.getElementById("error"))
            }

            let x_delta = Math.abs(x_range[1] / 10), y_delta = Math.abs(y_range[1] / 10)

            board = JXG.JSXGraph.initBoard('jxgbox', {
                boundingbox: [x_range[0] - x_delta, y_range[1] + y_delta, x_range[1] + x_delta, y_range[0] - y_delta],
                axis: true,
                showCopyright: false
            });

            draw_points(board, data.enhanced_eiler, 'green');
            draw_points(board, data.runge_kutta, 'red');
            draw_points(board, data.miln, 'blue');
            draw_points(board, data.perfect_solution, 'purple');

            $('#enhanced_eiler').html(`<p>${data.enhanced_eiler.map(p => `{x=${p.x}, y=${p.y}}`).join("</p><p>")}</p>`)
            $('#runge_kutta').html(`<p>${data.runge_kutta.map(p => `{x=${p.x}, y=${p.y}}`).join("</p><p>")}</p>`)

            if (data.miln.length === 0) {
                $('#miln').text('Для милна количество точек на интервале должно быть >= 4')
            }
            else {
                $('#miln').html(`<p>${data.miln.map(p => `{x=${p.x}, y=${p.y}}`).join("</p><p>")}</p>`)
            }
        }
    });
}


function initDropdownList() {
    $.ajax({
        type: 'GET',
        url: config.host + config.available_functions_endpoint,
        success: (data) => {
            const select = document.getElementById('dropdown');
            data.forEach((item) => {
                console.log(item);
                select.add(new Option(item.string_representation, item.id))
            });
        }
    });
}

$(document).ready(() => {
    let board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox: [-6, 6, 6, -6], axis: true, showCopyright: false});

    initDropdownList();

    $('#form #submit').click((event) => {

        if (validate_form_func()) {
            submitForm(board);
        }

        event.preventDefault();
    });
});