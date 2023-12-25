function clearInput(inputbox_id) {
  var inputField = document.getElementById(inputbox_id);
  //   console.log(inputField);
  inputField.value = "";
}

function showSection(sectionId) {
  // Hide all sections
  // div1 = document.getElementById("PA-whole-div-2");
  // div2 = document.getElementById("PA-whole-div-3");
  document.getElementById("div-out-lgcmf").classList.add("hidden");
  document.getElementById("div-out-mmm").classList.add("hidden");
  // div2.classList.add("hidden");

  // Show the selected section
  document.getElementById(sectionId).classList.remove("hidden");
}

// Add this function to submit the form for the active section
function solveSection(sectionId) {
  showSection(sectionId);  // Make sure the section is visible
  document.getElementById("math-form").submit();  // Submit the form
}