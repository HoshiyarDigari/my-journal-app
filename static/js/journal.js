//  function to populate date on journal landing page to the current date

addEventListener('DOMContentLoaded', setDate)
function setDate(){
    // Date object converts  Date.now() which is epoch time to 'Mon Dec 09 2024 12:57:33 GMT-0500 (Eastern Standard Time)
    const now = new Date(Date.now());
    // converting this to the format accepted by the Date HTML element
    formattedDate = now.toISOString().split('T')[0];
    formattedTime = now.toISOString().split('T')[1];

    document.getElementById('journalDate').value = formattedDate;
    
    

}