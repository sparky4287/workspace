app.controller('MainController', ['$scope', function($scope) {
    $scope.title = 'Best Sellers in Books';
    $scope.promo = 'You know it\'s good for you...';
    $scope.products =
        [
        	{
        		name: 'The Book of Trees',
        		price: 19,
        		pubdate: new Date('2014','03','08'),
                cover: 'img/the-book-of-trees.jpg',
                likes: 0,
                dislikes: 0
      		},
        	{
                name: 'Program or be Programmed',
                price: 8,
                pubdate: new Date('2013','08','01'),
                cover: 'img/program-or-be-programmed.jpg',
                likes: 0,
                dislikes: 0
            },
            {
        		name: 'Book 1',
        		price: 12,
        		pubdate: new Date('2013','01','09'),
                cover: 'img/the-book-of-trees.jpg',
                likes: 0,
                dislikes: 0
      		},
        	{
                name: 'Book 2',
                price: 21,
                pubdate: new Date('2011','05','12'),
                cover: 'img/program-or-be-programmed.jpg',
                likes: 0,
                dislikes: 0
            }
        ];
    $scope.previews =
        [
            {
                name: 'City',
                thumb: 'http://lorempixel.com/100/100/city',
                description: 'City'
            },
            {
                name: 'Nature',
                thumb: 'http://lorempixel.com/100/100/nature',
                description: 'Nature?'
            },
            {
                name: 'Abstract',
                thumb: 'http://lorempixel.com/100/100/abstract',
                description: 'I don\'t know, but it\'s called \'Abstract\'...'
            },
            {
                name: 'Cats',
                thumb: 'http://lorempixel.com/100/100/cats',
                description: 'Cats and shit'
            },
            {
                name: 'Food',
                thumb: 'http://lorempixel.com/100/100/food',
                description: 'Food'
            },
            {
                name: 'Animals',
                thumb: 'http://lorempixel.com/100/100/animals',
                description: 'Random animals'
            },
            {
                name: 'Business',
                thumb: 'http://lorempixel.com/100/100/business',
                description: 'Ha! Business...'
            },
            {
                name: 'People',
                thumb: 'http://lorempixel.com/100/100/people',
                description: 'People doing stuff for things'
            }
        ];
    $scope.setMaster =
        function(preview) {
            $scope.selected = preview;
        }
    $scope.plusOne = 
        function(index) {
            $scope.products[index].likes += 1;
        };
    $scope.minusOne = 
        function(index) {
            $scope.products[index].dislikes += 1;
        };
}]);