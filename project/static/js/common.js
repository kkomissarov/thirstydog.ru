$(document).ready(function(){
	
	$('.sandwich-menu').on('click', function() {
		$('.mobile-menu-wrapper').toggle(200);
		$('.sandwich-menu').toggleClass('to-cross');
	});



	//product-slider
	$('.slider-for').slick({
	  slidesToShow: 1,
	  slidesToScroll: 1,
	  arrows: true,
	  fade: true,
	  asNavFor: '.slider-nav'
	});

	$('.slider-nav').slick({
	  slidesToShow: 4,
	  slidesToScroll: 1,
	  asNavFor: '.slider-for',
	  dots: false,
	  centerMode: false,
	  focusOnSelect: true
	});

	//Анимация прокрутки к блоку с категориями
	$('#to_shop_btn').click(function(){
		$("html, body").animate({scrollTop: $('#shop_block').offset().top+"px"});
		return false;
	});


	//Оформление заказа
	$('.order-form').on('submit', function(e){
		e.preventDefault();
		var data = $(this).serialize();

		$.ajax({
			type: 'post',
			url: create_order_url,
			data: data,
			success: function(data){
				$('.order-form').hide(0);
				$('#order-status').text(data);
				$('#order-status').show(0);

				function closeOrderWindow() {
					$.fancybox.close();
					setTimeout(function () {
						$('#order-status').text('Вы уже оформили заказ этого товара. Мы свяжемся с Вами в ближайшее время.');
					}, 300);

				}

				setTimeout(closeOrderWindow, 1000);
			}
		});

	});


});