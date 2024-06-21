$(document).ready(function(){
    $('#div_id_line_six, #div_id_line_six_description, #div_id_line_six_quantity, #div_id_line_six_unit_price, #div_id_line_six_total_price,#div_id_line_seven, #div_id_line_seven_description, #div_id_line_seven_quantity, #div_id_line_seven_unit_price, #div_id_line_seven_total_price,#div_id_line_eight, #div_id_line_eight_description, #div_id_line_eight_quantity, #div_id_line_eight_unit_price, #div_id_line_eight_total_price,#div_id_line_nine, #div_id_line_nine_description, #div_id_line_nine_quantity, #div_id_line_nine_unit_price, #div_id_line_nine_total_price,#div_id_line_ten, #div_id_line_ten_description, #div_id_line_ten_quantity, #div_id_line_ten_unit_price, #div_id_line_ten_total_price').hide()
    $('#more-line').click(function(){
        $('#div_id_line_six, #div_id_line_six_description, #div_id_line_six_quantity, #div_id_line_six_unit_price, #div_id_line_six_total_price').slideToggle(200)
        $('#div_id_line_seven, #div_id_line_seven_description, #div_id_line_seven_quantity, #div_id_line_seven_unit_price, #div_id_line_seven_total_price').slideToggle(200)
       
        $('#div_id_line_eight, #div_id_line_eight_description, #div_id_line_eight_quantity, #div_id_line_eight_unit_price, #div_id_line_eight_total_price').slideToggle(200)
        $('#div_id_line_nine, #div_id_line_nine_description, #div_id_line_nine_quantity, #div_id_line_nine_unit_price, #div_id_line_nine_total_price').slideToggle(200)


        $('#div_id_line_ten, #div_id_line_ten_description, #div_id_line_ten_quantity, #div_id_line_ten_unit_price, #div_id_line_ten_total_price').slideToggle(200)

    });

    $('#div_id_line_one_quantity, #div_id_line_one_unit_price, #div_id_line_two_quantity, #div_id_line_two_unit_price, #div_id_line_three_quantity, #div_id_line_three_unit_price, #div_id_line_four_quantity, #div_id_line_four_unit_price, #div_id_line_five_quantity, #div_id_line_five_unit_price, #div_id_line_six_quantity, #div_id_line_six_unit_price, #div_id_line_seven_quantity, #div_id_line_seven_unit_price, #div_id_line_eight_quantity, #div_id_line_eight_unit_price #div_id_line_nine_quantity, #div_id_line_nine_unit_price, #div_id_line_ten_quantity, #div_id_line_ten_unit_price').keyup(function(){
        var line_one_quantity_text = $('#div_id_line_one_quantity').val();
        var line_one_unit_price_text = $('#div_id_line_one_unit_price').val();
        var line_one_total = line_one_quantity_text * line_one_unit_price_text
    
        var line_two_quantity_text = $('#div_id_line_two_quantity').val();
        var line_two_unit_price_text = $('#div_id_line_two_unit_price').val();
        var line_two_total = line_two_quantity_text * line_two_unit_price_text
    
        var line_three_quantity_text = $('#div_id_line_three_quantity').val();
        var line_three_unit_price_text = $('#div_id_line_three_unit_price').val();
        var line_three_total = line_three_quantity_text * line_three_unit_price_text
        
        var line_four_quantity_text = $('#div_id_line_four_quantity').val();
        var line_four_unit_price_text = $('#div_id_line_four_unit_price').val();
        var line_four_total = line_four_quantity_text * line_four_unit_price_text
    
        var line_five_quantity_text = $('#div_id_line_five_quantity').val();
        var line_five_unit_price_text = $('#div_id_line_five_unit_price').val();
        var line_five_total = line_five_quantity_text * line_five_unit_price_text
    
        var line_six_quantity_text = $('#div_id_line_six_quantity').val();
        var line_six_unit_price_text = $('#div_id_line_six_unit_price').val();
        var line_six_total = line_six_quantity_text * line_six_unit_price_text
    
        var line_seven_quantity_text = $('#div_id_line_seven_quantity').val();
        var line_seven_unit_price_text = $('#div_id_line_seven_unit_price').val();
        var line_seven_total = line_seven_quantity_text * line_seven_unit_price_text
    
        var line_eight_quantity_text = $('#div_id_line_eight_quantity').val();
        var line_eight_unit_price_text = $('#div_id_line_eight_unit_price').val();
        var line_eight_total = line_eight_quantity_text * line_eight_unit_price_text
    
        var line_nine_quantity_text = $('#div_id_line_nine_quantity').val();
        var line_nine_unit_price_text = $('#div_id_line_nine_unit_price').val();
        var line_nine_total = line_nine_quantity_text * line_nine_unit_price_text
    
        var line_ten_quantity_text = $('#div_id_line_ten_quantity').val();
        var line_ten_unit_price_text = $('#div_id_line_ten_unit_price').val();
        var line_ten_total = line_ten_quantity_text * line_ten_unit_price_text
    
        var total = line_one_total + line_two_total + line_three_total + line_four_total + line_five_total+ line_six_total + line_seven_total + line_eight_total + line_nine_total + line_ten_total
    
        $('#div_id_line_one_total_price').val(line_one_total);
        $('#div_id_line_two_total_price').val(line_two_total);
        $('#div_id_line_three_total_price').val(line_three_total);
        $('#div_id_line_four_total_price').val(line_four_total);
        $('#div_id_line_five_total_price').val(line_five_total);
        $('#div_id_line_six_total_price').val(line_six_total);
        $('#div_id_line_seven_total_price').val(line_seven_total);
        $('#div_id_line_eight_total_price').val(line_eight_total);
        $('#div_id_line_nine_total_price').val(line_nine_total);
        $('#div_id_line_ten_total_price').val(line_ten_total);
        $('#div_id_total').val(total);
    });

});








