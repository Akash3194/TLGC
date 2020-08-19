$(".follow").click(function(){
    console.log("sending request")
    console.log($(this).val())

    $.ajax
        ({
        type: "POST",
        url: "/follow/" + $(this).val(),
        dataType: 'json',
        headers: {
            "Authorization": "Basic " + btoa( username + ":" + password)
        },
        data: '',
        });
});