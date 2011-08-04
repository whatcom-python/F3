$(function ()
    $("#foods").change(
        function() {
         window.location.href = "/f3/food/" + $("#foods").val();
        }
    )
);

$(function ()
    $("#farms").change(
        function() {
         window.location.href = "/f3/farm/" + $("#farms").val();
        }
    )
);