// HIZI NI KWA AJILI YA KUHIDE LABELS


// JavaScript for hiding and showing containers
document.addEventListener('DOMContentLoaded', function () {
    // Hide 'after-clicked-container' initially
    // document.getElementById('year-Container').style.display = 'none';

    document.getElementById('id_line_six_label').style.display = 'none';
    document.getElementById('id_line_six_description_label').style.display = 'none';
    document.getElementById('id_line_six_quantity_label').style.display = 'none';
    document.getElementById('id_line_six_unit_price_label').style.display = 'none';
    document.getElementById('id_line_six_total_price_label').style.display = 'none';

    document.getElementById('id_line_seven_label').style.display = 'none';
    document.getElementById('id_line_seven_description_label').style.display = 'none';
    document.getElementById('id_line_seven_quantity_label').style.display = 'none';
    document.getElementById('id_line_seven_unit_price_label').style.display = 'none';
    document.getElementById('id_line_seven_total_price_label').style.display = 'none';

    document.getElementById('id_line_eight_label').style.display = 'none';
    document.getElementById('id_line_eight_description_label').style.display = 'none';
    document.getElementById('id_line_eight_quantity_label').style.display = 'none';
    document.getElementById('id_line_eight_unit_price_label').style.display = 'none';
    document.getElementById('id_line_eight_total_price_label').style.display = 'none';

    document.getElementById('id_line_nine_label').style.display = 'none';
    document.getElementById('id_line_nine_description_label').style.display = 'none';
    document.getElementById('id_line_nine_quantity_label').style.display = 'none';
    document.getElementById('id_line_nine_unit_price_label').style.display = 'none';
    document.getElementById('id_line_nine_total_price_label').style.display = 'none';

    document.getElementById('id_line_ten_label').style.display = 'none';
    document.getElementById('id_line_ten_description_label').style.display = 'none';
    document.getElementById('id_line_ten_quantity_label').style.display = 'none';
    document.getElementById('id_line_ten_unit_price_label').style.display = 'none';
    document.getElementById('id_line_ten_total_price_label').style.display = 'none';

   
    // Add click event listener to 'semister 1-button'
    document.getElementById('more-line').addEventListener('click', function () {


    

    // Show 'after-clicked-container'
    document.getElementById('id_line_six_label').style.display = 'flex';
    document.getElementById('id_line_six_description_label').style.display = 'flex';
    document.getElementById('id_line_six_quantity_label').style.display = 'flex';
    document.getElementById('id_line_six_unit_price_label').style.display = 'flex';
    document.getElementById('id_line_six_total_price_label').style.display = 'flex';

    document.getElementById('id_line_seven_label').style.display = 'flex';
    document.getElementById('id_line_seven_description_label').style.display = 'flex';
    document.getElementById('id_line_seven_quantity_label').style.display = 'flex';
    document.getElementById('id_line_seven_unit_price_label').style.display = 'flex';
    document.getElementById('id_line_seven_total_price_label').style.display = 'flex';

    document.getElementById('id_line_eight_label').style.display = 'flex';
    document.getElementById('id_line_eight_description_label').style.display = 'flex';
    document.getElementById('id_line_eight_quantity_label').style.display = 'flex';
    document.getElementById('id_line_eight_unit_price_label').style.display = 'flex';
    document.getElementById('id_line_eight_total_price_label').style.display = 'flex';

    document.getElementById('id_line_nine_label').style.display = 'flex';
    document.getElementById('id_line_nine_description_label').style.display = 'flex';
    document.getElementById('id_line_nine_quantity_label').style.display = 'flex';
    document.getElementById('id_line_nine_unit_price_label').style.display = 'flex';
    document.getElementById('id_line_nine_total_price_label').style.display = 'flex';

    document.getElementById('id_line_ten_label').style.display = 'flex';
    document.getElementById('id_line_ten_description_label').style.display = 'flex';
    document.getElementById('id_line_ten_quantity_label').style.display = 'flex';
    document.getElementById('id_line_ten_unit_price_label').style.display = 'flex';
    document.getElementById('id_line_ten_total_price_label').style.display = 'flex';


    });






    });









    