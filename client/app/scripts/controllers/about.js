'use strict';

/**
 * @ngdoc function
 * @name mastermindApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the mastermindApp
 */
angular.module('mastermindApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
