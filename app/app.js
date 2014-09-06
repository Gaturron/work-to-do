angular.module('work-to-do', [
    'ngRoute'
])
    .config(function($routeProvider) {
        $routeProvider

            .when('/', {
                templateUrl : 'views/main.html',
                controller  : 'controllers/mainController.js'
            });
    });