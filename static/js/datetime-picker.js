$(document).ready(function() {
    $('.datetime-picker').flatpickr({
        enableTime: true,
        dateFormat: "Y-m-d\\TH:i:S",
        defaultHour: 0,
        altFormat: "Y-m-d\\TH:i:S",
        allowInput: true,
        time_24hr: true,

    });
    $('.date-picker').flatpickr({
        enableTime: true,
        dateFormat: "Y-m-d",
        altFormat: "Y-m-d",
        allowInput: true,
    });
});
