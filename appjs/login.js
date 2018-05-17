angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {

        var thisCtrl = this;
        this.username = "";
        this.password = "";
        this.currentUser = {};

        this.checkLogin = function(){
            var reqURL = "http://localhost:5000/MessagingApp/login";
                console.log("reqURL: " + reqURL);
                var data = {'username': thisCtrl.username, 'password': thisCtrl.password}
                // Now issue the http request to the rest API
                $http.post(reqURL, data).then(
                    // Success function
                    function (response) {
                        console.log("data: " + JSON.stringify(response.data));
                        thisCtrl.currentUser = JSON.stringify(response.data);
                        thisCtrl.username = "";
                        thisCtrl.password = "";
                        $location.path('/msg/gchat/1')
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

                $log.error("Users Loaded: ", JSON.stringify());
        };
}]);