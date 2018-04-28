angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;

        this.messageList = [];
        this.counter  = 2;
        this.newText = "";

        //
        //HERE IS WHERE WE GET FROM THE DB???//
        //
        //
        //

//        this.loadMessages = function(){
//            // Get the messages from the server through the rest api
//            thisCtrl.messageList.push({"id": 1, "text": "Hola Mi Amigo", "author" : "Bob",
//            "like" : 4, "nolike" : 1});
//            thisCtrl.messageList.push({"id": 2, "text": "Hello World", "author": "Joe",
//                "like" : 11, "nolike" : 12});
//
//            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
//        };

        this.loadMessages = function(){
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingApp/msg/gchat/1";
            console.log("reqURL: " + reqURL);
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller

                    /*
                    * Stores the data received from python call. The jsonyfied data
                    */
                    thisCtrl.messageList = response.data.Messages;
                    //thisCtrl.messageList.push({"id": 1, "text": "Hola Mi Amigo", "author" : "Bob", "like" : 4, "nolike"
//                    thisCtrl.messageList.push({"id": 1, "text": "Hola Mi Amigo", "author" : "Bob", "like" : 4, "nolike" : 1});
//                    thisCtrl.messageList.push({"id": 2, "text": "Hello World", "author": "Joe", "like" : 11, "nolike" : 12});

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

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };


        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"id": nextId, "text" : msg, "author" : author, "like" : 0, "nolike" : 0});
            thisCtrl.newText = "";
        };

        this.loadMessages();
}]);

//angular.module('MessagingAppUI').controller('UserDetailController', ['$http', '$log', '$scope', '$location', '$routeParams',
//    function($http, $log, $scope, $location, $routeParams) {
//        // This variable lets you access this controller
//        // from within the callbacks of the $http object
//
//        var thisCtrl = this;
//
//        // This variable hold the information on the part
//        // as read from the REST API
//        var userDetails = {};
//
//        this.loadUserDetails = function(){
//            // Get the target part id from the parameter in the url
//            // using the $routerParams object
//            var userId = $routeParams.user_id;
//
//            // Now create the url with the route to talk with the rest API
//            var reqURL = "http://localhost:5000/MessagingApp/user/" + userId;
//            console.log("reqURL: " + reqURL);
//            // Now issue the http request to the rest API
//            $http.get(reqURL).then(
//                // Success function
//                function (response) {
//                    console.log("data: " + JSON.stringify(response.data));
//                    // assing the part details to the variable in the controller
//
//                    /*
//                    * Stores the data received from python call. The jsonyfied data
//                    */
//                    thisCtrl.userDetails = response.data.User;
//                }, //Error function
//                function (response) {
//                    // This is the error function
//                    // If we get here, some error occurred.
//                    // Verify which was the cause and show an alert.
//                    var status = response.status;
//                    //console.log("Error: " + reqURL);
//                    //alert("Cristo");
//                    if (status == 0) {
//                        alert("No Internet Connection");
//                    }
//                    else if (status == 401) {
//                        alert("Expired Session");
//                    }
//                    else if (status == 403) {
//                        alert("No System Authorization");
//                    }
//                    else if (status == 404) {
//                        alert("Information Not Found");
//                    }
//                    else {
//                        alert("Internal System Error");
//                    }
//                }
//            );
//        };
//
//        this.loadUserDetails();
//}]);
