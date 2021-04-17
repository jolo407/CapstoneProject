$('.player-dropdown').on('change', function(e) {
    e.preventDefault();
    selected_player_id = $('.player-dropdown').val();
    $.ajax({
        type: "POST",
        url: '/ajax/search-detail/' + selected_player_id,
    dataType: 'json',
        success: function (data) {
            $('.details').empty();
            $.each(data, function (key, val) {
                $(".details").append("\<tr>\
                <td>"+val['first_name']+"</td>\
                <td>"+val['last_name']+"</td>\
                <td>"+val['age']+"</td>\
                </tr>\
                ");
            });
        }
    })
});