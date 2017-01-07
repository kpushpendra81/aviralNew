// This block is going to use validate and control Invester persional information.


// This function for show/hide specify textbox when occupation is sellected other.
function occupationSpecify(sourceid, targetid) {
	document.getElementById(targetid).style.display = document.getElementById(sourceid).value === 'Other' ? 'block' : 'none'
}


// This function for copy address to permanent address
$('#chkadd').click(() => {
	if ( $('#chkadd').is(":checked")) {
		$("#correspondenceAddress1").val( $('#address1').val() )
		$("#correspondenceAddress2").val( $('#address2').val() )
		$("#correspondenceAddress3").val( $('#address3').val() )
		$("#correspondenceCity").val( $('#city').val() )
		$("#correspondenceState").val( $('#state').val() )
		$("#correspondencePin").val( $('#pin').val() )
	}
	else {
		$("#correspondenceAddress1").val('')
		$("#correspondenceAddress2").val('')
		$("#correspondenceAddress3").val('')
		$("#correspondenceCity").val('')
		$("#correspondenceState").val('')
		$("#correspondencePin").val('')
	}
})


