angular.module('AppChat').controller('NewChatController', ['$http', '$log', '$scope', '$location', '$routeParams', 'currUser',
    function($http, $log, $scope, $location, $routeParams, currUser) {

        var thisCtrl = this;
        this.currentUser = currUser.getUser();
        this.contacts = [];

        this.loadContacts = function() {
        var reqURL = "http://localhost:5000/MessagingApp/contactlist/owner/" + thisCtrl.currentUser.user_id;
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
                    thisCtrl.contacts = response.data.Contacts;
                    console.log(thisCtrl.contacts);
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

                }
                else {
                    alert("Error interno del sistema.");
                }
            });

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.newChat = function(gchat_name) {
            var reqURL = "http://localhost:5000/MessagingApp/gchat";
                console.log("reqURL: " + reqURL);
                var data = {'gchat_name': gchat_name, 'person_id': thisCtrl.currentUser.user_id};
                console.log(data);
                // Now issue the http request to the rest API
                $http.post(reqURL, data).then(
                    // Success function
                    function (response) {
                        console.log("data: " + JSON.stringify(response.data));
                        var gchat_id = response.data.GroupChat.gchat_id;

                        for (var i = 0; i < thisCtrl.contacts.length; i++) {
                            if ($scope.members[thisCtrl.contacts[i]] == true) {
                                $scope.addMember(gchat_id, thisCtrl.contacts[i].user_id);
                            }
                        }
                        $location.path('/user/gchats');
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

        $scope.members = {};

        $scope.addMember = function(gchat_id, person_id) {
            var reqURL = "http://localhost:5000/MessagingApp/gchat/members/" + gchat_id;
                console.log("reqURL: " + reqURL);
                var data = {'gchat_id': gchat_id, 'person_id': person_id};
                console.log(data);
                // Now issue the http request to the rest API
                $http.post(reqURL, data).then(
                    // Success function
                    function (response) {
                        console.log("data: " + JSON.stringify(response.data));
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

        this.showChats = function() {
            $location.path('/user/gchats');
        };

        this.logout = function() {
            currUser.deleteUser();
            localStorage.removeItem('currentChat');
            $location.path('/login')
        };

        this.loadContacts();

}]);