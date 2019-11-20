$(document).ready(function () {
    $("#pwchangeform").submit(function (e) {
        var p1 = $('#password').val();
        var p2 = $('#password_again').val();

        if (p1 != p2 || p1 == "" || p2 == "") {
            toastr.error("Passwords are different.");
            e.preventDefault(e);
            return
        }
    });
});