'use strict';

/**
 * @ngdoc overview
 * @name mastermindApp
 * @description
 * # mastermindApp
 *
 * Main module of the application.
 */
angular
    .module('mastermindApp', [
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'ngTouch',
        'ngMaterial'
    ])
    // .constant('API_END_POINT', 'http://10.0.101.42:8080') // TT-LAN
    .constant('API_END_POINT', 'http://127.0.0.1:8080')
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'views/main.html',
                controller: 'MainCtrl'
            })
            .when('/about', {
                templateUrl: 'views/about.html',
                controller: 'AboutCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    })
    .factory("Board", [ '$resource', 'API_END_POINT', function ($resource, API_END_POINT) {
        return $resource(API_END_POINT + '/:action', { 
        }, {
          'get': {
              method: 'GET',
              params: {
                  action: 'get'
              }
          },
          'save': {
              method: 'POST',
              params: {
                  action: 'move'
              }
          },
          'delete': {
              method: 'GET',
              params: {
                  'action': 'new'
              }
          }

        });
    } 
]);
