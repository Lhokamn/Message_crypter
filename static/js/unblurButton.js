// Get references to the text element and button
const textElement = document.getElementById('container-getter-link');
const buttonElement = document.getElementById('unblurButton');

textElement.classList.toggle('blurred');

// Function to toggle the blur effect
buttonElement.addEventListener('click', function() {
  // Toggle the 'blurred' class on the text element
  textElement.classList.toggle('blurred');

  // Update the button text based on the current state
  if (textElement.classList.contains('blurred')) {
    buttonElement.textContent = 'Unblur Text';
  } else {
    buttonElement.textContent = 'Blur Text';
  }
});