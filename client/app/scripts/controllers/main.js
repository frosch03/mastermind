'use strict';

angular.module('mastermindApp')
    .controller('MainCtrl', function ($scope, $http, Board) {
        $scope.colorMap = ['white', 'red', 'brown', 'indigo', 'yellow', 'green', 'purple'];
        $scope.index = 0;
        $scope.ended = false;
        $scope.won   = false;

        $scope.doMove = function (game) {
            $scope.index = 0;
		        $scope.game = game;
            // if game ended :
            if (game.ttl == 0 || game.state != "running") {
                $scope.ended = true
            };
            // if game ended by winning :
            if (game.ttl != 0 && game.state == "end") {
                $scope.won = true
            };
		        $scope.actualBoard = { 
			          move: [0,0,0,0]
		        };
        }


	      $scope.setActualColor = function(cId) {
		        $scope.actualColor = $scope.colorMap[cId];
            $scope.setColor($scope.index, cId);
	      }

	      $scope.setColor = function(ndx, cId) {
		        $scope.actualBoard.move[ndx] = cId;
            if($scope.index == 3){$scope.index = 0;} else {$scope.index += 1;};
	      }

        
	      Board.get(function(success) {
            $scope.doMove(success);
		        console.log(success);
	      }, function(error) {
		        $scope.game = {
			          state: "running",
			          
		        }
	      });

	      $scope.send = function() {
		        Board.save({request: $scope.actualBoard.move}, function (success) {
                $scope.doMove(success);
            }, function (error) {
                console.log("error: "+error);	
            });
	      }
        $scope.reset = function() {
            Board.delete();
		        $scope.game = {
			          state: "running",
		        };
            $scope.ended = false;
            $scope.won   = false;
        }
    });
