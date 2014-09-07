angular.module('worktodoServices',  [
    'ngResource'
])
    .factory('Project', ['$resource',

        function($resource){
            return $resource('project/', {}, {
                query: {method:'GET', isArray:true}
            });
        }
    ]);