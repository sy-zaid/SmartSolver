function clearInput(inputbox_id) {
  var inputField = document.getElementById(inputbox_id);
  //   console.log(inputField);
  inputField.value = "";
}

function showSection(sectionId) {
  // Hide all sections
  document.getElementById("PA-whole-div-2").classList.add("hidden");
  document.getElementById("PA-whole-div-3").classList.add("hidden");

  // Show section whose button is pressed.
  document.getElementById(sectionId).classList.remove("hidden");

  // Set section in the localstorage so when page renders, it can be called back.
  localStorage.setItem("sectionId", `${sectionId}`);
}

document.addEventListener("DOMContentLoaded", function () {
  // Get the last shown section from Local Storage
  var lastShownSection = localStorage.getItem("sectionId");

  // Show the last shown section (or a default if none is stored)
  showSection(lastShownSection || "PA-whole-div-2");
});

function showOnInput() {
  var lastelem = localStorage.getItem("sectionId");
  if (lastelem == "PA-whole-div-3") {
    // Show sec 3
    document.getElementById("PA-whole-div-3").classList.remove("hidden");
    document.getElementById("PA-whole-div-2").classList.add("hidden");
  } else if (lastelem == "PA-whole-div-2") {
    // Show sec 2
    document.getElementById("PA-whole-div-2").classList.remove("hidden");
    document.getElementById("PA-whole-div-3").classList.add("hidden");
  }
}


// ------------------------- ALGEBRA JS ------------------------- //
// var theTotal = 0;
// $('#1').click(function(){
// $('#result').val(1);

function operator(op) {
  op = String(op)
  var op_btn = document.getElementById("operator_poly");
  $("#operator_poly").val('op').change();
}

var res = 0
function focussed(x)
//Function to select one textarea and update the button values in that area only.
{
  if (x == '1') {
    res = document.getElementById("polynomial1")
  }
  else if (x == '2') {
    res = document.getElementById("polynomial2")
  }

  return res

}
function insertTextInInputValue(buttonValueIs) {
  var inputElementIs = res;
  inputElementIs.value = inputElementIs.value + buttonValueIs;
  res = 0;
  inputElementIs = 0;
  $('#res').val(inputElementIs.value);
}


