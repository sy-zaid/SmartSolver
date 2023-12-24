function clearInput(inputbox_id) {
  var inputField = document.getElementById(inputbox_id);
  //   console.log(inputField);
  inputField.value = "";
}

function showSection(sectionId) {
  // Hide all sections
  document.getElementById("PA-whole-div-2").classList.add("hidden");
  document.getElementById("PA-whole-div-3").classList.add("hidden");
  

  // Show the selected section
  document.getElementById(sectionId).classList.remove("hidden");
}
