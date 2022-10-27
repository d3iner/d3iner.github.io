jQuery('document').ready(function($){

	var menuBtn = $('.menu-icon'),
		menu = $('.navigation ul');

	menuBtn.click(function() {

		menu.addclass('show');

	});
});

