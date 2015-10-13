function main(){
	$('#students').DataTable({
		autoFill: true,
		responsive: true
	});
}

$(document).on('ready', main);