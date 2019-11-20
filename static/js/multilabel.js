$('#normalSwitch').change(function() {
    console.log('a');
    var buttons = $('[data-toggle="buttons"] .btn');
    if (this.checked) {
        // disable all the buttons
        buttons.addClass('disabled btn-light');
        buttons.removeClass('btn-primary active');
        buttons.find('[type=checkbox]').prop('checked',false);
    } else {
        // enable all the buttons
        buttons.removeClass('disabled');
    }
});

// based on https://www.codeply.com/go/IeuO1fPf7H
$('[data-toggle="buttons"] .btn').on('click', function () {
    // if it's disabled do nothing
    if ($(this).hasClass('disabled')) {
        return false;
    }

    // toggle style
    $(this).toggleClass('btn-primary btn-light active');

    // toggle checkbox
    var $chk = $(this).find('[type=checkbox]');
    $chk.prop('checked',!$chk.prop('checked'));

    return false;
});