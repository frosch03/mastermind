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
		$scope.actualColor = cId;
	}
	$scope.setColor = function(ndx) {
		$scope.actualBoard.move[ndx] = $scope.actualColor;
	}

	$scope.send = function() {
		$scope.game.board.push($scope.actualBoard);
		$scope.actualBoard = { 
			move: [0,0,0,0]
		};
		return;
		Board.move({ request: "1234" 
		}, function (error) {
            console.log("blub");	
        }, function (success) {
            console.log(success);	
        });
	//	Board.move({ request: "1234" }, function(success) {
	//		console.log(success);
	//	});

	}
	
  });
