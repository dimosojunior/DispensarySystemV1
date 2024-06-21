$(document).ready(function(){
    $('#id_line_six, #id_line_seven, #id_line_eight, #id_line_nine,#id_line_ten').hide()
    $('#more-line').click(function(){
        $('#id_line_six').slideToggle(200)
        $('#id_line_seven').slideToggle(200)
       
        $('#id_line_eight').slideToggle(200)
        $('#id_line_nine').slideToggle(200)


        $('#id_line_ten').slideToggle(200)

    });

    

});



// HIZI NI KWA AJILI YA KUHIDE LABELS


// JavaScript for hiding and showing containers
document.addEventListener('DOMContentLoaded', function () {
    // Hide 'after-clicked-container' initially
    // document.getElementById('year-Container').style.display = 'none';

    document.getElementById('id_line_six_label').style.display = 'none';
    
    document.getElementById('id_line_seven_label').style.display = 'none';
    
    document.getElementById('id_line_eight_label').style.display = 'none';
    
    document.getElementById('id_line_nine_label').style.display = 'none';
    
    document.getElementById('id_line_ten_label').style.display = 'none';
    
   
    // Add click event listener to 'semister 1-button'
    document.getElementById('more-line').addEventListener('click', function () {


    

    // Show 'after-clicked-container'
    document.getElementById('id_line_six_label').style.display = 'flex';
    
    document.getElementById('id_line_seven_label').style.display = 'flex';
    
    document.getElementById('id_line_eight_label').style.display = 'flex';
    
    document.getElementById('id_line_nine_label').style.display = 'flex';
    
    document.getElementById('id_line_ten_label').style.display = 'flex';
    

    });






    });





    