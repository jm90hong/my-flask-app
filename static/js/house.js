$(document).ready(function(){

   $("#predict-btn").on('click',function(){
      var area = $("#area").val();
      var year = $("#year").val();
      var income = $("#income").val();
      var school_rating = $("#school-rating").val();
      var transit_score = $("#transit-score").val();
      var rooms = $("#rooms").val();
   
      var postData = {
         area: area,
         year: year,
         income: income,
         school_rating: school_rating,
         transit_score: transit_score,
         rooms: rooms
      };
   
   
      console.log(postData);
      


      $.ajax({
         url:"./api/ai/predict-house-price",
         type:"get",
         data:postData,
         success:function(response){

            var price_by_lin = convert_to_comma(response.price_by_lin,'$');
            var price_by_rf = convert_to_comma(response.price_by_rf,'$');


          


            $("#result-text-1").text(price_by_lin);
            $("#result-text-2").text(price_by_rf);
            alert("예측 완료");
         },
         error:function(error){
            console.log(error);
         }
      });

   });



   function convert_to_comma(number,simbol){
     number = Math.floor(number);
     return simbol+number.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",")
   }

   





   


});