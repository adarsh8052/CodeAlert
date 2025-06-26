// This script toggles visibility of 'eligibility' and 'required_qualification_and_skills' fields in the Django admin based on the selected category.
document.addEventListener('DOMContentLoaded', function() {
    function toggleFields() {
        var category = document.getElementById('id_category');
        var reqQual = document.querySelector('.form-row.field-required_qualification_and_skills');
        var eligibility = document.querySelector('.form-row.field-eligibility');
        if (!category || !reqQual || !eligibility) return;
        if (category.value === 'IT') {
            reqQual.style.display = '';
            eligibility.style.display = 'none';
        } else if (category.value === 'GOVT') {
            reqQual.style.display = 'none';
            eligibility.style.display = '';
        } else {
            reqQual.style.display = '';
            eligibility.style.display = 'none';
        }
    }
    var category = document.getElementById('id_category');
    if (category) {
        category.addEventListener('change', toggleFields);
        toggleFields();
    }
}); 