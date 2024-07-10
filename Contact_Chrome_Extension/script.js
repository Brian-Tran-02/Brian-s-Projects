document.addEventListener('DOMContentLoaded', function () {         //Once the HTML file has finished running, do the following
    const emailList = document.getElementById('email-list');        //"document" refers to the html file.  therefore, we are getting the element from the HTML file with name 'email-list' and setting it to variable emailList
    const emailInput = document.getElementById('email-input');
    const nameInput = document.getElementById('name-input');
    const addEmailButton = document.getElementById('add-email');
  
    // Load saved emails from storage
    chrome.storage.sync.get(['emails'], function (result) {
      const emails = result.emails || [];
      emails.forEach(displayEmail);
    });
  
    // Add email button click handler
    addEmailButton.addEventListener('click', function () {
      const email = emailInput.value;
      const name = nameInput.value;
      if (email && name) {
        const emailData = { email, name };
        chrome.storage.sync.get(['emails'], function (result) {
          const emails = result.emails || [];
          emails.push(emailData);
          chrome.storage.sync.set({ emails: emails }, function () {
            displayEmail(emailData);
            emailInput.value = '';
            nameInput.value = '';
          });
        });
      }
    });
  
    // Display email entry
    function displayEmail(emailData) {
        const div = document.createElement('div');
        div.innerHTML = `
          <span>${emailData.name}: </span>
          <a href="mailto:${emailData.email}" target="_blank">${emailData.email}</a>
        `;
        
        emailList.appendChild(div);
      }
  });
  