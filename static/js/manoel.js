var callBackend = function (url, redirect_func, payload) {
    var jqxhr = $.post(url, JSON.stringify(payload))
        .done(function (data) {
            toastr.success('👍');
            redirect_func(data);
        })
        .fail(function (data) {
            toastr.error('❌ ' + data.responseText);
            console.log("error on " + url);
            console.log(data.status + " " + data.statusText + ": " + data.responseText);
        });
}

var isadmin = false;
var isadminwaiting = true;
$(document).ready(function () {
    var jqxhr = $.post('/roles')
        .done(function (data, status, xhr) {
            isadminwaiting = false;
            try {
                roles = JSON.parse(data);

                var lis = ['limulti', 'limc', 'limt', 'lireset', 'linormal'];
                for (var i = 0; i < roles.length; i++ ) {
                    if (roles[i].Name == "admin") {
                        isadmin = true;
                        for (var j = 0; j < lis.length; j++) {
                            // show all the <li>s
                            $('#'+lis[j]).removeClass('d-none');
                        }
                    }
                    if (roles[i].Name == "default") {
                        $('#limulti').removeClass('d-none');
                        $('#limc').removeClass('d-none');
                        $('#limt').removeClass('d-none');
                        $('#linormal').removeClass('d-none');
                    }
                }
            } catch(e) {
                console.log("response is not json, are we in the login page?");
            }
        })
        .fail(function (data) {
            console.log("error on admin check");
            console.log(data.status + " " + data.statusText + ": " + data.responseText);
        });
});