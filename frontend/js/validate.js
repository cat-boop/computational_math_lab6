function showError(input, message) {
    const formField = input.parentElement;

    formField.classList.remove('success');
    formField.classList.add('error');

    const error = formField.querySelector('small');
    error.textContent = message;
}

function showSuccess(input) {
    const formField = input.parentElement;

    formField.classList.remove('error');
    formField.classList.add('success');

    const error = formField.querySelector('small');
    error.textContent = '';
}

function validate_form_func() {

    const xElement = document.getElementById("x");
    const yElement = document.getElementById("y");

    let valid = validate_not_empty(xElement);
    valid = validate_not_empty(yElement) && valid;

    const stepElement = document.getElementById("step");
    const epsElement = document.getElementById("eps");
    const lengthElement = document.getElementById("length");

    valid = validate_non_negative(stepElement) && valid;
    valid = validate_non_negative(epsElement) && valid;
    valid = validate_non_negative(lengthElement) && valid;

    if (stepElement.value > lengthElement.value) {
        showError(stepElement, "Шаг на интервале должен быть <= длине интервала");
        valid = false;
    } else {
        showSuccess(stepElement)
    }

    return valid;
}

function validate_not_empty(element) {
    let valid;

    let value = element.value;

    if (isNaN(value) || isNaN(parseFloat(value))) {
        showError(element, "Введите число");
        valid = false;
    } else {
        showSuccess(element);
        valid = true;
    }

    return valid;
}

function validate_non_negative(element) {
    if (!validate_not_empty(element)) return false;

    let valid;

    let value = element.value;

    if (value <= 0) {
        showError(element, "Введите число строго > 0");
        valid = false;
    } else {
        showSuccess(element);
        valid = true;
    }

    return valid;
}