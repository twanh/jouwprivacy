$(function(){
    $('select').material_select();

    // Look if the user wants to search
    // When query is entered
    $('#search').keyup(function(){
        // Category
        category = $("#select_catagory").val();
        // Search Query
        query = $('#search').val();
         $.ajax({
            type: 'POST',
            url: "/i/articles/search/",
            data: {
                'query': query,
                'category': category,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });

    // When btn is clicked
    $('#search_btn').click(function(){
        // Category
        category = $("#select_catagory").val();
        // Search Query
        query = $('#search').val();
         $.ajax({
            type: 'POST',
            url: "/i/articles/search/",
            data: {
                'query': query,
                'category': category,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
    // Category selected
    // Search query
    // ajax

    // $('#search').keyup(function(){
    //     $.ajax({
    //         type: 'POST',
    //         url: "/i/articles/search/",
    //         data: {
    //             'query': $('#search').val(),
    //             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    //         },
    //         success: searchSuccess,
    //         dataType: 'html'
    //     });
});

function searchSuccess(data, textStatus, jqXHR){
    $('#search_results').html(data);
}
