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
  } 
  else{
	document.getElementById('roleValue').value = "Patient";
  }
}
