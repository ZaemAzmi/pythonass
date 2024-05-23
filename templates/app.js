$(document).ready(function() {
    $('.company-link').click(function(e) {
        e.preventDefault();
        var companyName = $(this).data('company');
        loadChart(companyName);
    });
});

function loadChart(companyName) {
    $.ajax({
        url: '/visualize',
        type: 'GET',
        data: { 'company': companyName },
        success: function(response) {
            $('#chart-container').html(response); // Insert chart HTML into the container
        },
        error: function(error) {
            console.log(error);
        }
    });
}
