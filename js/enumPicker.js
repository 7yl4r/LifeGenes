
$('.enum-picker').each( function(index){
    var THIS = $(this);
    dust.render('enumPicker',
        {
            triggerName: THIS.data("trigger-name"),
            settingsObj: window[THIS.data("settings-obj")]
        },
        function(err, out){
            THIS.html(out);
            if (err){
                console.log(err);
            }
        }
    );

});



