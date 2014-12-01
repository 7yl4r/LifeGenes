$.ajax({
    type: "GET",
    url: '../package.json',
    async: false,
    beforeSend: function(x) {
        if(x && x.overrideMimeType) {
            x.overrideMimeType("application/j-son;charset=UTF-8");
        }
    },
    dataType: 'json',
    success: function(data){
        // put package info into browser for debug n stuff
        packageInfo = data;
        console.log(data);
        $('.version-number').html(data.version);
    }
});