document.getElementById('copyButton').addEventListener('click', function() {
    // Get the text from the div
    var textToCopy = document.getElementById('linkSending').innerText;

    // Create a temporary textarea element to hold the text
    var tempInput = document.createElement('textarea');

    tempInput.value = textToCopy;

    console.log(textToCopy)

    document.body.appendChild(tempInput);

    // Select the text and copy it
    tempInput.select();

    document.execCommand('copy');
    // Remove the temporary element
    document.body.removeChild(tempInput);

    // Change the button text to "Copied!"
    copyButton.innerText = 'Copied!';
    
    // Optionally, reset the button text back after a short delay
    setTimeout(() => {
        copyButton.innerText = 'Copy';
    }, 2000); // Change this delay (in milliseconds) as needed
});
