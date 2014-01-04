$(document).ready(function() {
	$(".pallete a").tooltip();
	var $currentClass = $(".belize-hole");
	var currentColor = "belize-hole";
	$('#turquoise').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("turquoise");
		$currentClass = $(".turquoise");
		currentColor = "turquoise";
	});
	$('#green-sea').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("green-sea");
		$currentClass = $(".green-sea");
		currentColor = "green-sea";
	});
	$('#emerald').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("emerald");
		$currentClass = $(".emerald");
		currentColor = "emerald";
	});
	$('#nephritis').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("nephritis");
		$currentClass = $(".nephritis");
		currentColor = "nephritis";
	});
	$('#peter-river').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("peter-river");
		$currentClass = $(".peter-river");
		currentColor = "peter-river";
	});
	$('#belize-hole').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("belize-hole");
		$currentClass = $(".belize-hole");
		currentColor = "belize-hole";
	});
	$('#amethyst').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("amethyst");
		$currentClass = $(".amethyst");
		currentColor = "amethyst";
	});
	$('#wisteria').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("wisteria");
		$currentClass = $(".wisteria");
		currentColor = "wisteria";
	});
	$('#wet-asphalt').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("wet-asphalt");
		$currentClass = $(".wet-asphalt");
		currentColor = "wet-asphalt";
	});
	$('#midnight-blue').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("midnight-blue");
		$currentClass = $(".midnight-blue");
		currentColor = "midnight-blue";
	});
	$('#sun-flower').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("sun-flower");
		$currentClass = $(".sun-flower");
		currentColor = "sun-flower";
	});
	$('#orange').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("orange");
		$currentClass = $(".orange");
		currentColor = "orange";
	});
	$('#carrot').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("carrot");
		$currentClass = $(".carrot");
		currentColor = "carrot";
	});
	$('#pumpkin').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("pumpkin");
		$currentClass = $(".pumpkin");
		currentColor = "pumpkin";
	});
	$('#alizarin').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("alizarin");
		$currentClass = $(".alizarin");
		currentColor = "alizarin";
	});
	$('#pomegranate').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("pomegranate");
		$currentClass = $(".pomegranate");
		currentColor = "pomegranate";
	});
	$('#concrete').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("concrete");
		$currentClass = $(".concrete");
		currentColor = "concrete";
	});
	$('#asbestos').click(function(){
		$("div").find($currentClass).removeClass(currentColor).addClass("asbestos");
		$currentClass = $(".asbestos");
		currentColor = "asbestos";
	});
});