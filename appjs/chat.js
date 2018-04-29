angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;

        this.messageList = [];
        this.counter  = 0;
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
                    thisCtrl.counter = thisCtrl.messageList.length;
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

        this.loadWhoLiked = function(msg_id){
            // Now create the url with the route to talk with the rest API
            var reqURL1 = "http://localhost:5000/MessagingApp/msg/wholiked/" + msg_id;
            console.log("reqURL: " + reqURL1);
            // Now issue the http request to the rest API
            $http.get(reqURL1).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller

                    /*
                    * Stores the data received from python call. The jsonyfied data
                    */
                    thisCtrl.likesList = response.data.username;
                    thisCtrl.counter = thisCtrl.likesList.length;

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

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.reactList));
        };

        this.loadWhoDisliked = function(msg_id){
            // Now create the url with the route to talk with the rest API
            var reqURL1 = "http://localhost:5000/MessagingApp/msg/whodisliked/" + msg_id;
            console.log("reqURL: " + reqURL1);
            // Now issue the http request to the rest API
            $http.get(reqURL1).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller

                    /*
                    * Stores the data received from python call. The jsonyfied data
                    */
                    thisCtrl.dislikesList = response.data.username;
                    thisCtrl.counter = thisCtrl.dislikesList.length;

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

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.reactList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            thisCtrl.counter += 1;
            thisCtrl.messageList.unshift({"msg_id": thisCtrl.counter, "text" : msg, "username" : author, "likes" : 0, "dislikes" : 0});
            thisCtrl.newText = "";
        };

        this.likeMsg = function(m_id){
            for (var i = 0; i < thisCtrl.messageList.length; i++) {
                if (thisCtrl.messageList[i].msg_id == m_id) {
                    thisCtrl.messageList[i]["likes"] += 1;
                    break;
                }
            }
        };

        this.dislikeMsg = function(m_id){
            for (var i = 0; i < thisCtrl.messageList.length; i++) {
                if (thisCtrl.messageList[i].msg_id == m_id) {
                    thisCtrl.messageList[i]["dislikes"] += 1;
                    break;
                }
            }
        };

        this.loadMessages();
}]);