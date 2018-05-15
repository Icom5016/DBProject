angular.module('AppChat').controller('DashController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {

        var thisCtrl = this;

        this.counter  = 0;
        this.numberOfLikes = 0;
        this.numberOfDislikes = 0;
        this.orderedHashtagList = [];
        this.date = "";


        this.loadTrendingHashtags = function(){
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingApp/trending_hashtagss";
            console.log("reqURL: " + reqURL);
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));

                    thisCtrl.hashtagList = response.data.Hashtag; //CHECK THIS LINE
                    thisCtrl.counter = thisCtrl.hashtagList.length;
                },
            function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });

            $log.error("Hashtags Loaded: ", JSON.stringify(thisCtrl.hashtagList));
        };

        this.loadMessages();
}]);