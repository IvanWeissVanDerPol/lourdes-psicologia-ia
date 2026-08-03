/*
	Miniport by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$body = $('body'),
		$nav = $('#nav'),
		$top = $('#top'),
		$about = $('#about'),
		$skills = $('#skills'),
		$projects = $('#projects'),
		$contact = $('#contact'),
		$work = $('#work');
		$fadeIn = $('.fadeIn');

	// Breakpoints.
		breakpoints({
			xlarge:  [ '1281px',  '1680px' ],
			large:   [ '981px',   '1280px' ],
			medium:  [ '737px',   '980px'  ],
			small:   [ null,      '736px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Scrolly.
		$('#nav a, .scrolly').scrolly({
			speed: 1000,
			offset: function() { return $nav.height(); }
		});

	// fadeIn.
	if ($fadeIn.length > 0) {

		// Hack: Fix flex min-height on IE.
			if (browser.name == 'ie') {
				$window.on('resize.ie-top-fix', function() {

					var h = $fadeIn.height();

					if (h > $window.height())
						$fadeIn.css('height', 'auto');
					else
						$fadeIn.css('height', h);

				}).trigger('resize.ie-top-fix');
			}

		// Hide element on scroll (> small).
			breakpoints.on('>small', function() {

				$fadeIn.unscrollex();

				$fadeIn.scrollex({
					mode: 'bottom',
					top: '35vh',
					bottom: '-50vh',
					enter: function() {
						$fadeIn.removeClass('hidden');
					},
					leave: function() {
						$fadeIn.addClass('hidden');
					}
				});

			});

		// Hide element on scroll (<= small).
			breakpoints.on('<=small', function() {

				$fadeIn.unscrollex();

				$fadeIn.scrollex({
					mode: 'middle',
					top: '15vh',
					bottom: '-15vh',
					enter: function() {
						$fadeIn.removeClass('hidden');
					},
					leave: function() {
						$fadeIn.addClass('hidden');
					}
				});

		});

	}

})(jQuery);