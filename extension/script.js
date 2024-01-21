// script.js
chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  // tabs is an array of tab objects
  var currentTab = tabs[0];
  
  // Access the URL of the current tab
  var currentTabUrl = currentTab.url;
  
  // Now you can use currentTabUrl as needed
  document.getElementById("urlInput").value = currentTabUrl;


});


var story = "In a quaint town, mysterious packages began arriving at doorsteps every Friday. No one knew the sender, yet the parcels held personalized gifts, uncannily fitting each recipient's desires. Speculation buzzed, and excitement grew with each delivery. As friendships formed over shared surprises, the once-quiet community blossomed into a tapestry of joy. Local businesses thrived, as townsfolk eagerly anticipated their weekly enchanting presents. The secret benefactor remained elusive, leaving the town enchanted in wonder. In the heart of uncertainty, the unspoken agreement was clear — the magic of the unknown had woven a tale of unity and kindness, forever altering their ordinary Fridays."
document.getElementById("openButton").addEventListener("click", function() {
  openUrl();
});

function openUrl() {
  var url = document.getElementById("urlInput").value;
  if (url) {

    saveUrl(url);

    new_Title(url);//change to new title later.
    generateSummary(story);
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
  var question = document.getElementById("questionBox")
  if (question.style.visibility=='visible') {
    question.style.visibility = 'hidden';
  }
  else 
    question.style.visibility = 'visible'
}