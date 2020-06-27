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
});