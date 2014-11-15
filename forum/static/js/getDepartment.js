$(document).ready(function() {



$('select[name=campus]').change(function(){
    var department_name = $(this).val();
    var request_url = '/get_department/' + department_name + "/";
    $.ajax({
        url: request_url,
        success: function(data) {
            $.each(data[0], function(key, value) {
                $('select[name=course]').append('<option value="' + this.key + '">' + this.value + '</option>');
            });
        }
    })
}
)

});