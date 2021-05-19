document.addEventListener('DOMContentLoaded', function() {


  

  
  window.setInterval(function() {
  
    fetch('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=725&date=19-05-2021')
      
    
              .then(response => response.json())
              .then(data =>  {
                
                console.log(data)

               fetch('py_api', {
                method: 'POST',
                body: JSON.stringify({
                    centers: data,
                           
                })
  
            })
              .then(response => console.log(response))
            
            })
  
  
  }, 5000)
  
  
  
  
  
  
  
  })
  
  