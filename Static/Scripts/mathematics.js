function clearInput(inputbox_id) {
  var inputField = document.getElementById(inputbox_id);
  //   console.log(inputField);
  inputField.value = "";
}

function showSection(sectionId) {
  // Hide all sections
  document.getElementById("PA-whole-div-2").classList.add("hidden");
  document.getElementById("PA-whole-div-3").classList.add("hidden");
  document.getElementById(sectionId).classList.remove("hidden");
  localStorage.setItem("sectionId", `${sectionId}`);
}


document.addEventListener("DOMContentLoaded", function () {
  // Retrieve the last shown section from Local Storage
  var lastShownSection = localStorage.getItem("sectionId");

  // Show the last shown section (or a default if none is stored)
  showSection(lastShownSection || "PA-whole-div-2");
});
function inputStatus() {
  var lastelem = localStorage.getItem("sectionId");
  console.log(lastelem);
  if (lastelem == "PA-whole-div-3") {
    // Show sec 3
    document.getElementById("PA-whole-div-3").classList.remove("hidden");
    document.getElementById("PA-whole-div-3").classList.remove("hidden");
    document.getElementById("PA-whole-div-2").classList.add("hidden");
  } else if (lastelem == "PA-whole-div-2") {
    // Show sec 2
    document.getElementById("PA-whole-div-2").classList.remove("hidden");
    document.getElementById("PA-whole-div-2").classList.remove("hidden");
    document.getElementById("PA-whole-div-3").classList.add("hidden");
  }
}
