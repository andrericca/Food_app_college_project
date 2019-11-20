$('#btnCritical').on('click', function (event) {
    var url = '/label/' + id + '/critical';
    callBackend(url, nextManualClassification);
});

$('#btnNonCritical').on('click', function (event) {
    var url = '/label/' + id + '/noncritical';
    callBackend(url, nextManualClassification);
});

$('#btnSkipCritical').on('click', function (event) {
    var url = '/label/' + id + '/skip_critical';
    callBackend(url, nextManualClassification);
});

$('#btnNormal').on('click', function (event) {
    var url = '/label/' + id + '/normal';
    callBackend(url, nextManualClassification);
});

var nextManualClassification = function() {
    toastr.info('loading next image');
    setTimeout(function() {
        window.location.reload();
    }, 1000);
}
