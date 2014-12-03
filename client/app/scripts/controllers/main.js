'use strict';

/**
 * @ngdoc function
 * @name mastermindApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the mastermindApp
 */
angular.module('mastermindApp')
    .controller('MainCtrl', function ($scope, $http, Board) {
        $scope.colorMap = ['', 'red', 'brown', 'indigo', 'yellow', 'green', 'purple'];
        $scope.index = 0;
        
	      Board.get(function(success) {
		        $scope.game = success;
		        console.log(success);
		        $scope.actualBoard = { 
			          move: [0,0,0,0]
		        };
	      }, function(error) {
		        $scope.game = {
			          state: "running",
			          
		        }
	      });

	      $scope.setActualColor = function(cId) {
		        $scope.actualColor = $scope.colorMap[cId];
            $scope.setColor($scope.index, cId);
	      }

	      $scope.setColor = function(ndx, cId) {
		        $scope.actualBoard.move[ndx] = cId;
            if($scope.index == 3){$scope.index = 0;} else {$scope.index += 1;};
	      }

	      $scope.send = function(combi) {
		        Board.save({request: $scope.actualBoard.move}, function (success) {
                $scope.game = success;
		            $scope.actualBoard = { 
			              move: [0,0,0,0]
		            };
            }, function (error) {
                console.log("error: "+error);	
            });
	      }
    });
