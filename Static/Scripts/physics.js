function clearInput(inputbox_id) {
  var inputField = document.getElementById(inputbox_id);
  //   console.log(inputField);
  inputField.value = "";
}

function showSection(sectionId) {
  // Hide all sections
  document.getElementById("PC-whole-div-2").classList.add("hidden");
  document.getElementById("PC-whole-div-3").classList.add("hidden");
  document.getElementById("PC-whole-div-4").classList.add("hidden");
  document.getElementById("PC-whole-div-5").classList.add("hidden");
  document.getElementById("PC-whole-div-6").classList.add("hidden");

  // Show section whose button is pressed.
  document.getElementById(sectionId).classList.remove("hidden");

  // Set section in the localstorage so when page renders, it can be called back.
  localStorage.setItem("sectionId", `${sectionId}`);
}

document.addEventListener("DOMContentLoaded", function () {
  // Get the last shown section from Local Storage
  var lastShownSection = localStorage.getItem("sectionId");

  // Show the last shown section (or a default if none is stored)
  showSection(lastShownSection || "PC-whole-div-2");
});

function showOnInput() {
  var lastelem = localStorage.getItem("sectionId");
  // Remove All
  document.getElementById("PC-whole-div-2").classList.add("hidden");
  document.getElementById("PC-whole-div-3").classList.add("hidden");
  document.getElementById("PC-whole-div-4").classList.add("hidden");
  document.getElementById("PC-whole-div-5").classList.add("hidden");
  document.getElementById("PC-whole-div-6").classList.add("hidden");

  if (lastelem == "PC-whole-div-3") {
    // Show sec 3
    document.getElementById("PC-whole-div-3").classList.remove("hidden");
  } else if (lastelem == "PC-whole-div-2") {
    // Show sec 2
    document.getElementById("PC-whole-div-2").classList.remove("hidden");
  } else if (lastelem == "PC-whole-div-4") {
    // Show sec 4
    document.getElementById("PC-whole-div-4").classList.remove("hidden");
  } else if (lastelem == "PC-whole-div-5") {
    // Show sec 5
    document.getElementById("PC-whole-div-5").classList.remove("hidden");
  } else if (lastelem == "PC-whole-div-6") {
    // Show sec 6
    document.getElementById("PC-whole-div-6").classList.remove("hidden");
  }
}
