
/*
dust.js contextual helper that iterates over simple key-value objects (aka dictionaries)
note: the order of iteration through the keys is arbitrary and varies between browsers

USAGE:
    # myContextObject (the object you want to iterate over):
    var myContextObject = {"a": 2, "b": 4, "c": 6};

    # dust.js render call:
    dust.render('myTemplate',
        {obj=myContextObject},
        myCallbackFunction
    );

    # myTemplate.dust:
    {@iterate:obj}
        {key}: {value}{~n}
    {/iterate}

    # output:
    a: 2
    b: 4
    c: 6
 */

dust.helpers.iterate = function(chunk, context, bodies, params) {
    params = params || {};
    var obj = params['on'] || context.current();
    for (var k in obj) {
        chunk = chunk.render(bodies.block, context.push({key: k, value: obj[k]}));
    }
    return chunk;
}