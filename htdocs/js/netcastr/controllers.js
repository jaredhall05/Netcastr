function NetcastrCtrl($scope, $http) {
	$http.get('/netcastr/feeds/').success(function(data) {
		$scope.feeds = data;
	});
}