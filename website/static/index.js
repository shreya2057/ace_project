$(document).ready(function () {
	// Check for click events on the navbar burger icon
	$(".navbar-burger").click(function () {
		// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
		$(".navbar-burger").toggleClass("is-active");
		$(".navbar-menu").toggleClass("is-active");
	});
});

function changeValue(){
	if (document.getElementById('role').checked) 
  {
      document.getElementById('roleValue').value = "Doctor";
	  document.getElementById('dob').hidden = true
	  document.getElementById('nmc').hidden = false
	  document.getElementById('docField').hidden = false
  } 
  else{
	document.getElementById('roleValue').value = "Patient";
	document.getElementById('dob').hidden = false
	  document.getElementById('nmc').hidden = true
	  document.getElementById('docField').hidden = true
  }
}
