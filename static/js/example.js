$(document).ready(function() {
    $('.datetime-picker').flatpickr({
        enableTime: true,
        dateFormat: "Y-m-d\\TH:i:S",
        defaultHour: 0,
        altFormat: "Y-m-d\\TH:i:S",
        allowInput: true,
        time_24hr: true,
    });
	function renderTable(data){
	
		let tableBody='';
		let keys=['_id','flare_id','start','end','link'];
		data.forEach((item)=>{
			tableBody+='<tr>';
			keys.forEach((key)=>{tableBody+='<td>'+item[key]+'</td>'; });
			tableBody+='</tr>';
		});
		$('#flare-list').show();
		 $('#flare-list >tbody').html(tableBody);

	}
	$('#query-btn').on('click',function(e){
		e.preventDefault();
		let start=$('#start').val();
		let end=$('#end').val();
		$('#result').html('Waiting for response...');
		$.ajax({
			url: '/api/flare/query',
			type: "POST",
			data:{'start':start, 'end':end},
			dataType: "json",
			success: function(data) {
				console.log(data);
				renderTable(data);
			}

		});
	});
});


