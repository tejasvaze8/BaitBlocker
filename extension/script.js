// script.js
const apiEndpoint = 'http://100.64.161.177:5000/';

chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  // tabs is an array of tab objects
  var currentTab = tabs[0];
  
  // Access the URL of the current tab
  var currentTabUrl = currentTab.url;
  
  // Now you can use currentTabUrl as needed
  document.getElementById("urlInput").value = currentTabUrl;


});
function callApi(apiEndpoint, urlParameter) {
  // Construct the full API URL
  const fullApiUrl = `${apiEndpoint}/generate_summary`;

  // Define the request headers
  const headers = {
    'Content-Type': 'application/json',
    // Add any additional headers if required by your API
  };

  // Construct the request body
  const requestBody = JSON.stringify({ url: urlParameter });

  // Make a POST request to the API
  fetch(fullApiUrl, {
    method: 'POST',
    headers: headers,
    body: requestBody,
  })
    .then(response => {
      // Check if the response status is OK (status code 200-299)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      // Parse the response body as JSON
      return response.json();
    })
    .then(data => {
      // Handle the data from the API response
      console.log(data);
      new_Title(data.Revised_title);
      generateSummary(data.Revised_summary);
      // You can do further processing or update UI based on the API response here
    })
    .catch(error => {
      // Handle errors during the fetch operation
      console.error('Fetch error:', error);
    });
   
  
}

var story = "In a quaint town, mysterious packages began arriving at doorsteps every Friday. No one knew the sender, yet the parcels held personalized gifts, uncannily fitting each recipient's desires. Speculation buzzed, and excitement grew with each delivery. As friendships formed over shared surprises, the once-quiet community blossomed into a tapestry of joy. Local businesses thrived, as townsfolk eagerly anticipated their weekly enchanting presents. The secret benefactor remained elusive, leaving the town enchanted in wonder. In the heart of uncertainty, the unspoken agreement was clear — the magic of the unknown had woven a tale of unity and kindness, forever altering their ordinary Fridays."
document.getElementById("openButton").addEventListener("click", function() {
  openUrl();
});

document.getElementById("openButton2").addEventListener("click", function() {
  createAnswer("HELLO THIS IS TEXT");
});

function openUrl() {
  var url = document.getElementById("urlInput").value;
  if (url) {
    callApi(apiEndpoint, url);
    saveUrl(url);

    createQuestion();
  }
}
function showURL(urlT){
  var url = document.getElementById("urlTest");
  url.textContent = urlT

}
function saveUrl(url) {
  console.log("URL saved:", url);
}
function displayUrl(url) {
  var displayedUrlElement = document.getElementById("displayedUrl");
  displayedUrlElement.textContent = "URL: " + url;
}
function new_Title(title) {
  var newTitle = document.getElementById("newTitle");
  var newTitleName = document.getElementById("newTitleName");
  newTitle.textContent = "New Title";
  newTitleName.textContent = title;
}
function generateSummary(summaryText){
  var summaryTitle = document.getElementById("summaryTitle");
  var summary = document.getElementById("summary");
  summaryTitle.textContent = "Summary";
  summary.textContent = summaryText;
}
function createQuestion(){
  var question = document.getElementById("questionBox");
  if (question.style.visibility=='visible') {
    question.style.visibility = 'hidden';
  }
  else 
    question.style.visibility = 'visible';
}

function createAnswer(text) {
  var answer = document.getElementById("answerText");
  if (answer.style.visibility=='visible') {
    answer.style.visibility = 'hidden';
  }
  else 
    answer.style.visibility = 'visible';  
    answer.textContent = text; 
}