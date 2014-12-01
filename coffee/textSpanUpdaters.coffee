$(document).on("set-environment-type", (evt, selection) ->
    $(".set-environment-type-name").html(selection)
)