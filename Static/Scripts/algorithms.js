function toggleBox() {
  /* Creating function for toggling the 4th input box for algorithms which require more than 3 inputs (e.g. RR requires QT)
    Below are the details for it.
    - FCFS - stays same
    - SJF Preemptive - stays same
    - SJF Non-Preemptive - stays same
    - Round-Robin - changes
    - Priority Preemptive - changes
    - Priority Non-Preemptive - changes
   */

  var section_dynamic_input= document.getElementById("dynamic-input-box");
  var dropdownitem = document.getElementById("algos-dropdown");

  if (
    dropdownitem.value === "FCFS" ||
    dropdownitem.value === "SJF-nonpr" ||
    dropdownitem.value === "SJF"
  ) {
    section_dynamic_input.classList.add("hidden")
  }

  else if (dropdownitem.value === "RR"){

  }
}
