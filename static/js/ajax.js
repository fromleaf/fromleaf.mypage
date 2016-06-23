$(function() {


    // Submit post on submit
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });
    
 // Submit post on submit
    $('#post_gameday_form').on('submit', function(event){
        event.preventDefault();
        console.log("post_gameday_form submitted!")  // sanity check
        update_gameday();
    });

    // AJAX for posting
    function create_post() {
        console.log("create post is working!") // sanity check
        $.ajax({
            url : "create_post/", // the endpoint
            type : "POST", // http method
            data : { the_post : $('#post-text').val() }, // data sent with the post request
            dataType: 'json',
            // handle a successful response
            success : function(json) {
            	$('#post-text').val(''); // remove the value from the input
            	var jsonResponse = eval(json);
            	jsonContent = jsonResponse.content;
            	var json_obj = $.parseJSON(jsonContent);
    
                console.log(json_obj); // log the returned json to the console
                $("#talk").prepend("<li><strong>"+json_obj.text+"</strong> - <em> "+json_obj.author+"</em> - <span> "+json_obj.created+
                    "</span> - <a id='delete-post-"+json_obj.postid+"'>delete me</a></li>");
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
    
    // update gameday(app name: ourhockey) 
    function update_gameday() {
    	$.ajax({
    		url : "updated_gameday/", // the endpoint
            type : "POST", // http method
            data : { post_gameday : $('#post_gameday').val(), 
            	post_gametype : $('#post_gametype').val() }, // data sent with the post request
            dataType: 'json',
            // handle a successful response
            success : function(json) {
            	$('#post_gameday').val(''); // remove the value from the input
            	$('#post_gametype').val('');
            	var jsonResponse = eval(json);
            	jsonContent = jsonResponse.content;
            	var json_obj = $.parseJSON(jsonContent);
                console.log(json_obj); // log the returned json to the console
                $("#gameday").prepend("<li><strong>"+json_obj.game_day+"</strong> - " 
                		+ "<strong>" + json_obj.game_type + "</strong>");
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
    	});
    };

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});