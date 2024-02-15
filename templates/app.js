



function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  
  var brand = document.getElementById("uiBrand");
  var laptoptype = document.getElementById("uiLaptoptype");
  var ram = document.getElementById("uiRam");
  var weight = document.getElementById("uiWeight");
  var os = document.getElementById("uiOs");
  var gpu = document.getElementById("uiGpu");
  var touchscreen = document.getElementById("uiTouchscreen");
  var ips = document.getElementById("uiIps");
  var harddrive = document.getElementById("uiHarddrive");
  
  var ssd = document.getElementById("uiSsd");
  var screen = document.getElementById("uiScreen");
  var screensize = document.getElementById("uiScreensize");
  var processor = document.getElementById("uiProcessor");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_laptop_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
    
      brand: brand.value,
      laptoptype: laptoptype.value,
      ram: ram.value,
      weight: weight.value,
      os: os.value,
      gpu: gpu.value,
      touchscreen: touchscreen.value,
      ips: ips.value,
      harddrive: harddrive.value,
      ssd: ssd.value,
      screen: screen.value,
      screensize: screensize.value,
      processor: processor.value,





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
          var brands = data.brands;
          var laptoptypes = data.laptoptypes;
          var rams = data.rams;
          var weights = data.weights;
          var oss = data.oss;
          var gpus = data.gpus;
          var touchscreens = data.touchscreens;
          var ipss = data.ipss;
          var harddrives = data.harddrives;
          var ssds = data.ssds;
          var gpus = data.gpus;
          var screens = data.screens;
          var screensizes = data.screensizes;
          var processors = data.processors;

          var uiBrand = document.getElementById("uiBrand");
          var uiLaptoptype = document.getElementById("uiLaptoptype");
          var uiRam = document.getElementById("uiRam");
          var uiWeight = document.getElementById("uiWeight");
          var uiOs = document.getElementById("uiOs");
          var uiGpu = document.getElementById("uiGpu");
          var uiTouchscreen = document.getElementById("uiTouchscreen");
          var uiIps = document.getElementById("uiIps");
          var uiHarddrive = document.getElementById("uiHarddrive");
          var uiSsd = document.getElementById("uiSsd");
          var uiScreen = document.getElementById("uiScreen");
          var uiScreensize = document.getElementById("uiScreensize");
          var uiProcessor = document.getElementById("uiProcessor");
          
          $('#uiBrand').empty();
          for(var i in rams) {
              var opt = new Option(brands[i]);
              $('#uiBrand').append(opt);
          }
          $('#uiLaptoptype').empty();
          for(var i in laptoptypes) {
              var opt = new Option(laptoptypes[i]);
              $('#uiLaptoptype').append(opt);
          }
          $('#uiRam').empty();
          for(var i in rams) {
              var opt = new Option(rams[i]);
              $('#uiRam').append(opt);
          }
          $('#uiWeight').empty();
          for(var i in weights) {
              var opt = new Option(weights[i]);
              $('#uiWeight').append(opt);
          }
          $('#uiOs').empty();
          for(var i in oss) {
              var opt = new Option(oss[i]);
              $('#uiOs').append(opt);
          }
          $('#uiGpu').empty();
          for(var i in gpus) {
              var opt = new Option(gpus[i]);
              $('#uiGpu').append(opt);
          }
          $('#uiTouchscreen').empty();
          for(var i in touchscreens) {
              var opt = new Option(touchscreens[i]);
              $('#uiTouchscreen').append(opt);
          }
          $('#uiIps').empty();
          for(var i in ipss) {
              var opt = new Option(ipss[i]);
              $('#uiIps').append(opt);
          }
          $('#uiHarddrive').empty();
          for(var i in harddrives) {
              var opt = new Option(harddrives[i]);
              $('#uiHarddrive').append(opt);
          }
          $('#uiSsd').empty();
          for(var i in ssds) {
              var opt = new Option(ssds[i]);
              $('#uiSsd').append(opt);
          }
          $('#uiScreen').empty();
          for(var i in screens) {
              var opt = new Option(screens[i]);
              $('#uiScreen').append(opt);
          }
          $('#uiScreensize').empty();
          for(var i in screensizes) {
              var opt = new Option(screensizes[i]);
              $('#uiScreensize').append(opt);
          }
          $('#uiProcessor').empty();
          for(var i in processors) {
              var opt = new Option(processors[i]);
              $('#uiProcessor').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
