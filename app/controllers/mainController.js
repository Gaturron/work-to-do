angular.module('worktodoControllers', [])

    .controller('mainController', ['$scope', 

        function($scope) {
            $scope.message = 'Everyone come and see how good I look!';
            $scope.currentTime = new Date();
        }
    ]);