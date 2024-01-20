// script.js
var story = "In a quaint town, mysterious packages began arriving at doorsteps every Friday. No one knew the sender, yet the parcels held personalized gifts, uncannily fitting each recipient's desires. Speculation buzzed, and excitement grew with each delivery. As friendships formed over shared surprises, the once-quiet community blossomed into a tapestry of joy. Local businesses thrived, as townsfolk eagerly anticipated their weekly enchanting presents. The secret benefactor remained elusive, leaving the town enchanted in wonder. In the heart of uncertainty, the unspoken agreement was clear — the magic of the unknown had woven a tale of unity and kindness, forever altering their ordinary Fridays."
document.getElementById("openButton").addEventListener("click", function() {
  openUrl();
});

function openUrl() {
  var url = document.getElementById("urlInput").value;
  if (url) {

    saveUrl(url);

    new_Title(url)//change to new title later.
    generateSummary(story)
  }
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
function generateSummary(summary){
  var summaryTitle = document.getElementById("summaryTitle");
  var summary = document.getElementById("summary");
  summaryTitle.textContent = "Summary";
  summary.textContent = "hey";
}