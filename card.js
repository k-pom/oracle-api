$(document).ready(function(){


   	$(".card").mouseover(function() {
		if($(this).has('img').length ==1){
			$(this).find('img').remove();
		}else{
       		title = $(this).html().replace(/ /g,'');

			div = $("<div style='display:none;padding:3px;border:1px solid #CCC;background:white;position:absolute;float:right;z-index:1000000'><div>");


			div.append("<img src=\"http://l5r.herokuapp.com/cards/" + $(this).html() + ".jpg\" />");

			div.css('left', $(this).position().left + $(this).width());


			div.css('top', $(this).position().top );
			$(this).append(div);
			div.fadeIn();
			div.click(function(){$(this).fadeOut('fast');$(this).remove();});
		}
    });
	$(".card").mouseout(function(){$(this).find('div').fadeOut('fast');$(this).find('div').remove();});
});
