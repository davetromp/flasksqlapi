$(function() {
    $('button').click(function() {
    
        function apiIdCall(id) {
            $.ajax({
                url: '/Api',
                data: "id="+id,
                type: 'POST',
                success: function(response) {
                    console.log(response);
                    return response;
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }    
    
        $( "#IDs" ).empty();
        var q = $('#q').val();
        console.log(q);
        $.ajax({
            url: '/Api',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                for(var x = 0; x < response["IDs"].length; x++){
                    var z = response["IDs"][x];
                    $( "#IDs" ).append( "<li>"+z+"<br>"+apiIdCall(z)+"</li>" );
                    console.log(z);
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
