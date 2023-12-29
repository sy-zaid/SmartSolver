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
  document.getElementById(sectionId).classList.remove("hidden")
}

function toggleSection(sectionId) {
  var gcfLcmSection = document.getElementById("PA-whole-div-3");
  var meanMedianModeSection = document.getElementById("PA-whole-div-2");

  if (
    gcfLcmSection.style.display === "none" ||
    gcfLcmSection.style.display === ""
  ) {
    // If GCF/LCM section is hidden or not set, show it and hide Mean/Median/Mode section
    gcfLcmSection.style.display = "block";
    meanMedianModeSection.style.display = "none";
  } else {
    // If GCF/LCM section is visible, hide it and show Mean/Median/Mode section
    gcfLcmSection.style.display = "none";
    meanMedianModeSection.style.display = "block";
  }
}

// Add this function to submit the form for the active section
function solveSection(sectionId) {
  showSection(sectionId);  // Make sure the section is visible
  document.getElementById("math-form").submit();  // Submit the form
}