$(document).ready(function(){
  $(".hide").hide();
  $(".marker-cafe").click(function(){
     $(".hide").hide();
    $(".cafe-txt").fadeIn(300);
  });

  $(".marker-guest_services").click(function(){
     $(".hide").hide();
    $(".GuestServices-txt").fadeIn(300);
  });
  
  $(".marker-tugboat").click(function(){
     $(".hide").hide();
    $(".Tugboat-txt").fadeIn(300);
  });

  $(".marker-kidsport").click(function(){
     $(".hide").hide();
    $(".Kidsport-txt").fadeIn(300);
  });
});