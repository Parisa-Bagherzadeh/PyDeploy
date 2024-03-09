var settings = {
    "url": "https://thispersondoesnotexist.com/",
    "method": "GET",
    "timeout": 0,
  };
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });