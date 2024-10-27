document.addEventListener("DOMContentLoaded", () => {
  const percentageDisplay = document.querySelector(".loading-percentage");
  const loadingBar = document.querySelector(".loading-bar");
  const finalMessage = document.querySelector(".final-message"); // Select the final message

  let progress = 0;
  const interval = setInterval(() => {
    if (progress < 100) {
      progress++;
      percentageDisplay.textContent = `${progress}%`;
      loadingBar.style.width = `${progress}%`;

      console.log(`Progress: ${progress}%`);
    } else {
      clearInterval(interval);
      
      
      console.log("Loading complete! Displaying final message.");
      
     
      finalMessage.style.opacity = "1"; 
      finalMessage.style.transform = "translateY(0)"; 


      console.log("Final message styles applied:", {
        opacity: finalMessage.style.opacity,
        transform: finalMessage.style.transform
      });
    }
  }, 60); 
});
