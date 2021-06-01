document.addEventListener('DOMContentLoaded', function() {

  let state_selector = document.querySelector('#select-states')
  let district_selector = document.querySelector('#select-districts')
  
  district_selector.style.display = 'none'
  
  state_selector.onchange = function () {
    let state_name = state_selector.value
  
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

 fetch('districts', {
  method: 'POST',
  credentials: 'same-origin',
  headers: {"X-CSRFToken": csrftoken},
  body: JSON.stringify({
      state: `${state_name}`,
   
  })
  

})
.then(response => response.json())
.then(data => {

  console.log(data)
  district_selector.style.display = 'block'

  let i, x = district_selector.options.length - 1;
  for (i = x; i >= 0; i--) {
    district_selector.remove(i)
  }

  for (i = 0; i < data.length; i++) {
    let opt = data[i]
    let el = document.createElement('option')
    el.textContent = opt;
    el.value = opt;
    district_selector.appendChild(el);
  }

})







}



})