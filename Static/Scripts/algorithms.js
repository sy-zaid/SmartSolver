var lastdynid = "dynamic-input-box";
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

  var section_dynamic_input = document.getElementById("input-row-4th");
  var dropdownitem = document.getElementById("algos-dropdown");

  if (
    dropdownitem.value === "FCFS" ||
    dropdownitem.value === "SJF-nonpr" ||
    dropdownitem.value === "SJF"
  ) {
    section_dynamic_input.classList.add("hidden");
  } else if (dropdownitem.value === "RR") {
    section_dynamic_input.classList.remove("hidden");
    var label = document.getElementsByName("label-dynamic-ib");
    label[0].textContent = "Enter Quantum Time";
    var dynamic_input_box = document.getElementById(lastdynid);
    dynamic_input_box.id = "quantum-time";
    dynamic_input_box.name = "quantum-time";
    dynamic_input_box.placeholder = "e.g. 2 secs";
    lastdynid = "quantum-time";
  } else if (dropdownitem.value == "Priority" || dropdownitem.value == "Priority-nonpr" ) {
    section_dynamic_input.classList.remove("hidden");
    var label = document.getElementsByName("label-dynamic-ib");
    label[0].textContent = "Enter Priority";
    var dynamic_input_box = document.getElementById(lastdynid);
    dynamic_input_box.id = "priority";
    dynamic_input_box.name = "priority";
    dynamic_input_box.placeholder = "priority high to low";
    lastdynid = "priority";
  }
}
