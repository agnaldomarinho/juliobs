$(function() {
    $.ajax('http://uhunt.felix-halim.net/api/ranklist/92440/0/0', {
        success: function(data) {
            data = eval(data);
            $('.username').text(data[0].username);
            $('.problems').text(data[0].ac);
        },
        error: function(data) {
            $('.username').text('error');
            $('.accepted').text('are you using IE?');
        }
    });
});
