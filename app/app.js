angular.module('worktodoApp', [
    'ngRoute',
    'worktodoControllers',
    'worktodoServices'
])
    .config(['$routeProvider', 
        function($routeProvider) {
            $routeProvider

                .when('/', {
                    templateUrl : 'views/main.html',
                    controller  : 'mainController'
                });
    }]);