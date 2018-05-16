angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {

        var thisCtrl = this;
        this.counter = 1;
        this.username = "";
        this.password = "";
        this.currentUser = {};

        this.checkLogin = function(){
            var reqURL = "http://localhost:5000/MessagingApp/user";
                console.log("reqURL: " + reqURL);
                // Now issue the http request to the rest API
                $http.get(reqURL).then(
                    // Success function
                    function (response) {
                        console.log("data: " + JSON.stringify(response.data));
                        userList = response.data.User;
//                        username = $scope.username;
                        console.log(username)
                        password = $scope.password;
                        console.log(password)
                        for (var i = 0; i < userList.length; i++) {
                            if (userList[i].username == thisCtrl.username){
                                if (userList[i].password == password) {
                                    thisCtrl.currentUser = userList[i];
                                    $location.url('/msg/gchat/1'); //+ userList[i].person_id)
                                    break;
                                }
                                else {
                                    alert("Incorrect password.");
                                    break;
                                }
                            }
                            alert("Incorrect username.")
                        }
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