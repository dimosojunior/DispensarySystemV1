$(document).ready(function () {
    console.log("DATE");

    // Attach the datetime picker to elements with the 'datetimepicker' class
    $(".datepicker").datepicker({
        changeYear: true,
        changeMonth: true,
        dateFormat: 'yy-mm-dd',
        timeFormat: 'HH:mm:ss'
    });
    
    console.log("NEW DATE SELECTED");
});
