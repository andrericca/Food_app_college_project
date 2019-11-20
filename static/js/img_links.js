$('.imglink').on('click', function (event) {
    event.preventDefault();
    var id = event.target.id; // get id of the element clicked on
    var an = id.split("_")[1]; // split on `_` and get the second part, which is the AN
    var imgID = "#img_" + an; // build the jQuery selector for the image with this AN
    $(imgID).toggleClass('d-none'); // show or hide the image
});

$('.acklink').on('click', function (event) {
    event.preventDefault();
    var id = event.target.id; // get id of the element clicked on
    var dicomID = id.split("_")[1]; // split on `_` and get the second part, which is the dicom ID
    var url = '/ack/' + dicomID;
    $.post(url)
        .done(function (data) {
            toastr.success('👍 recarregando');
            setTimeout(function() {
                window.location.reload();
            }, 1000);
        })
        .fail(function (data) {
            toastr.error('❌  ' + data.responseText);
            console.log("error on " + url);
            console.log(data.status + " " + data.statusText + ": " + data.responseText);
        });;
});
