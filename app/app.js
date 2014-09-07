angular.module('worktodoApp', [
    'ngRoute',
    'worktodoControllers'
])
    .config(['$routeProvider', 
        function($routeProvider) {
            $routeProvider

                .when('/', {
                    templateUrl : 'views/main.html',
                    controller  : 'mainController'
                });
    }]);