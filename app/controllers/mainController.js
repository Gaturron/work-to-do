angular.module('worktodoControllers', [])

    .controller('mainController', ['$scope', 'Project',

        function($scope, Project) {

            $scope.message = Project.query();
            $scope.currentTime = new Date();
        }
    ]);