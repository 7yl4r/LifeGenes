
evts = [
    'set-environment-type'
]
addEvt = (name) ->
    console.log('watching', name, 'event')
    $( document ).on(
        name,
        (event) ->
            console.log( '\t\t\t\t\t\t\t\t\t\t\t\t\t\tEVENT:', event.type ,':',event)
    )

addEvt(evt) for evt in evts
