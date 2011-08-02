function getMap() {
    var mapOptions = {
    credentials: "Ah8zRtYA3Yrct0VBSap6geCLdhsUjRzn_2Zu2lK7IeZVv9gI7724XrkxmdcoCOyL",
    mapTypeId: Microsoft.Maps.MapTypeId.aerial,
    center: new Microsoft.Maps.Location(48.7595529, -122.4882249),
    zoom: 9
    }
    var map = new Microsoft.Maps.Map(document.getElementById("mapDiv"), mapOptions);
    $.getJSON(
        '/f3/json/all',
        function(data) {
           $.each(data, function(key, val) {
                var loc = new Microsoft.Maps.Location(val[1][0], val[1][1]);
                map.entities.push(
                    new Microsoft.Maps.Pushpin(
                        loc,
                        {
                            name: val[0],
                            icon: '/f3/media/images/farmpin.png', width: 24, height: 50, draggable: true
                        }
                    )
                );
           });
        }
    );
}
