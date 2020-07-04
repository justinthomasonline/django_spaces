$(document).ready(function(){
var i=1;

    $('#add-more-property-image').click(function()
    { 
      $html=`<div class="col-lg-6 mt-2" >
      Type
      <select name="image-`+i+`-PropertyImageType" class="form-control" maxlength="200" id="id_image-`+i+`-PropertyImageType">
<option value="0">Property Image</option>

<option value="1">Floor Plan</option>

</select>
      
    </div>

    <div class="col-lg-6 mt-2">
      Image
      <input type="file" name="image-`+i+`-PropertyImage" class="form-control py-4" accept="image/*" id="id_image-`+i+`-PropertyImage">
      
    </div>`  

$("#add_property_img_contianer").append($html);

i++;
    });




    var n=1;

    $('#add-more-property-nearby').click(function()
    { 
      $html=`<div class="col-lg-6 mt-2">
          Near by type
          <select name="nearby-`+n+`-NearbyType" class="form-control" maxlength="200" id="id_nearby-`+n+`-NearbyType">
<option value="0">Education</option>

<option value="1">Health &amp; Medical</option>

<option value="3">Transportation</option>

</select>
          
        </div>

        <div class="col-lg-6 mt-2">
          Distance in kilo meters
          <input type="file" name="nearby-`+n+`-Distance" class="form-control py-4" maxlength="200" id="id_nearby-`+n+`-Distance">
          
        </div>`  

$("#add_property_nearby_contianer").append($html);

n++;
    });


    $('.aminities').click(function(){

        var aminity="";
        $('.aminities:checked').each(function(){
          aminity+=$(this).val()+",";
        });
        aminity=aminity.substring(0,aminity.length-1);
        $("#selected-aminity").val(aminity);

    });


    var selected_aminities = $("#selected-aminity").val().split(",");

    var selected_aminities_array = [];
       $.each(selected_aminities,function(i){
        selected_aminities_array.push(selected_aminities[i]);
      });
      

    $('.aminities').each(function(){

      if ($.inArray($(this).val(),selected_aminities_array)!== -1)
      {
       $(this).attr('checked','checked');
      }

    });

  


    $('#id_RentBuy').change(function(){
     
      $.ajax({
        type:"GET",
        cache:false,
        url:"Ajaxgetproperttype",
        data:{value: $('#id_RentBuy option:selected').val()},
        success: function (data) { 
          $("#id_PropertyType").empty();
          $("#id_PropertyType").append("<option value=''>--Select--</option>");
          for (var i=0;i<data.length;++i)
         {
          
          $("#id_PropertyType").append("<option value='"+data[i].pk+"'>"+data[i].fields.Type+"</option>");
         }

        }
         
      });
      
    });




    $('#id_MainLocation').change(function(){
     
      $.ajax({
        type:"GET",
        cache:false,
        url:"Ajaxgetsublocation",
        data:{value: $('#id_MainLocation option:selected').val()},
        success: function (data) { 
          $("#id_SubLocation").empty();
          $("#id_SubLocation").append("<option value=''>--Select--</option>");
          for (var i=0;i<data.length;++i)
         {
          
          $("#id_SubLocation").append("<option value='"+data[i].pk+"'>"+data[i].fields.SubLocationName+"</option>");
         }

        }
         
      });
      
    });

});