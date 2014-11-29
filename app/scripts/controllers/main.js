'use strict';

/**
 * @ngdoc function
 * @name mastermindApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the mastermindApp
 */
angular.module('mastermindApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
