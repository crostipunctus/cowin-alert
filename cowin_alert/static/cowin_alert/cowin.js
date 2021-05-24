document.addEventListener('DOMContentLoaded', function() {

let today = new Date();
let dd = String(today.getDate()).padStart(2, '0');
let mm = String(today.getMonth() + 1).padStart(2, '0'); 
let yyyy = today.getFullYear();

today = dd + '-' + mm + '-' + yyyy;
console.log(today)

let start = document.querySelector('#start')

fetch('user_dict')
  .then(response => response.json())
  .then(data1 => 
  

  start.onclick = function () {
  
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;}


  window.setInterval(function() {
    data1.forEach(element => {
      
      console.log(element)
  


    fetch(`https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=${element}&date=${today}`)
      
    
              .then(response => response.json())
              .then(data =>  {
                
                console.log(data)

               fetch('py_api', {
                method: 'POST',
                body: JSON.stringify({
                    centers: data,
                    id: `${element}`,
                    headers: {"X-CSRFToken": getCookie("csrftoken")}
                           
                })
  
            })
              .then(response => console.log(response))
            
            })
  
          })
  }, 5000)
  
  
  
  
  
}
  
  )
  })
  
  