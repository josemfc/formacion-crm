var $ = django.jQuery;

$(document).ready(function(){
	// Secciones
	$('.btn-toggle').click(function(e){
		e.preventDefault();

		var $this_toggle = $(this).parent().find('.toggle');
		$(".toggle").not($this_toggle).hide();				// Si se despliega uno, el resto se oculta
		$(".btn-toggle > i").not($(this).children()).removeClass( "fa-caret-down" ).addClass( "fa-caret-right" );

		$this_toggle.slideToggle();
		var $icono = $(this).parent().find('.btn-toggle > .fa');
		$icono.toggleClass('fa-caret-right fa-caret-down');
	});
});

