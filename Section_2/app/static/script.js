function toggleDescription(item){
    console.log('Item clicked');
    item.classList.toggle('expanded');
}

function setColours() {
    const assessments = document.querySelectorAll('.assessment-item');

    // Loop through each assessment item
    assessments.forEach(assessment => {

        if (assessment.getAttribute('data-status') == 'True'){
            assessment.classList.add('completed');
            assessment.classList.remove('due');
        } else {
            assessment.classList.add('due');
            assessment.classList.remove('completed');
        }
    });
}




function updateAssessments() {
    // Gets the elements by their ID
    const completedCheckbox = document.getElementById('completed-checkbox');
    const dueCheckbox = document.getElementById('due-checkbox');

    // Selects all elements with the assessment-item class 
    const assessments = document.querySelectorAll('.assessment-item');

    setColours();

    // Loop through each assessment item
    assessments.forEach(assessment => {

        if (assessment.getAttribute('data-status') == 'True'){
            assessment.classList.add('completed');
            assessment.classList.remove('due');
        } else {
            assessment.classList.add('due');
            assessment.classList.remove('completed');
        }

        // Determine the display status based on checkbox states
        if (completedCheckbox.checked && assessment.getAttribute('data-status') == 'True') {
            assessment.style.display = ''; // Show if completed checkbox is checked
        } else if (dueCheckbox.checked && !(assessment.getAttribute('data-status') == 'True')) {
            assessment.style.display = ''; // Show if due checkbox is checked
        } else if (!completedCheckbox.checked && !dueCheckbox.checked) {
            assessment.style.display = ''; // Show all if neither checkbox is checked
        } else {
            assessment.style.display = 'none'; // Hide otherwise
        }
    });
}


window.onload = function() {
    updateAssessments();
}