// Get references to the text element and button
const textElement = document.getElementById('container-getter-link');
const buttonElement = document.getElementById('unblurButton');

textElement.classList.toggle('blurred');

// Function to toggle the blur effect
buttonElement.addEventListener('click', function() {
  // Toggle the 'blurred' class on the text element
  textElement.classList.toggle('blurred');

  const url = window.location.hostname

  const token = window.location.pathname;

  const urlDelete = `/delete`;

  fetch(urlDelete, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ token })
  })
  .then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data.message); // Handle the response from the backend
    console.log("Token deleted successfully:", data);
  })
  .catch(error => {
    console.error("Error deleting token:", error);

  });
});
