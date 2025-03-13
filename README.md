# baitBlocker

<img src="extension/baitblaocker22.png" alt="Extension Logo" width="400" height="266">

## Overview

A Chrome extension that simplifies dense and clickbaity articles, for whenever you'd much rather have a tl;dr.

Our extension will pull the link from the webpage you are currently browsing and will temporarily save the text to our database. We then will run a sentence embedding model to embed the text and create a simple RAG pipeline, injecting the knowledge in the webpage to the LLM. We have the option to crawl through links found in the original webpage to further the context for the LLM. 

This allows you to ask questions about specific articles or even codebases. Similar to some emergent LLMs attatched to documentation of libraries, we can also start generating code from documentation of lesser known libraries that the LLM might not be familiar with.

## Features

### 1. Summary Generation

Generate concise summaries for simplified understanding of an article or wall of text. Sums up the key points.

### 2. Title Revision

Generate new titles based on the contents of the article.

### 3. Question Integration

Ask questions related to article right from the extension, without the need to redirect to a new tab.

### 4. Fish

Cool fish for when the data is loading.

## Installation

1. Open up Chrome options and navigate to your extensions to enable Developer Mode. Select "Load a new extension" and select the extension folder you downloaded from the repository. You should now be able to use the extension.

