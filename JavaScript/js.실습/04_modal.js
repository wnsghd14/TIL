const modalToggle = function() {
  document.querySelector('#modal-content').classList.toggle('active')
}

const modalBtn = document.querySelector('#modal-btn')
modalBtn.addEventListener('click', modalToggle)


const modalOverlay = document.querySelector('#modal-content')
modalOverlay.addEventListener('click', modalToggle)
