function toggleEmploymentDetails() {
    let employeeYes = document.getElementById('employeeYes');
    let employmentDetails = document.getElementById('employmentDetails');
    if (employeeYes.checked) {
        employmentDetails.style.display = 'block';
    } else {
        employmentDetails.style.display = 'none';
    }
}

document.getElementById('employeeYes').addEventListener('change', toggleEmploymentDetails);
document.getElementById('employeeNo').addEventListener('change', toggleEmploymentDetails);

toggleEmploymentDetails();