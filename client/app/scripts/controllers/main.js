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
