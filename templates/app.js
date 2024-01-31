



function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  
  var name = document.getElementById("uiName");
  var processor = document.getElementById("uiProcessor");
  var ram = document.getElementById("uiRam");
  var os = document.getElementById("uiOs");
  var storage = document.getElementById("uiStorage");
  var display = document.getElementById("uiDisplay");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_laptop_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
    
      name: name.value,
      processor: processor.value,
      ram: ram.value,
      os: os.value,
      storage: storage.value,
      display: display.value,



  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_all_data"; // Use this if you are NOT using nginx which is first 7 tutorials
  // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var names = data.names;
          var processors = data.processors;
          var oss = data.oss;
          var rams = data.rams;
          var displays = data.displays;
          var storages = data.storages;

          var uiName = document.getElementById("uiName");
          var uiProcessor = document.getElementById("uiProcessor");
          var uiOs = document.getElementById("uiOs");
          var uiRam = document.getElementById("uiRam");
          var uiStorage = document.getElementById("uiStorage");
          var uiDisplay = document.getElementById("uiDisplay");
          $('#uiName').empty();
          for(var i in names) {
              var opt = new Option(names[i]);
              $('#uiName').append(opt);
          }
          $('#uiProcessor').empty();
          for(var i in names) {
              var opt = new Option(processors[i]);
              $('#uiProcessor').append(opt);
          }
          $('#uiOs').empty();
          for(var i in oss) {
              var opt = new Option(oss[i]);
              $('#uiOs').append(opt);
          }
          $('#uiRam').empty();
          for(var i in rams) {
              var opt = new Option(rams[i]);
              $('#uiRam').append(opt);
          }
          $('#uiStorage').empty();
          for(var i in storages) {
              var opt = new Option(storages[i]);
              $('#uiStorage').append(opt);
          }
          $('#uiDisplay').empty();
          for(var i in displays) {
              var opt = new Option(displays[i]);
              $('#uiDisplay').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
