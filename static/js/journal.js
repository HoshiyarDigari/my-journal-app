//  function to populate date on journal landing page to the current date

addEventListener('DOMContentLoaded', setDateTime)
function setDateTime(){
    // Date object converts  Date.now() which is epoch time to 'Mon Dec 09 2024 12:57:33 GMT-0500 (Eastern Standard Time)
    // new Date() gives the local browser Date
    const today = new Date();
    // converting this to the format accepted by the Date HTML element
    formattedDate = today.toLocaleDateString('en-CA');
    // set journalDate on the page
    document.getElementById('journalDate').value = formattedDate;
    
    //get only the hour and minute for use with journalTime input
    formattedTime = today.toLocaleTimeString('en-US',{hour:'2-digit', minute:'2-digit', hour12:false});  
    // set JournalTime 
    document.getElementById('journalTime').value = formattedTime;
    
    

}