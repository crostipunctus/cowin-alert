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
                    id: `${element}`
                           
                })
  
            })
              .then(response => console.log(response))
            
            })
  
          })
  }, 5000)
  
  
  
  
  
}
  
  )
  })
  
  