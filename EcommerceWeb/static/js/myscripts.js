function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    var currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
          /*check if the item starts with the same letters as the text field value:*/
          if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            /*create a DIV element for each matching element:*/
            b = document.createElement("DIV");
            /*make the matching letters bold:*/
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            /*insert a input field that will hold the current array item's value:*/
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            /*execute a function when someone clicks on the item value (DIV element):*/
            b.addEventListener("click", function(e) {
                /*insert the value for the autocomplete text field:*/
                inp.value = this.getElementsByTagName("input")[0].value;
                /*close the list of autocompleted values,
                (or any other open lists of autocompleted values:*/
                closeAllLists();
            });
            a.appendChild(b);
          }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
          /*If the arrow DOWN key is pressed,
          increase the currentFocus variable:*/
          currentFocus++;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 38) { //up
          /*If the arrow UP key is pressed,
          decrease the currentFocus variable:*/
          currentFocus--;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 13) {
          /*If the ENTER key is pressed, prevent the form from being submitted,*/
          e.preventDefault();
          if (currentFocus > -1) {
            /*and simulate a click on the "active" item:*/
            if (x) x[currentFocus].click();
          }
        }
    });
    function addActive(x) {
      /*a function to classify an item as "active":*/
      if (!x) return false;
      /*start by removing the "active" class on all items:*/
      removeActive(x);
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);
      /*add class "autocomplete-active":*/
      x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
      /*a function to remove the "active" class from all autocomplete items:*/
      for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
      }
    }
    function closeAllLists(elmnt) {
      /*close all autocomplete lists in the document,
      except the one passed as an argument:*/
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
          x[i].parentNode.removeChild(x[i]);
        }
      }
    }
    /*execute a function when someone clicks in the document:*/
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
  }
  
  /*An array containing all the country names in the world:*/
  var countries = ["Teknosa","Hepsiburada","n11","Trendyol","ÇiçekSepeti","Casper","MSI","HP","Fujitsu","Acer","Asus","Hometech","Razer","Monster","Dell","Lenovo","Apple","0","2","3","4","5","6","7","10","11","12","Intel Core i9","Intel Core i5","Apple M2","Intel Core i7","Intel Celeron","Apple M1","AMD Ryzen 7","AMD Ryzen 3","AMD Ryzen 9","AMD A6","AMD Athlon","Intel Core i3","Intel Xeon","AMD","AMD Ryzen 5","16,1","14","13,4","17","17,3","14,5","13,3","14,1","15,6","13,6","16","1 TB256 GB","250 GB","256 GB","256 GB256 GB","512 GB","500 GB","1 GB","240 GB","128 GB","120 GB","2 TB","1 TB512 GB","1 TB","20 GB","4 GB","8 GB","16 GB","64 GB","32 GB","12 GB","24 GB","Freedos","Ubuntu","Windows","Linux","MacOS","HDD","SSD","SSD+HDD","ExpertBook","PULSE","Pulse","X515FA-EJ031","Nitro","X509FA-EJ950T09","Book","E14","X415FA-EK0662","D515DA-BR998","X515JA-EJ2120A72","Swift","240","Vivobook","Legion","Stealth","ProArt","X415FA-EK0663","Inspiron","M5760","15-DW4010NTA14","Nirvana","Ni̇rvana","ThinkPad","255","V15","Extensa","XPS","15-DW4010NTA34","X515MA-EJ494","Alfa","X515JA-EJ2120A108","E15","17-CN2004NTA41","B1500CEPE-BQ0726","Delta","Summit","Precision","X515JA-EJ2120A3","X415FA-EK06623","D409BA-BV167T","Rog","Ideapad","GF63","G15","M7760","X515JA-EJ2120A12","X515JF-EJ354","F35OBF821NA43","WF66","Katana","Pavilion","X415FA-EK06626","IdeaPad","X415FA-EK06618","V14","ProBook","ZBook","X515JA-EJ2119","X515MA-EJ435","Envy","D515DA-BR3169","X515JA-EJ2120A15","Elitebook","X415FA-EK06627","15-DW4010NT","X515EA-BQ1843","NB","TravelMate","X515JA-EJ2120A17","X415FA-EK06639","Proart","X509FA-EJ950T02","Prestige","15-DW4010NTA12","MacBook","D515DA-BQ980","Thinkpad","X515JA-EJ2112W","Aspire","D515DA-BQ9802","X415FA-EK06619","VivoBook","X415FA-EK06617","V17","Huma","Vostro","X415FA-EK06610","450","17-CN2004NT","EliteBook","WS76","X415FA-EK0666","PRESTIGE","Modern","Bravo","ThinkBook","Expertbook","250","Latitude","D515DA-BR408","Lifebook","Victus","B1500CEPE-BQ072630","17-CN2000NT","Creator","X415FA-EK06622","ROG","X415FA-EK0661","Omen","X515EA-EJ1314","T14","X509FA-EJ950T","WS","LifeBook","Raider","17-CN2001NT"];
  
  /*initiate the autocomplete function on the "myInput" element, and pass along the countries array as possible autocomplete values:*/
  autocomplete(document.getElementById("myInput"), countries);