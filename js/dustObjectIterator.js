
/*
dust.js contextual helper that iterates over simple key-value objects (aka dictionaries)
note: the order of iteration through the keys is arbitrary and varies between browsers

USAGE:
    # myContextObject (the object you want to iterate over):
    var myContextObject = {"a": 2, "b": 4, "c": 6};

    # dust.js render call:
    dust.render('myTemplate',
        {
            iter: dustObjectIterator,
            obj: myContextObject
        },
        myCallbackFunction
    );

    # myTemplate.dust:
    {#iter:obj}
        {key}: {value}{~n}
    {/iter}

    # output:
    a: 2
    b: 4
    c: 6
 */

dustObjectIterator = function(chk, ctx, bodies) {
    var obj = ctx.current();
    for (var k in obj) {
        chk = chk.render(bodies.block, ctx.push({key: k, value: obj[k]}));
    }
    return chk;
}