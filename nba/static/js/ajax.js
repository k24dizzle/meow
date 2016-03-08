#(document).ready(function(){
	$('#calculate').click(function(){
		$.ajax({
			url: 'code/test.py', 
			success: function(response) {

				$('#calculate').hide();

			}
		});
	});

});