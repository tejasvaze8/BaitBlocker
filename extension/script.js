// script.js

document.getElementById("openButton").addEventListener("click", function() {
  openUrl();
});

function openUrl() {
  var url = document.getElementById("urlInput").value;
  if (url) {
    saveUrl(url);
  }
}

function saveUrl(url) {
  console.log("URL saved:", url);
  // You can perform additional actions with the URL as needed
}
