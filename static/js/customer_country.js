let countrySelected = $('#id_primary_country').val();
if(!countrySelected) {
    $('#id_primary_country').css('color', '#aab7c4');
};
$('#id_primary_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});