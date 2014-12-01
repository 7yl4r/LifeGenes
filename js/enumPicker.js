
$('.enum-picker').each( function(index){
    console.log($(this));
    var THIS = $(this);
    dust.render('enumPicker',
        {
            iter: dustObjectIterator,
            triggerName: THIS.data("trigger-name"),
            enum: window[THIS.data("enum")]
        },
        function(err, out){
            console.log(THIS);

            THIS.html(out);
            if (err){
                console.log(err);
            }
        }
    );

});



