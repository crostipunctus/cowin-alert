document.addEventListener('DOMContentLoaded', function() {


  
  let slots = document.querySelector("#slots")
  
  slots.onclick = function av_slots() {
  
  window.setInterval(function() {
  
    fetch(`https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date=15-05-2021`)
              .then(response => response.json())
              .then(data =>  {
                  
               fetch('', {
                method: 'POST',
                body: JSON.stringify({
                    centers: data,
                           
                })
  
            })
            .then(response => console.log(response.json()))
        
            })
  
  
  }, 5000)
  
  
  
  }
  
  
  
  })
  
  