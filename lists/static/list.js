$('input').on('keypress', function(e) {
    if (e.which>=70){
        $('.has-error').hide();
        $(document.body).append(e.which);
    }
});
