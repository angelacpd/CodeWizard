$(document).ready(function(){
    console.log("loaded");

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();

        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });

    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();

        var form = $(this).serialize();

        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(response){
                if (response == "error"){
                    alert("Could not log in.");
                }else{
                    console.log("Logged in as", response);
                    window.location.href = "/"
                }
            }
        });
    });

    $(document).on('click', '#logout-link', function(e){
        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(response){
                if(response == 'success'){
                    window.location.href = 'login';
                }else{
                    alert("Something went wrong.");
                }
            }
        });
    });

    $(document).on('submit', '#post-activity', function(e){
        e.preventDefault();
        form = $(this).serialize();

        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });

    $(document).on('submit', '#settings-form', function(e){
        e.preventDefault();

        var form = $(this).serialize();
        $.ajax({
            url: 'update-settings',
            type: 'POST',
            data: form,
            success: function(response){
                if(response == 'success'){
                    window.location.href = window.location.href;
                }else{
                    alert(response);
                }
            }
        });
    });

});